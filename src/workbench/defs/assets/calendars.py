import datetime

import pandas as pd
from dagster import AutoMaterializePolicy, asset, load_assets_from_current_module
from pandas.tseries.holiday import USFederalHolidayCalendar

from workbench.constants import ASSET_GROUPS


@asset
def holiday_min_date() -> datetime.date:
    """Returns January 1 of five years ago."""
    today = datetime.date.today()
    return datetime.date(today.year - 5, 1, 1)


@asset
def holiday_max_date() -> datetime.date:
    """Returns December 31 of next year."""
    today = datetime.date.today()
    return datetime.date(today.year + 1, 12, 31)


@asset
def holidays(holiday_min_date: datetime.date, holiday_max_date: datetime.date) -> pd.DataFrame:
    """Returns a DataFrame of US federal holidays between holiday_min_date and holiday_max_date."""
    dates = USFederalHolidayCalendar().holidays(start=holiday_min_date, end=holiday_max_date)
    return pd.DataFrame({"holiday": dates})

assets = load_assets_from_current_module(
    group_name=ASSET_GROUPS.CALENDAR.value,
    auto_materialize_policy=AutoMaterializePolicy.eager(),
    )
