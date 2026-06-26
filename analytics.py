from db_connection import cursor, conn


# total on time flights for each origin airport

cursor.execute("""
    select da.airport_code, ff.delay_category, count(*) as total_on_time
    from fact_flights ff
    inner join dim_airport da
    on  ff.origin_airport_id = da.airport_id
    where ff.delay_category = 'on_time'
    group by da.airport_code,ff.delay_category
    order by total_on_time desc
      
    
               """)
rows=cursor.fetchall()
print(rows)

for row in rows:
    print(row)