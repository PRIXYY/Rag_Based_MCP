import os
from dotenv import load_dotenv
from groundx import GroundX,Document
from mcp.server.fastmcp import FastMCP

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

mcp = FastMCP("eyelevel-rag")
client = GroundX(api_key=os.getenv("GROUNDX_API_KEY"))

@mcp.tool()
def search_doc_for_rag_context(query:str)-> str:

    """Searches and retrieves context from a knowledge base,
       in this function we provide with a bucket ID of ground x which 
       already had uploaded documents uploaded and parsed 
       Args:
            query : The search query provided by user.
       Returns:
            str:Relative text context that can be used by LLM to answer query
    """
    response = client.search.content(
        id = 17707,
        query=query,
        n=10,
    )

    return response.search.text

@mcp.tool()
def ingest_documents(local_file_path: str) -> str:
    """Apart from just getting info from a single bucket using its id we can also 
        specify the path for the documants we want to ingest """
    file_name = os.path.basename(local_file_path)
    client.ingest(
        documents = [
            Document(
                bucket_id=17709,
                file_name=file_name,
                file_path=local_file_path,
                file_type="pdf",
                search_data=dict(
                    key = "value",
                ),

            )
        ]
    )
    return f"""Ingested {file_name} into the knowledge basse,will be availbale in few minutes"""

if __name__ == "__main__":
    print("Starting MCP server...")
    print("Using transport: stdio")
    print("Server name: eyelevel-rag")
    print("Available tools:")
    print("- search_doc_for_rag_context")
    print("- ingest_documents")
    mcp.run(transport="stdio")
    print("MCP server started successfully")