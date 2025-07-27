SELECT * FROM {{ ref('relative_dates') }}
WHERE day_offset BETWEEN -30 AND -1
