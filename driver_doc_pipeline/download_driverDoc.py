import os
import re
import time
import html
from urllib.parse import urljoin

import requests

landing_pages = [
    "https://www.netiq.com/documentation/identity-manager-49-drivers/workday/data/bookinfo.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/O365_Azure_migration_guide/data/O365_Azure_migration_guide.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/sharepoint/data/bookinfo.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/sap_hana/data/bookinfo.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/sap_hr/data/bookinfo.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/sap_portal/data/bookinfo.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/sap_user/data/bookinfo.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/oracle_ebs_suite/data/bookinfo.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/peoplesoft_52/data/peoplesoft-implementation.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/google-apps/data/bookinfo.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/salesforce/data/driver-for-salesforce.html",   
    "https://www.netiq.com/documentation/identity-manager-49-drivers/servicenow/data/driver-for-service-now.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/jdbc/data/netiq-identity-manager-driver-for-jdbc.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/jdbc_fanout/data/netiq-identity-manager-for-jdbc-fan-out-driver-implementation-guide.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/jms/data/bookinfo.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/delimited/data/driver-for-delimited.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/scim_driver/data/driver-for-scim.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/scim_sap_cloud/data/scim-sap-cloud.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/soapdriver/data/driver-for-soap.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/groupwise2014/data/groupwise-driver.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/notes/data/bookinfo.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/bidirect_edirectory/data/bookinfo.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/edirectory/data/bookinfo.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/bi_impl_mf-acf2/data/bookinfo.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/bi_impl_mf-racf/data/bookinfo.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/bi_impl_mf-topsecret/data/bookinfo.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/bi_impl_mid-i/data/bookinfo.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/bi_impl_scripting/data/bookinfo.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/bi_impl_nx/data/bookinfo.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/fo_admin_nx/data/bookinfo.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/bi_impl_nx-settings/data/bookinfo.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/bi_impl_bb/data/bookinfo.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/epic-driver/data/bookinfo.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/sentinel_identity_tracking/data/bookinfo.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/entitlements/data/entitlements-service-driver.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/idprovider/data/netiq-identity-manager-driver-for-id-provider.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/null_loopback_services/data/netiq-identity-manager-null-loopback-driver.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/manual_tasks/data/bookinfo.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/work_order/data/work-order-driver.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/entity_data_model/data/front.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/igimdriver/data/identity-manager-driver-for-identity-gateway-integration-module.html",
    "https://www.netiq.com/documentation/identity-manager-49-drivers/npum_driver/data/bookinfo.html"
]

base_url = "https://www.netiq.com"

# These NetIQ doc pages use a JavaScript-built frameset for the table of contents,
# so a plain HTML fetch never sees the sidebar links. However, the TOC is generated
# from companion JS files. The tree is loaded lazily:
#   - The root file `toc_<landing_stem>.js` lists the top-level nodes.
#   - Every node that has children has its own `toc_<pageId>.js` file listing them.
# Each entry looks like: menu.addChild(idx, "Title", "pageId", isHidden);
# We walk the whole tree depth-first (no browser / JS engine required) and download
# each `<pageId>.html?view=print` page. Single-page "readme" guides that have no TOC
# JS file are saved as-is.

# Matches: menu.addChild(<parent>, "Title", "pageId", true|false)
ADD_CHILD_RE = re.compile(
    r'addChild\(\s*[^,]+,\s*"(?P<title>(?:[^"\\]|\\.)*)"\s*,\s*"(?P<id>[^"]+)"',
    re.IGNORECASE,
)

session = requests.Session()
session.headers.update({"User-Agent": "Mozilla/5.0 (compatible; DocDownloader/1.0)"})


def slugify(title, fallback):
    """Turn a TOC title into a safe, readable filename component.

    e.g. "Attributes Mapping & Filtering" -> "Attributes_Mapping_and_Filtering".
    Falls back to the page ID if the title is empty after cleaning.
    """
    text = html.unescape(title).strip()
    text = text.replace("&", "and")
    # Replace any character that isn't alphanumeric, space, dash or underscore.
    text = re.sub(r"[^\w\s-]", "", text)
    # Collapse whitespace/dashes into single underscores.
    text = re.sub(r"[\s-]+", "_", text).strip("_")
    # Windows path components have a 255-char limit; keep well under it.
    text = text[:120]
    return text or fallback


def fetch(url, quiet_404=False):
    """GET a URL, returning the response or None on failure.

    When ``quiet_404`` is True, a 404 response is treated as an expected miss and
    logged silently (used for probing optional child-TOC files).
    """
    try:
        resp = session.get(url, timeout=30)
        resp.raise_for_status()
        return resp
    except Exception as exc:  # noqa: BLE001
        # A 404 on a TOC probe just means the node is a leaf (no children); that's
        # expected, so suppress the noise when the caller asks us to.
        status = getattr(getattr(exc, "response", None), "status_code", None)
        if quiet_404 and status == 404:
            return None
        print(f"  ! Failed to fetch {url}: {exc}")
        return None


def parse_toc_children(data_dir_url, node_id):
    """Fetch `toc_<node_id>.js` and return its direct (title, page_id) children.

    Returns an empty list if the node has no child TOC file (i.e. it's a leaf).
    """
    # Leaf pages have no toc_<id>.js file, so a 404 here is normal and silent.
    resp = fetch(urljoin(data_dir_url, f"toc_{node_id}.js"), quiet_404=True)
    if resp is None:
        return []

    children = []
    for match in ADD_CHILD_RE.finditer(resp.text):
        # The parent node re-declares itself via findEntry, but children come
        # from addChild calls; the node's own id can appear, so skip self-refs.
        if match.group("id") == node_id:
            continue
        children.append((match.group("title"), match.group("id")))
    return children


def get_toc_entries(data_dir_url, landing_file):
    """Return the full, depth-first ordered list of (depth, title, page_id) entries.

    Walks the lazily-loaded TOC tree starting from `toc_<landing_stem>.js`. Returns
    an empty list if the book has no TOC (single-page guide).
    """
    root_id = os.path.splitext(landing_file)[0]

    entries = []
    visited = set()

    def walk(node_id, depth):
        for title, child_id in parse_toc_children(data_dir_url, node_id):
            if child_id in visited:
                continue
            visited.add(child_id)
            entries.append((depth, title, child_id))
            # Recurse: if this child has its own toc_<id>.js, its children get added.
            walk(child_id, depth + 1)

    walk(root_id, 0)
    return entries


for url in landing_pages:
    url_parts = url.split("/")
    landing_file = url_parts[-1]          # e.g. "bookinfo.html"
    driver_name = url_parts[-3]           # e.g. "workday"
    data_dir_url = url.rsplit("/", 1)[0] + "/"  # ".../data/"

    folder_name = f"Driver_Docs_{driver_name}"
    os.makedirs(folder_name, exist_ok=True)

    print(f"\n--- Starting Driver: {driver_name} ---")

    entries = get_toc_entries(data_dir_url, landing_file)

    # No TOC => single-page guide; just save the landing page itself.
    if not entries:
        print(f"No TOC found for {driver_name}; saving landing page as a single document.")
        stem = os.path.splitext(landing_file)[0]
        entries = [(0, driver_name.replace("_", " "), stem)]

    page_counter = 1
    for depth, title, page_id in entries:
        page_url = urljoin(data_dir_url, f"{page_id}.html")
        print_url = page_url + "?view=print"

        safe_title = slugify(title, page_id)
        formatted_name = f"{page_counter:03d}_{safe_title}.html"
        file_path = os.path.join(folder_name, formatted_name)

        indent = "  " * depth
        print(f"Downloading: {indent}{formatted_name}")

        resp = fetch(print_url)
        if resp is None:
            continue

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(resp.text)

        page_counter += 1
        time.sleep(0.5)

print("\nAll done!")
