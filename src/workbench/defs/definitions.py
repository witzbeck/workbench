from pathlib import Path

from dagster import Definitions
from dagster_dbt import DbtProject

from .asset_checks import asset_checks as py_asset_checks
from .assets import assets
from .resources import resources
from .schedules import schedules

project_path = Path(__file__).parent.parent
project = DbtProject(project_dir=project_path)


defs = Definitions(
    assets=assets,
    asset_checks=py_asset_checks,
    resources=resources,
    schedules=schedules,
)
