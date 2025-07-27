from dagster import define_asset_job

jobs = [define_asset_job("update_holidays", selection = "holidays")]
