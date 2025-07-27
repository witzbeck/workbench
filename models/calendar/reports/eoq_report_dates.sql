SELECT * FROM {{ ref('relative_dates') }} AS c
WHERE
    c.year
    = (
        SELECT MAX(d.year) FROM relative_dates AS d
        WHERE quarter_completed = 1
    )
    AND c.quarter_end < CURRENT_DATE
