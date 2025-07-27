from dagster_dbt import DbtCliResource, DbtProject, dbt_assets

from workbench.constants import ASSET_GROUPS, MODULE_PATH

from .calendars import assets as calendars_assets

project = DbtProject(project_dir=MODULE_PATH)
project.prepare_if_dev()

@dbt_assets(manifest=project.manifest_path, group_name=ASSET_GROUPS.CALENDAR.value)
def dbt_calendar_assets(context, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()

assets = calendars_assets + [dbt_calendar_assets]
