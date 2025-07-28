{% test expect_consecutive_dates(model, column_name) %}

with dates as (
    select
        {{ column_name }} as date_col,
        lag({{ column_name }}) over (order by {{ column_name }}) as prev_date
    from {{ model }}
)

select *
from dates
where date_col != prev_date + interval '1 day' and prev_date is not null

{% endtest %}

{% test expect_no_gaps_in_dates(model, column_name) %}

select *
from (
    select
        {{ column_name }},
        lead({{ column_name }}) over (order by {{ column_name }}) as next_date
    from {{ model }}
) sub
where next_date != {{ column_name }} + interval '1 day'

{% endtest %}

{% test expect_row_count(model, expected) %}

select *
from (select count(*) as row_count from {{ model }}) sub
where row_count != {{ expected }}

{% endtest %}

{% test expect_row_count_between(model, min, max) %}

select *
from (select count(*) as row_count from {{ model }}) sub
where row_count < {{ min }} or row_count > {{ max }}

{% endtest %}

-- Add more custom tests as needed, e.g., for offsets in relative models
