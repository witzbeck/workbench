WITH y AS (
    SELECT *
    FROM relative_dates
    WHERE
        year_offset = 0
        AND is_past = 1
)

SELECT * FROM relative_dates AS v
INNER JOIN y ON
    y.year - 1 = v.year
    AND v.dayofyear = y.dayofyear
