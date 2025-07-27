
from dagster import Definitions
from dagster_dbt import DbtProject

from workbench.constants import PROJECT_PATH

from .asset_checks import asset_checks as py_asset_checks
from .assets import assets
from .resources import resources
from .schedules import schedules

project = DbtProject(project_dir=PROJECT_PATH)


defs = Definitions(
    assets=assets,
    asset_checks=py_asset_checks,
    resources=resources,
    schedules=schedules,
)
