from dagster_dbt import build_schedule_from_dbt_selection

from .assets import dbt_calendar_assets

dbt_calendar_schedule = build_schedule_from_dbt_selection(
    [dbt_calendar_assets],
    job_name="materialize_dbt_models",
    cron_schedule="0 0 * * *",
    dbt_select="*",
)

schedules = [dbt_calendar_schedule]