SELECT
    d.year,
    d.weekofyear,
    MIN(d.date) AS first_business_day
FROM {{ ref('dates') }} AS d
INNER JOIN {{ ref('weeks') }} AS w ON d.date BETWEEN w.week_start AND w.week_end
LEFT JOIN {{ source('python_assets', 'holidays') }} AS h ON d.date = h.date
WHERE d.dayofweek BETWEEN 1 AND 5 AND h.date IS NULL
GROUP BY d.year, d.weekofyear
