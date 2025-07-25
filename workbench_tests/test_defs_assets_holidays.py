"""Unit tests for holiday assets and associated asset checks.
"""

import datetime

import pandas as pd
from dagster import AssetCheckResult

from workbench.defs.asset_checks import (
    holiday_max_date_check,
    holiday_min_date_check,
    holidays_no_nulls_check,
    holidays_non_empty_check,
    holidays_within_bounds_check,
)
from workbench.defs.assets.calendars import holiday_max_date, holiday_min_date, holidays


def test_holiday_min_date_first_of_year():
    """holiday_min_date returns January 1 of five years ago."""
    min_date = holiday_min_date()
    today = datetime.date.today()
    assert min_date.year == today.year - 5
    assert min_date.month == 1
    assert min_date.day == 1


def test_holiday_max_date_last_of_next_year():
    """holiday_max_date returns December 31 of next year."""
    max_date = holiday_max_date()
    today = datetime.date.today()
    assert max_date.year == today.year + 1
    assert max_date.month == 12
    assert max_date.day == 31


def test_holidays_dataframe_structure_and_bounds():
    """holidays returns a non-empty DataFrame with correct structure and date bounds."""
    min_date = holiday_min_date()
    max_date = holiday_max_date()
    df = holidays(min_date, max_date)
    assert isinstance(df, pd.DataFrame)
    assert "holiday" in df.columns
    assert not df.empty
    assert pd.api.types.is_datetime64_any_dtype(df["holiday"])
    assert df["holiday"].min().date() >= min_date
    assert df["holiday"].max().date() <= max_date


def test_holidays_no_duplicates():
    """holidays returns unique dates without duplicates."""
    df = holidays(holiday_min_date(), holiday_max_date())
    assert df["holiday"].is_unique


# Tests for asset check functions

def test_holiday_min_date_check_success():
    """Check that holiday_min_date_check passes for the correct date."""
    result = holiday_min_date_check(holiday_min_date())
    assert isinstance(result, AssetCheckResult)
    assert result.passed


def test_holiday_min_date_check_failure():
    """Check that holiday_min_date_check fails for an incorrect date."""
    bad_date = datetime.date(2000, 2, 2)
    result = holiday_min_date_check(bad_date)
    assert not result.passed


def test_holiday_max_date_check_success():
    """Check that holiday_max_date_check passes for the correct date."""
    result = holiday_max_date_check(holiday_max_date())
    assert isinstance(result, AssetCheckResult)
    assert result.passed


def test_holiday_max_date_check_failure():
    """Check that holiday_max_date_check fails for an incorrect date."""
    bad_date = datetime.date(2000, 1, 1)
    result = holiday_max_date_check(bad_date)
    assert not result.passed


def test_holidays_non_empty_check_success_and_failure():
    """Check holidays_non_empty_check rejects empty DataFrames and accepts non-empty ones."""
    empty_df = pd.DataFrame({"holiday": []})
    result_empty = holidays_non_empty_check(empty_df)
    assert not result_empty.passed
    valid_df = holidays(holiday_min_date(), holiday_max_date())
    result_valid = holidays_non_empty_check(valid_df)
    assert result_valid.passed


def test_holidays_no_nulls_check_success_and_failure():
    """Check holidays_no_nulls_check rejects DataFrames with nulls and accepts ones without."""
    null_df = pd.DataFrame({"holiday": [pd.NaT]})
    result_null = holidays_no_nulls_check(null_df)
    assert not result_null.passed
    df_valid = holidays(holiday_min_date(), holiday_max_date())
    result_valid_no_nulls = holidays_no_nulls_check(df_valid)
    assert result_valid_no_nulls.passed


def test_holidays_within_bounds_check_success_and_failure():
    """Check holidays_within_bounds_check rejects dates outside the range and accepts valid ones."""
    min_date = holiday_min_date()
    max_date = holiday_max_date()
    out_of_bounds_df = pd.DataFrame({"holiday": [pd.to_datetime(min_date) - pd.Timedelta(days=1)]})
    result_fail = holidays_within_bounds_check(out_of_bounds_df)
    assert not result_fail.passed
    valid_df_bounds = holidays(min_date, max_date)
    result_pass = holidays_within_bounds_check(valid_df_bounds)
    assert result_pass.passed
