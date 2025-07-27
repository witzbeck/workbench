SELECT * FROM {{ ref('relative_dates') }}
WHERE week_completed = 1 AND week_offset = -1
