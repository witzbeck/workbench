SELECT * FROM {{ ref('relative_dates') }}
WHERE quarter_completed = 1 AND quarter_offset = -1
