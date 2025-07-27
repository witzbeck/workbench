SELECT * FROM {{ ref('relative_dates') }} AS c
WHERE
    c.year
    = (
        SELECT MAX(d.year) FROM relative_dates AS d
        WHERE month_completed = 1
    )
    AND c.month_end < CURRENT_DATE
