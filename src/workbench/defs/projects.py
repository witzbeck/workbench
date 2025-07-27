from dagster_dbt import DbtProject

from workbench.constants import PROJECT_PATH

project = DbtProject(project_dir=PROJECT_PATH)
project.prepare_if_dev()
