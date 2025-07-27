from dagster import job

from .assets.calendars import holiday_max_date, holiday_min_date, holidays


@job
def update_holidays():
    holidays(holiday_min_date(), holiday_max_date())
