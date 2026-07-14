from db_connection import conn, cursor

create_dim_carrier = """
CREATE TABLE IF NOT EXISTS dim_carrier (
    carrier_id SERIAL PRIMARY KEY,
    carrier_code VARCHAR(10) UNIQUE NOT NULL
);
"""

truncate = """
TRUNCATE TABLE dim_carrier RESTART IDENTITY;
"""

insert_dim_carrier = """
INSERT INTO dim_carrier (carrier_code)
SELECT DISTINCT carrier_code
FROM stg_flight_weather
WHERE carrier_code IS NOT NULL;
"""

cursor.execute(create_dim_carrier)
cursor.execute(truncate)
cursor.execute(insert_dim_carrier)
conn.commit()

cursor.execute("SELECT * FROM dim_carrier;")
data = cursor.fetchall()

for row in data:
    print(row)