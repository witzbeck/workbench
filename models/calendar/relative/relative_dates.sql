SELECT
    d.id,
    d.date,
    d.year,
    d.quarter,
    d.month,
    d.week,
    d.dayofyear,
    d.dayofmonth,
    d.dayofweek,
    dw.isweekend,
    dw.isweekday,
    d.isodayofweek,
    d.isoyear,
    y.year_start,
    y.year_end,
    q.quarter_start,
    q.quarter_end,
    m.month_start,
    m.month_end,
    w.week_start,
    w.week_end,
    CASE
        WHEN today.date > y.year_end THEN 1 ELSE 0
    END AS year_completed,
    DATEDIFF('YEAR', today.date, d.date) AS year_offset,
    CASE
        WHEN today.date > q.quarter_end THEN 1 ELSE 0
    END AS quarter_completed,
    DATEDIFF('QUARTER', today.date, d.date) AS quarter_offset,
    CASE
        WHEN today.date > m.month_end THEN 1 ELSE 0
    END AS month_completed,
    DATEDIFF('MONTH', today.date, d.date) AS month_offset,
    CASE
        WHEN today.date > w.week_end THEN 1 ELSE 0
    END AS week_completed,
    DATEDIFF('WEEK', today.date, d.date) AS week_offset,
    DATEDIFF('DAY', today.date, d.date) AS day_offset,
    CASE
        WHEN d.date = today.date THEN 1 ELSE 0
    END AS is_now,
    CASE
        WHEN d.date < today.date THEN 1 ELSE 0
    END AS is_past,
    CASE
        WHEN d.date > today.date THEN 1 ELSE 0
    END AS is_future
FROM {{ ref('dates') }} AS d
INNER JOIN (
    SELECT * FROM {{ ref('dates') }}
    WHERE {{ ref('dates') }}.date = CURRENT_DATE
) AS today
    ON 1 = 1
INNER JOIN {{ ref('years') }} AS y ON d.year = y.year
INNER JOIN {{ ref('quarters') }} AS q
    ON
        y.year = q.year
        AND d.quarter = q.quarter
INNER JOIN {{ ref('months') }} AS m
    ON
        y.year = m.year
        AND d.month = m.month
INNER JOIN {{ ref('weeks') }} AS w
    ON
        y.year = w.year
        AND d.week = w.week
        AND d.date BETWEEN w.week_start AND w.week_end
INNER JOIN {{ ref('dayofweek') }} AS dw ON d.dayofweek = dw.dayofweek
