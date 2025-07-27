from dagster import define_asset_job

update_holidays = define_asset_job("update_holidays", selection = "holidays")

jobs = [update_holidays]
