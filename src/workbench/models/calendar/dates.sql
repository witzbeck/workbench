WITH dates AS (
    SELECT
        UNNEST(GENERATE_SERIES(
            MAKE_DATE(YEAR(CURRENT_DATE) - 5, 1, 1),
            MAKE_DATE(YEAR(CURRENT_DATE) + 1, 12, 31),
            INTERVAL '1 day'
        )) AS date
)
SELECT
    ROW_NUMBER() OVER (ORDER BY date)  AS id,
    CAST(d.date AS DATE)               AS date,
    EXTRACT('YEAR' FROM d.date)        AS year,
    EXTRACT('QUARTER' FROM d.date)     AS quarter,
    EXTRACT('MONTH' FROM d.date)       AS month,
    EXTRACT('WEEK' FROM d.date)        AS week,
    DAYOFYEAR(d.date)                  AS dayofyear,
    DAYOFMONTH(d.date)                 AS dayofmonth,
    DAYOFWEEK(d.date)                  AS dayofweek,
    ISODOW(d.date)                     AS isodayofweek,
    ISOYEAR(d.date)                    AS isoyear,
    YEARWEEK(d.date)                   AS yearweek

    FROM dates AS d