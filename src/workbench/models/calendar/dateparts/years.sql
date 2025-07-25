SELECT
    year_value AS year,
    days_in_year,
    CAST(year_value AS VARCHAR) AS year_string,
    LEFT(CAST(year_value AS VARCHAR), 2) AS year_cc,
    RIGHT(CAST(year_value AS VARCHAR), 2) AS year_yy,
    CAST(year_start AS DATE) AS year_start,
    CAST(year_end AS DATE) AS year_end
FROM (
    SELECT
        d.year AS year_value,
        MIN(d.date) AS year_start,
        MAX(d.date) AS year_end,
        COUNT(*) AS days_in_year
    FROM dates AS d
    GROUP BY year_value
) AS c
