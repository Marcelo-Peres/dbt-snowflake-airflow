SELECT
    A.ID,
    A.FIRST_NAME,
    A.LAST_NAME,
    A.birthdate,
    B.BOOKING_REFERENCE,
    B.HOTEL,
    B.BOOKING_DATE,
    B.COST
FROM {{ref('stg_customers')}}  A
JOIN {{ref('int_combined_bookings')}} B
on A.ID = B.ID