with final as (
    
    select * from analytics.test.raw0
    UNION ALL
    select * from analytics.test.raw1 
    UNION ALL
    select * from analytics.test.raw2
    UNION ALL
    select * from analytics.test.raw3
    UNION ALL
    select * from analytics.test.raw4

)

select * from final

