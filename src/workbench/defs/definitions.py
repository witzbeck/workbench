from pathlib import Path

from dagster import Definitions
from dagster_dbt import DbtProject, dbt_assets

from .asset_checks import asset_checks as py_asset_checks
from .assets import assets as py_assets
from .resources import resources

project_path = Path(__file__).parent.parent
project = DbtProject(project_dir=project_path)
assets = py_assets + dbt_assets(
    project=project,
    select=["model.calendar.dates"],
)

defs = Definitions(
    assets=assets,
    asset_checks=py_asset_checks,
    resources=resources,
)
