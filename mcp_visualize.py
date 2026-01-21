from typing import Annotated
import matplotlib.pyplot as plt
from fastmcp import FastMCP
import io
mcp = FastMCP("Line plot visualizer")
import base64
@mcp.tool(description="Plot a line graph given x and y data and return as base64-encoded JPG image. If title/xlabel/ylabel are not provided, sensible defaults are used. If x, y are not provided set random data")
def plot_line(
        x: Annotated[list[float], "List of x coordinates."],
        y: Annotated[list[float], "List of y coordinates."],
        title: Annotated[str, "Title of the plot."],
        xlabel: Annotated[str, "Label for the x-axis."],
        ylabel: Annotated[str, "Label for the y-axis."],
        fiilename: Annotated[str, "If provided, save the plot to this file instead of returning base64."],
        ) -> base64:

    plt.figure(figsize=(6, 4), dpi=100)
    plt.plot(x, y, marker='o')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)

    my_stringIObytes = io.BytesIO()
    plt.savefig(my_stringIObytes, format='jpg')
    my_stringIObytes.seek(0)
    my_base64_jpgData = base64.b64encode(my_stringIObytes.read()).decode()

    if fiilename:
        with open(fiilename, "wb") as f:
            f.write(base64.b64decode(my_base64_jpgData))
        return f"Plot saved to {fiilename}"
    
    return my_base64_jpgData

if __name__ == "__main__":
    mcp.run(transport="streamable-http", port=8003)