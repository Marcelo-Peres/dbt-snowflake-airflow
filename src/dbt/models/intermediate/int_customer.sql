SELECT
    ID,
    FIRST_NAME,
    LAST_NAME,
    birthdate
FROM {{ ref('stg_customers') }}