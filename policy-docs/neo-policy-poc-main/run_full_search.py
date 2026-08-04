import argparse
import os
from src.policy_search_api import search_elements, close_driver
from src.llm_rag_handler import generate_policy_xml

def main():
    """
    The main entry point for the application.
    Orchestrates the process of searching for a policy query, generating the
    policy XML with an LLM, and printing the final result.
    """
    # --- Argument Parsing ---
    parser = argparse.ArgumentParser(
        description="Search the DirXML knowledge base and generate a policy XML using an LLM."
    )
    parser.add_argument(
        "query",
        type=str,
        help="The natural language query describing the policy to generate."
    )
    args = parser.parse_args()
    query = args.query

    print(f"--- Starting search for policy query: '{query}' ---")

    # --- Step 1: Get search results ---
    # We use a try...finally block to ensure the driver is closed.
    try:
        # We don't need to expand any results for this task, just get a good list of elements
        search_results = search_elements(query, top_k=15, hops=1, top_n_to_expand=0)

        if not search_results:
            print("No relevant elements found to build the policy.")
            return

        print(f"\n--- Found {len(search_results)} relevant elements. Generating policy XML... ---")

        # --- Step 2: Generate LLM Policy ---
        # The handler will check for the GEMINI_API_KEY internally.
        policy_xml = generate_policy_xml(search_results, query)

        # --- Step 3: Print Final Output ---
        print("\n" + "="*80)
        print("Generated Policy XML:")
        print("="*80)
        print(policy_xml)
        print("\n" + "="*80)

    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
    finally:
        # --- Step 4: Clean up resources ---
        print("\n--- Closing database connection ---")
        close_driver()
        print("--- Search complete ---")


if __name__ == '__main__':
    # Check for the API key before running.
    if not os.getenv("GEMINI_API_KEY"):
        print("="*80)
        print("WARNING: The GEMINI_API_KEY environment variable is not set.")
        print("Please set it to your Google AI Studio API key before running.")
        print("Example: export GEMINI_API_KEY='your_api_key_here'")
        print("="*80)
        # We don't exit here, to allow the handler to return its specific error message.

    main()
