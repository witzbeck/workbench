from dagster import Definitions

from .assets import assets
from .jobs import jobs
from .resources import resources
from .schedules import schedules

defs = Definitions(
    assets=assets,
    resources=resources,
    schedules=schedules,
    jobs=jobs,
)
