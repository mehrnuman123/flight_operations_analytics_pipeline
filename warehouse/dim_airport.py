from db_connection import cursor, conn

create_dim_airport_query="""
create table if not exists dim_airport(
    airport_id SERIAL PRIMARY KEY,
    airport_code VARCHAR(10) UNIQUE NOT NULL
)
"""

truncate="""
truncate table dim_airport restart identity
"""

filter_and_insert="""
insert into dim_airport (airport_code)
select distinct origin_airport as airport_code
from stg_flight_weather
where origin_airport is not null

union

select distinct destination_airport as airport_code
from stg_flight_weather
where destination_airport is not null

"""



#cursor.execute(create_dim_airport_query)
#cursor.execute(truncate)
#cursor.execute(filter_and_insert)
#conn.commit()

cursor.execute(""" select * from dim_airport """)
rows=cursor.fetchall()
for row in rows:
    print(row)
