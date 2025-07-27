SELECT * FROM {{ ref('relative_dates') }}
WHERE month_offset = 0
