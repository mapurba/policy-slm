# LLM-Powered DirXML Policy Builder

This project is a proof-of-concept for an LLM-powered tool to help developers build and understand DirXML policies. It uses a Neo4j graph database as a knowledge base, populated with data from the DirXMLScript DTD and official documentation.

The core of the project is a hybrid search engine that combines semantic (vector) search and full-text keyword search to provide highly accurate and context-aware results for natural language queries about DirXML policy elements.

## Features

- **Robust Data Pipeline**: Automatically parses the DirXML DTD and markdown documentation to build a comprehensive knowledge graph.
- **Hybrid Search**: Combines vector embeddings, full-text search, and graph traversal for accurate, relationship-aware search results.
- **Neo4j Backend**: Leverages the power of graph databases to represent and query the complex relationships between policy elements.
- **Thoroughly Documented**: The codebase is fully documented to help new developers get started quickly.

## Requirements

- Python 3.8+
- A running Neo4j instance (AuraDB or a local install is recommended).
- **Neo4j Credentials**: The application currently expects the Neo4j URI, username, and password to be hardcoded in the scripts. Before running, please update the credentials at the top of `load_to_neo4j.py` and `policy_search_api.py`.

## Setup & Usage

### 1. Installation

Clone the repository and install the required Python packages.

```bash
git clone <repository-url>
cd <repository-directory>
pip install -r requirements.txt
```

### 2. Build the Knowledge Base

Run the following script to parse all the data, generate embeddings, and load everything into your Neo4j instance. This will create the graph that the search API uses.

```bash
python3 build_database.py
```

This process may take a few minutes, especially on the first run as it needs to download the sentence-transformer model.

### 3. Verify the Installation

To ensure that the data has been loaded correctly and the search functionality is working, you can run two verification scripts.

**a) Vector Search Verification**

This script checks if the vector embeddings and indexes have been set up correctly in Neo4j.

```bash
python3 test_vector_search.py
```

**b) End-to-End Search Test**

This script runs several test queries against the search API to ensure it returns accurate and relevant results.

```bash
python3 test_relationship_search.py
```

You should see all tests passing successfully.

## Using the Search API

You can integrate the hybrid search into your own tools. The `search_elements` function in `policy_search_api.py` takes a natural language query and returns a ranked list of relevant policy elements.

Here is a simple example of how to use it:

```python
from policy_search_api import search_elements, close_driver

def perform_search(query):
    """
    Performs a search and prints the results.
    """
    print(f"Executing search for: '{query}'")
    results = search_elements(query)

    if not results:
        print("No results found.")
        return

    print("\n--- Search Results ---")
    # Print top 5 results for brevity
    for item in results[:5]:
        print(f"- Found: {item['name']} (Score: {item['score']:.2f}, Type: {item['match_type']})")
    print("----------------------\n")


if __name__ == '__main__':
    # Example queries
    search_query_1 = "how do I set a local variable?"
    search_query_2 = "condition for attribute equals"

    try:
        perform_search(search_query_1)
        perform_search(search_query_2)
    finally:
        # Clean up the database connection
        close_driver()

```

This example demonstrates how to find policy elements related to setting a local variable and checking an attribute value, showcasing the capabilities of the natural language search.
