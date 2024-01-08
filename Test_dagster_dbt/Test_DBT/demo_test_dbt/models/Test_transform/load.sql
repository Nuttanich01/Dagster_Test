with real_data as (
    select * from {{ref("transform")}}
)

 select * from real_data