from typing import Annotated

from fastmcp import FastMCP

mcp = FastMCP("Date utilities")
import datetime

@mcp.tool(description="Get current date in YYYY-MM-DD format")
def get_current_date() -> str:
    return datetime.date.today().isoformat()

@mcp.tool(description="Get current datetime in ISO 8601 format")
def get_current_datetime() -> str:
    return datetime.datetime.now().isoformat()

if __name__ == "__main__":
    mcp.run(transport="streamable-http", port=8002)