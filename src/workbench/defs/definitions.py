from pathlib import Path
from dagster import Definitions
from dagster_dbt import dbt_assets
from .assets import assets as py_assets


project_path = Path(__file__).parent.parent
project = DbtProject(project_dir=project_path)
assets = py_assets + dbt_assets(
    project=project,
    select=["model.calendar.dates"],
)

defs = Definitions(
    assets=assets
)