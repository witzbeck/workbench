from dagster_dbt import DbtCliResource
from dagster_duckdb import DuckDBResource
from dagster_duckdb_pandas import DuckDBPandasIOManager

from workbench.constants import DATA_PATH, PROJECT_PATH

db_path = DATA_PATH / "workbench.db"

workbench_db = DuckDBResource(database=db_path)
workbench_io = DuckDBPandasIOManager(database=db_path)
dbt = DbtCliResource(project_dir=PROJECT_PATH, profiles_dir=PROJECT_PATH)
resources = {
    "workbench_db": workbench_db,
    "workbench_io": workbench_io,
    "dbt": dbt,
}
