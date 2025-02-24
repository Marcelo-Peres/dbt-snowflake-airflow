with source as (
select 
    id,
    name,
    'I love dbt, snowflake and airflow' as description
from {{ ref('stg_tb_developer') }}
)

select * from source