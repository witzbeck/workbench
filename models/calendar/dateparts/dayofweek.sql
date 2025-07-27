SELECT
    d.dayofweek,
    dayname(d.date) AS dayname,
    coalesce(d.dayofweek IN (0, 6), FALSE) AS isweekend,
    NOT coalesce(d.dayofweek IN (0, 6), FALSE) AS isweekday
FROM {{ ref('dates') }} AS d
GROUP BY d.dayofweek, dayname(d.date)
