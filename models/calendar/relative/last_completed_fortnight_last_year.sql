WITH F AS (
    SELECT *
    FROM {{ ref('relative_dates') }}
    WHERE
        WEEK_OFFSET BETWEEN -2 AND -1
        AND WEEK_COMPLETED = 1
)

SELECT C.*
FROM {{ ref('relative_dates') }} AS C
INNER JOIN F ON
    C.WEEKOFYEAR = F.WEEKOFYEAR
    AND C.DAYOFWEEK = F.DAYOFWEEK
    AND YEAR(F.DATE) - 1 = C.YEAR
