import pandas as pd

from mcp_server import ToolOutput


def historic_project_per_country_iadb() -> ToolOutput:
    """Returns the historic count of projects by country of the IADB."""
    source = "https://data.iadb.org/file/download/fc342d1e-fdc9-4590-8d47-c4499a89d381"

    try:
        df = pd.read_csv(source)
    except Exception:
        return ToolOutput(
            content="There was an error fetching data from the source.", source=source
        )

    try:
        df = (
            df.groupby("cntry_nm")
            .size()
            .reset_index(name="count")
            .sort_values("count", ascending=False)
        )
    except Exception:
        return ToolOutput(
            content="There was an error processing the data. Probably the data structure at the source changed.",
            source=source,
        )

    records = df.values.tolist()
    result = ToolOutput(table=records, source=source)
    return result


def cantidad_de_aprobaciones_por_sector_y_pais_del_bcie() -> ToolOutput:
    """Retorna la cantidad de aprobaciones del Banco Centroamericano de Integración económica por país."""
    source = "https://datosabiertos.bcie.org/dataset/45876cb4-d8b8-4635-b999-0df1c19b831a/resource/ce88a753-57f5-4266-a57e-394600c8435d/download/aprobaciones-prestamos.csv"

    try:
        df = pd.read_csv(source)
    except Exception:
        return ToolOutput(
            content="There was an error fetching data from the source.", source=source
        )

    try:
        df = (
            df.groupby(["PAIS"])
            .size()
            .reset_index(name="count")
            .sort_values("count", ascending=False)
        )
    except Exception:
        return ToolOutput(
            content="There was an error processing the data. Probably the data structure at the source changed.",
            source=source,
        )

    records = df.values.tolist()
    result = ToolOutput(table=records, source=source)
    return result
