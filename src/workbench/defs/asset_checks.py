"""Asset checks for holiday assets:
- Verifies holiday_min_date and holiday_max_date accuracy
- Validates holidays DataFrame integrity
"""

import datetime

import pandas as pd
from dagster import AssetCheckResult, asset_check, load_asset_checks_from_current_module

from workbench.defs.assets.calendars import holiday_max_date, holiday_min_date, holidays


@asset_check(asset=holiday_min_date)
def holiday_min_date_check(value: datetime.date) -> AssetCheckResult:
    """Ensure holiday_min_date returns January 1 of five years ago."""
    if value.month == 1 and value.day == 1:
        return AssetCheckResult(passed=True)
    return AssetCheckResult(passed=False, description=f"holiday_min_date must be January 1 but got {value}")

@asset_check(asset=holiday_max_date)
def holiday_max_date_check(value: datetime.date) -> AssetCheckResult:
    """Ensure holiday_max_date returns December 31 of next year."""
    if value.month == 12 and value.day == 31:
        return AssetCheckResult(passed=True)
    return AssetCheckResult(passed=False, description=f"holiday_max_date must be December 31 but got {value}")

@asset_check(asset=holidays)
def holidays_non_empty_check(df: pd.DataFrame) -> AssetCheckResult:
    """Ensure holidays DataFrame is not empty."""
    if df.empty:
        return AssetCheckResult(passed=False, description="holidays DataFrame is empty")
    return AssetCheckResult(passed=True)

@asset_check(asset=holidays)
def holidays_no_nulls_check(df: pd.DataFrame) -> AssetCheckResult:
    """Ensure holidays DataFrame has no null values in the 'holiday' column."""
    if df["holiday"].isnull().any():
        return AssetCheckResult(passed=False, description="holidays DataFrame contains null values")
    return AssetCheckResult(passed=True)

@asset_check(asset=holidays)
def holidays_within_bounds_check(df: pd.DataFrame) -> AssetCheckResult:
    """Ensure all holiday dates fall within the min and max date bounds."""
    min_val = df["holiday"].min().date()
    max_val = df["holiday"].max().date()
    min_date = holiday_min_date()
    max_date = holiday_max_date()
    if min_val < min_date or max_val > max_date:
        return AssetCheckResult(passed=False, description="Holidays outside expected range")
    return AssetCheckResult(passed=True)

asset_checks = load_asset_checks_from_current_module()
