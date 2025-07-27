from dagster import ScheduleDefinition
from dagster_dbt import build_schedule_from_dbt_selection

from .assets import dbt_calendar_assets
from .jobs import update_holidays

dbt_calendar_schedule = build_schedule_from_dbt_selection(
    [dbt_calendar_assets],
    job_name="materialize_dbt_models",
    cron_schedule="0 0 * * *",
    dbt_select="*",
)

update_holidays_schedule = ScheduleDefinition(
    name="update_holidays_schedule",
    job=update_holidays,
    cron_schedule="0 0 * * *",
)

schedules = [dbt_calendar_schedule, update_holidays_schedule]
