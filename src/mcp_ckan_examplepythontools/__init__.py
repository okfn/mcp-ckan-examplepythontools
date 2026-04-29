from mcp_ckan_examplepythontools import localtools


def register_tools(mcp):
    mcp.tool()(localtools.historic_project_per_country_iadb)
    mcp.tool()(localtools.cantidad_de_aprobaciones_por_sector_y_pais_del_bcie)
