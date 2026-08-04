# DirXMLScript DTD Elements Tree

This document lists all tags (elements) defined in the DirXMLScript DTD, including policies, rules, actions, arguments, and tokens. Each tag is shown with its description and content model.

## Top-Level Elements

- **policy**
  - **description**
  - **include**
  - **rule**
    - **comment**
    - **conditions**
      - **and**
      - **or**
    - **actions**
      - **do-add-association**
      - **do-add-dest-attr-value**
      - **do-add-dest-object**
      - **do-add-role**
      - **do-add-resource**
      - **do-add-src-attr-value**
      - **do-add-src-object**
      - **do-append-xml-element**
      - **do-append-xml-text**
      - **do-break**
      - **do-clear-dest-attr-value**
      - **do-clear-op-property**
      - **do-clear-src-attr-value**
      - **do-clone-op-attr**
      - **do-clone-xpath**
      - **do-create-resource**
      - **do-create-role**
      - **do-delete-dest-object**
      - **do-delete-src-object**
      - **do-find-matching-object**
      - **do-for-each**
      - **do-if**
      - **do-while**
      - ... (see JSON for all actions)

## Argument Elements

- **arg-actions**
- **arg-conditions**
- **arg-association**
- **arg-component**
- **arg-dn**
- **arg-match-attr**
- **arg-node-set**
- **arg-object**
- **arg-password**
- **arg-query-condition**
- **arg-string**
- **arg-value**

## Token Elements

- **token-added-entitlement**
- **token-association**
- **token-attr**
- **token-base64-decode**
- **token-base64-encode**
- **token-char**
- **token-class-name**
- **token-convert-time**
- **token-dest-attr**
- **token-dest-dn**
- **token-dest-name**
- **token-document**
- **token-entitlement**
- **token-escape-for-dest-dn**
- **token-escape-for-src-dn**
- **token-generate-password**
- **token-global-variable**
- **token-join**
- **token-json-array**
- **token-json-object**
- **token-local-variable**
- **token-lower-case**
- **token-map**
- **token-map-source-col**
- **token-named-password**
- **token-op-attr**
- **token-op-property**
- **token-operation**
- **token-parse-dn**
- **token-password**
- **token-query**
- **token-removed-attr**
- **token-removed-entitlement**
- **token-replace-all**
- **token-replace-first**
- **token-resolve**
- **token-split**
- **token-src-attr**
- **token-src-dn**
- **token-src-name**
- **token-substring**
- **token-text**
- **token-time**
- **token-unique-name**
- **token-unmatched-src-dn**
- **token-upper-case**
- **token-xml-parse**
- **token-xml-serialize**
- **token-xpath**

---

This list is complete as of the current JSON and DTD. For full details, see the JSON file or the DTD/Markdown documentation files.
