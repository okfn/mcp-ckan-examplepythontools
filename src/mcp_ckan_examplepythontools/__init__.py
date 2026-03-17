def register_tools(mcp):
    @mcp.tool()
    def greetings_from_examplepythontools():
        return "Hello from mcp_ckan_examplepythontools!"


def main() -> None:
    print("Hello from mcp-ckan-examplepythontools!")
