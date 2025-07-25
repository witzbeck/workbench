SELECT
    d.year,
    d.quarter,
    CONCAT('Q', CAST(d.quarter AS VARCHAR))
        AS quarter_name,
    MIN(d.date) AS quarter_start,
    MAX(d.date) AS quarter_end
FROM dates AS d
GROUP BY d.year, d.quarter
