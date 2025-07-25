from dagster_duckdb import DuckDBResource
from dagster_duckdb_pandas import DuckDBPandasIOManager

from workbench.constants import DATA_PATH

db_path = DATA_PATH / "workbench.db"

workbench_db = DuckDBResource(database=db_path)
workbench_io = DuckDBPandasIOManager(database=db_path)
