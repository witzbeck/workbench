import datetime
from typing import Any, Dict

import pandas as pd
from dagster import AutoMaterializePolicy, asset
from dagster_dbt import DagsterDbtTranslator, DbtCliResource, dbt_assets
from pandas.tseries.holiday import USFederalHolidayCalendar

from workbench.constants import ASSET_GROUPS

from ..projects import project


@asset(
    kinds={"python"},
    key_prefix=["main"],
    io_manager_key="workbench_io",
    group_name=ASSET_GROUPS.CALENDAR.value,
    auto_materialize_policy=AutoMaterializePolicy.eager(),
)
def holidays() -> pd.DataFrame:
    """Returns a DataFrame of US federal holidays between 5 years ago and next year."""
    today = datetime.date.today()
    min_date = datetime.date(today.year - 5, 1, 1)
    max_date = datetime.date(today.year + 1, 12, 31)
    dates = USFederalHolidayCalendar().holidays(start=min_date, end=max_date).to_frame()
    dates.reset_index(drop=False, inplace=True)
    dates.columns = ["date", "holiday"]
    return dates


class CalendarGroupTranslator(DagsterDbtTranslator):
    def get_group_name(self, node_info: Dict[str, Any]) -> str:
        return ASSET_GROUPS.CALENDAR.value

    def get_auto_materialize_policy(
        self, node_info: Dict[str, Any]
    ) -> AutoMaterializePolicy:
        return AutoMaterializePolicy.eager()


@dbt_assets(
    project=project,
    manifest=project.manifest_path,
    dagster_dbt_translator=CalendarGroupTranslator(),
)
def dbt_calendar_assets(context, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()


assets = [holidays, dbt_calendar_assets]
