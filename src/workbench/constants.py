from pathlib import Path

MODULE_PATH = Path(__file__).parent
MODULE_SOURCE_PATH = MODULE_PATH.parent
PROJECT_PATH = MODULE_SOURCE_PATH.parent
DATA_PATH = PROJECT_PATH / "data"
DBT_PROJECT_FILE = MODULE_PATH / "dbt_project.yml"
DBT_PROFILES_FILE = MODULE_PATH / "profiles.yml"
