SELECT * FROM {{ref('stg_bookings_1')}}
UNION ALL
SELECT * FROM {{ref('stg_bookings_2')}}