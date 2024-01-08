from dagster import (
    AssetSelection,
    Definitions,
    define_asset_job,
    load_assets_from_modules,
)

from TestDagSter.assets import extract,transform,load

all_assets = load_assets_from_modules([extract,transform,load])

dagster_job = define_asset_job("dagster_job", selection=AssetSelection.all())
defs = Definitions(
    assets=all_assets,
    jobs=[dagster_job]
)
