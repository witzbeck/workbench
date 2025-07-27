from dagster_dbt import DbtCliResource, DbtProject, dbt_assets

from workbench.constants import PROJECT_PATH

from .calendars import assets as calendars_assets

project = DbtProject(project_dir=PROJECT_PATH)
project.prepare_if_dev()

@dbt_assets(project=project, manifest=project.manifest_path)
def dbt_calendar_assets(context, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()

assets = calendars_assets + [dbt_calendar_assets]
