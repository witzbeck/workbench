from pathlib import Path

from dagster import Definitions
from dagster_dbt import DbtProject, load_assets_from_dbt_project

from .asset_checks import asset_checks as py_asset_checks
from .assets import assets as py_assets
from .resources import resources

project_path = Path(__file__).parent.parent
project = DbtProject(project_dir=project_path)
assets = py_assets + load_assets_from_dbt_project(
    project_dir=str(project.project_dir),
    profiles_dir=str(project.project_dir),
)

defs = Definitions(
    assets=assets,
    asset_checks=py_asset_checks,
    resources=resources,
)
