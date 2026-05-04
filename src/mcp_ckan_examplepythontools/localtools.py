import pandas as pd

from mcp.types import CallToolResult, TextContent

from mcp_server import DataToolOutput
from mcp_server.results import text_result


def historic_project_per_country_iadb() -> DataToolOutput:
    """Returns the historic count of projects by country of the IADB."""
    source = "https://data.iadb.org/file/download/fc342d1e-fdc9-4590-8d47-c4499a89d381"
    try:
        df = (pd.read_csv(source)
            .groupby("cntry_nm")
            .size()
            .reset_index(name="count")
            .sort_values("count", ascending=False)
        )
        records = df.values.tolist()

        # Build markdown list
        markdown_lines = ["## Project Count by Country\n"]
        for country, count in records:
            markdown_lines.append(f"- **{country}**: {count} projects")
        markdown_lines.append(f"Source of the data: {source}")
        message = "\n".join(markdown_lines)

        return text_result(message, source, table=records)
    except Exception:
        message = "There was an internal error processing the data."
        return text_result(message, source_url=source)


def cantidad_de_aprobaciones_por_sector_y_pais_del_bcie() -> DataToolOutput:
    """Retorna la cantidad de aprobaciones del Banco Centroamericano de Integración económica por país."""
    source = "https://datosabiertos.bcie.org/dataset/45876cb4-d8b8-4635-b999-0df1c19b831a/resource/ce88a753-57f5-4266-a57e-394600c8435d/download/aprobaciones-prestamos.csv"

    try:
        df = pd.read_csv(source)
        df = (
            df.groupby(["PAIS"])
            .size()
            .reset_index(name="count")
            .sort_values("count", ascending=False)
        )
        records = df.values.tolist()

        # Build markdown list
        markdown_lines = ["## Aprobaciones del BCIE por País:\n"]
        for country, count in records:
            markdown_lines.append(f"- **{country}**: {count} aprobaciones")
        markdown_lines.append(f"Fuente de los datos: {source}")
        message = "\n".join(markdown_lines)

        return text_result(message, source, table=records)
    except Exception:
        message = "Hubo un error interno procesando los datos."
        return text_result(message, source_url=source)
