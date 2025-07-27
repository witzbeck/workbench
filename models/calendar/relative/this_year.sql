SELECT * FROM {{ ref('relative_dates') }}
WHERE year_offset = 0
