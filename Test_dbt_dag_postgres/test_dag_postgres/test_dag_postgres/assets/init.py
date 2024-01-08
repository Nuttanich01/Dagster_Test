
from dagster_dbt import load_assets_from_dbt_project
from dagster import file_relative_path


DBT_PROJECT_PATH = file_relative_path(__file__, "../../../Test_dbt_postgres")
DBT_PROFILES = file_relative_path(__file__, "../../../Test_dbt_postgres")

dbt_assets = load_assets_from_dbt_project(
    project_dir=DBT_PROJECT_PATH, profiles_dir=DBT_PROFILES, key_prefix=["public"]
)

