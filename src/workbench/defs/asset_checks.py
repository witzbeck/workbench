"""Asset checks for holiday assets:
- Verifies holiday_min_date and holiday_max_date accuracy
- Validates holidays DataFrame integrity
"""


import pandas as pd
from dagster import AssetCheckResult, asset_check, load_asset_checks_from_current_module

from workbench.defs.assets import holidays


@asset_check(asset=holidays)
def holiday_min_date_check(df: pd.DataFrame) -> AssetCheckResult:
    """Ensure holiday_min_date returns January 1 of five years ago."""
    if df["date"].min().date().month == 1 and df["date"].min().date().day == 1:
        return AssetCheckResult(passed=True)
    return AssetCheckResult(passed=False, description=f"holiday_min_date must be January 1 but got {df['date'].min().date()}")

@asset_check(asset=holidays)
def holiday_max_date_check(df: pd.DataFrame) -> AssetCheckResult:
    """Ensure holiday_max_date returns December 31 of next year."""
    if df["date"].max().date().month == 12 and df["date"].max().date().day == 31:
        return AssetCheckResult(passed=True)
    return AssetCheckResult(passed=False, description=f"holiday_max_date must be December 31 but got {df['date'].max().date()}")

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

asset_checks = load_asset_checks_from_current_module()
