from dagster_dbt import DbtCliResource
from dagster_duckdb import DuckDBResource
from dagster_duckdb_pandas import DuckDBPandasIOManager

from ..constants import DATA_PATH, PROJECT_PATH

db_path = DATA_PATH / "workbench.db"

workbench_db = DuckDBResource(database=db_path.as_posix())
workbench_io = DuckDBPandasIOManager(database=db_path.as_posix())
dbt = DbtCliResource(project_dir=PROJECT_PATH, profiles_dir=PROJECT_PATH)
resources = {
    "workbench_db": workbench_db,
    "workbench_io": workbench_io,
    "dbt": dbt,
}
