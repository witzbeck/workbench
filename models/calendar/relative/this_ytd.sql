SELECT * FROM {{ ref('relative_dates') }}
WHERE year_offset = 0 AND is_past = 1
