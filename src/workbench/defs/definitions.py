from pathlib import Path
from dagster import Definitions
from dagster_dbt import dbt_assets



project_path = Path(__file__).parent.parent
project = DbtProject(project_dir=project_path)

defs = Definitions(
    assets=[
        dbt_assets(
            project=project,
            select=["model.calendar.dates"],
        )
    ]
)