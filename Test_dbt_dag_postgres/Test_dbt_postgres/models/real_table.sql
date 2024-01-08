with data_pass_transform as (
    select * from {{ref("transform_table")}}
    --test_dbt_dagster.public.transform_table

)

 select * from data_pass_transform