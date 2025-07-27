from dagster_dbt import DbtCliResource, dbt_assets

from .calendars import assets as calendars_assets
from .projects import project


@dbt_assets(project=project, manifest=project.manifest_path)
def dbt_calendar_assets(context, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()

assets = calendars_assets + [dbt_calendar_assets]
