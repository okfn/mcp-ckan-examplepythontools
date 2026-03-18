# MCP CKAN Plugin Example

This is an example of a [MCP CKAN](https://github.com/okfn/mcp-ckan) Plugin that register tools to answer data based on Open Data.

## How to create a MCP Plugin

1. Init a package repository:

```bash
uv init --package mcp-ckan-exampleplugin
```

2. Define a `register_tools(mcp)` function that register tools in a MCP Server:

```python
def register_tools(mcp):
    @mcp.tool()
    def greetings_from_examplepythontools():
        return "Hello from mcp_ckan_examplepythontools!"
```

3. Register a new `mcp_ckan` entrypoint in the `pyproject.toml` file that calls the `register_tools` function.

```toml
[project.entry-points."mcp_ckan"]
mcp-ckan-examplepythontools = "mcp_ckan_examplepythontools:register_tools"
```

4. Install it in the same virtual environment as your server.

```bash
uv pip install "git+https://github.com/okfn/mcp-ckan"
uv pip install "git+https://github.com/okfn/mcp-ckan-examplepythontools"
uv run mcp-ckan
```
