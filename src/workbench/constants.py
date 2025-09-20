from enum import Enum
from pathlib import Path


class DBT_SELECT(Enum):
    ALL = "*"
    CALENDAR = "model.calendar.*"


class ASSET_GROUPS(Enum):
    CALENDAR = "Calendar"
    REPORTS = "Reports"

# Paths --------------------------------------------------------------------
DATA_PATH = Path("/opt/dagster/data")
DBT_PROJECT_FILE = Path("/home/abeckwit/repos/workbench/dbt_project.yml")
DBT_PROFILES_FILE = Path("/home/abeckwit/repos/workbench/profiles.yml")
PROJECT_PATH = Path("/home/abeckwit/repos/workbench")