from typing import Any, Dict

from dagster import AutoMaterializePolicy
from dagster_dbt import DagsterDbtTranslator, DbtCliResource, dbt_assets

from workbench.constants import ASSET_GROUPS

from ..projects import project
from .calendars import assets as calendars_assets


class CalendarGroupTranslator(DagsterDbtTranslator):
    def get_group_name(self, node_info: Dict[str, Any]) -> str:
        return ASSET_GROUPS.CALENDAR.value

    def get_auto_materialize_policy(self, node_info: Dict[str, Any]) -> AutoMaterializePolicy:
        return AutoMaterializePolicy.eager()

@dbt_assets(project=project, manifest=project.manifest_path, dagster_dbt_translator=CalendarGroupTranslator())
def dbt_calendar_assets(context, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()

assets = calendars_assets + [dbt_calendar_assets]
