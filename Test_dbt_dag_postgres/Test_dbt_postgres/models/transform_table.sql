
with raw_data as (
    select * from {{ref("extract_table")}}
    --test_dbt_dagster.public.extract_table
    
    
),

 data_pass_transform as (
    select 
    INITCAP(LOWER(TRIM(first_name))) as First_name,
    INITCAP(LOWER(TRIM(last_name))) as Last_name,
    CAST(TRIM(age) as INT) as Age ,
    (CASE
        WHEN sex LIKE 'MF' THEN 'LGBT'
        WHEN sex LIKE 'both' THEN 'LGBT'
        WHEN sex LIKE 'FM' THEN 'LGBT'
        WHEN sex LIKE 'Male' THEN 'M'
        WHEN sex LIKE 'm' THEN 'M'
        WHEN sex LIKE 'Man' THEN 'M'
        WHEN sex LIKE 'f' THEN 'F'
        WHEN sex LIKE 'Female' THEN 'F'
        WHEN sex LIKE 'Girl' THEN 'F'
        ELSE 'Not Defined' 
    END) AS sex
    
    from raw_data
    WHERE age ~ '^\d+$'  -- Only select rows with numeric age values
    --where TRY_TO_NUMBER(age) IS NOT NULL
)

select * from data_pass_transform
