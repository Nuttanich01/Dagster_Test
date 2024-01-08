from my import assets

import os

from dagster_dbt import DbtCliClientResource
from my.assets import DBT_PROFILES, DBT_PROJECT_PATH
from dagster import ScheduleDefinition, Definitions, load_assets_from_modules, define_asset_job, Definitions

run_everything_job = define_asset_job("run_everything", selection="*")
resources = {
    "dbt": DbtCliClientResource(
        project_dir=DBT_PROJECT_PATH,
        profiles_dir=DBT_PROFILES,
    ),
}

defs = Definitions(
    assets=load_assets_from_modules([assets]), 
    resources=resources, 
    schedules=[
        ScheduleDefinition(
            job=run_everything_job,
            cron_schedule="@daily",
        ),],
    )


