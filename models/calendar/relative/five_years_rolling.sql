SELECT *
FROM {{ ref('relative_dates') }} AS d
WHERE d.date BETWEEN CURRENT_DATE - INTERVAL '5 years' AND CURRENT_DATE
