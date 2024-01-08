
with soruce as (
    select * from {{ref("extract")}}
),

data_transform as (
    select 
    INITCAP(LOWER(TRIM(first_name))) ,
    INITCAP(LOWER(TRIM(last_name))) ,
    CAST(TRIM(age) as INT) as age ,
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
    
    from soruce
    where TRY_TO_NUMBER(age) IS NOT NULL
)

select * from data_transform
