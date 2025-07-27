
from dagster import Definitions

from .asset_checks import asset_checks as py_asset_checks
from .assets import assets
from .jobs import jobs
from .resources import resources
from .schedules import schedules

defs = Definitions(
    assets=assets,
    asset_checks=py_asset_checks,
    resources=resources,
    schedules=schedules,
    jobs=jobs,
)
