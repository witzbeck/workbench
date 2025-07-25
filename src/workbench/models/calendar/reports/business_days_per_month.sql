SELECT
    d.year,
    d.month,
    COUNT(*) AS n_business_days
FROM dates AS d
LEFT JOIN holidays AS h ON d.date = h.date
WHERE d.dayofweek BETWEEN 1 AND 5 AND h.date IS NULL
GROUP BY d.year, d.month
