SELECT
    d.year,
    d.week,
    CAST(MIN(d.date) AS DATE) AS week_start,
    CAST(MAX(d.date) AS DATE) AS week_end
FROM {{ ref('dates') }} AS d
GROUP BY d.year, d.week
