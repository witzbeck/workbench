"""Unit tests for holiday assets and associated asset checks."""

import datetime

import pandas as pd
import pytest

from workbench.defs.assets import holidays


@pytest.fixture
def min_date():
    return datetime.date(datetime.date.today().year - 5, 1, 1)


@pytest.fixture
def max_date():
    return datetime.date(datetime.date.today().year + 1, 12, 31)


@pytest.fixture
def holidays_df():
    return holidays()


def test_holidays_dataframe_structure_and_bounds(holidays_df, min_date, max_date):
    """holidays returns a non-empty DataFrame with correct structure and date bounds."""
    assert isinstance(holidays_df, pd.DataFrame)
    assert "holiday" in holidays_df.columns
    assert not holidays_df.empty
    assert pd.api.types.is_datetime64_any_dtype(holidays_df["holiday"])


def test_holidays_no_duplicates(holidays_df):
    """holidays returns unique dates without duplicates."""
    assert holidays_df.loc[:, "holiday"].is_unique


def test_holidays_within_bounds(holidays_df, min_date, max_date):
    """holidays returns dates within the specified bounds."""
    assert holidays_df.loc[:, "holiday"].min().date() >= min_date
    assert holidays_df.loc[:, "holiday"].max().date() <= max_date
