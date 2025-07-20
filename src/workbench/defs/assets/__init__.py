import datetime

import dagster as dg
import pandas as pd


@dg.asset
def holiday_min_date() -> datetime.date:
    """Returns the minimum date for the holiday calendar, 5 years ago from Jan 1."""
    today = datetime.date.today()
    return datetime.date(today.year - 5, 1, 1)


@dg.asset
def holiday_max_date() -> datetime.date:
    """Returns the maximum date for the holiday calendar, Dec 31 of next year."""
    today = datetime.date.today()
    return datetime.date(today.year + 1, 12, 31)


@dg.asset
def holidays(
    holiday_min_date: datetime.date, holiday_max_date: datetime.date
) -> pd.DataFrame:
    """
    Returns a DataFrame of US federal holidays between holiday_min_date and holiday_max_date.

    Args:
        holiday_min_date (datetime.date): The start date for the holiday range.
        holiday_max_date (datetime.date): The end date for the holiday range.

    Returns:
        pd.DataFrame: DataFrame with a DatetimeIndex of US federal holidays.
    """
    # Generate the holiday dates as a DatetimeIndex
    holiday_dates = pd.tseries.holiday.USFederalHolidayCalendar().holidays(
        start=holiday_min_date, end=holiday_max_date
    )
    # Return as a DataFrame for consistency and downstream compatibility
    return pd.DataFrame({"holiday": holiday_dates})

assets = dg.load_assets_from_current_module()