
from test_dag_postgres.assets import all_file,init,raw_table

from dagster_dbt import DbtCliClientResource
from test_dag_postgres.assets.init import DBT_PROFILES, DBT_PROJECT_PATH
from dagster import ScheduleDefinition, Definitions, load_assets_from_modules, define_asset_job, Definitions

run_everything_job = define_asset_job("run_everything", selection="*")
resources = {
    "dbt": DbtCliClientResource(
        project_dir=DBT_PROJECT_PATH,
        profiles_dir=DBT_PROFILES,
    ),
}

defs = Definitions(
    assets=load_assets_from_modules([all_file,init,raw_table]), 
    resources=resources, 
    schedules=[
        ScheduleDefinition(
            job=run_everything_job,
            cron_schedule="@daily",
        ),],
    )
