SELECT
    d.year,
    d.quarter,
    d.month,
    MONTHNAME(d.date) AS month_name,
    MIN(CAST(d.date AS DATE)) AS month_start,
    MAX(CAST(d.date AS DATE)) AS month_end
FROM dates AS d
GROUP BY d.year, d.quarter, d.month, MONTHNAME(d.date)
