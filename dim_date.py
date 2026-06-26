from db_connection import cursor, conn

create_dim_date="""
create table if not exists dim_date(
    date_id SERIAL PRIMARY KEY,
    full_date DATE UNIQUE NOT NULL,
    year INT,
    month INT,
    day INT,
    weekday INT
)
"""

truncate=""" truncate table dim_date restart identity """


get_and_insert_data="""
INSERT INTO dim_date (
    full_date,
    year,
    month,
    day,
    weekday
)
SELECT DISTINCT
    TO_DATE(date, 'YYYY-MM-DD'),
    year,
    month,
    day,
    weekday
from stg_flight_weather
where date is not null
"""

cursor.execute(create_dim_date)
cursor.execute(truncate)
cursor.execute(get_and_insert_data)
conn.commit()

cursor.execute(""" select * from dim_date""")
days=cursor.fetchall()
for day in days:
    print(day)