with raw_data as (
    
    select * from {{ source('public', 'raw_table') }}
    --test_dbt_dagster.public.raw_table

)   

select * from raw_data
