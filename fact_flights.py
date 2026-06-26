from db_connection import cursor, conn


drop_fact_flights="""drop table fact_flights"""
cursor.execute(drop_fact_flights)

create_fact_table="""


  CREATE TABLE IF NOT EXISTS fact_flights (
    flight_id SERIAL PRIMARY KEY,
    carrier_id INT,
    origin_airport_id INT,
    destination_airport_id INT,
    date_id INT,

    flight_number BIGINT,
    tail_number TEXT,

    scheduled_elapsed_time BIGINT,
    departure_delay BIGINT,
    arrival_delay BIGINT,

    delay_carrier BIGINT,
    delay_weather BIGINT,
    delay_national_aviation_system BIGINT,
    delay_security BIGINT,
    delay_late_aircarft_arrival BIGINT,

    cancelled_code TEXT,

    origin_temperature DOUBLE PRECISION,
    origin_precipitation DOUBLE PRECISION,
    origin_visibility DOUBLE PRECISION,
    origin_wind_speed DOUBLE PRECISION,

    destination_temperature DOUBLE PRECISION,
    destination_precipitation DOUBLE PRECISION,
    destination_visibility DOUBLE PRECISION,
    destination_wind_speed DOUBLE PRECISION,

    weather_risk TEXT,
    delay_category TEXT
);

"""

truncate="""truncate table fact_flights restart identity"""

get_and_insert_records="""
INSERT INTO fact_flights (
    carrier_id,
    origin_airport_id,
    destination_airport_id,
    date_id,
    flight_number,
    scheduled_elapsed_time,
    departure_delay,
    arrival_delay,
    delay_carrier,
    delay_weather,
    delay_national_aviation_system,
    delay_security,
    delay_late_aircarft_arrival,
    cancelled_code,
    weather_risk,
    delay_category
)
SELECT 
    dc.carrier_id,
    origin.airport_id,
    dest.airport_id,
    dd.date_id,
    stg.flight_number,
    stg.scheduled_elapsed_time,
    stg.departure_delay,
    stg.arrival_delay,
    stg.delay_carrier,
    stg.delay_weather,
    stg.delay_national_aviation_system,
    stg.delay_security,
    stg.delay_late_aircarft_arrival,
    stg.cancelled_code,
    stg.weather_risk,
    stg.delay_category
FROM stg_flight_weather stg
JOIN dim_carrier dc
    ON stg.carrier_code = dc.carrier_code
JOIN dim_airport origin
    ON stg.origin_airport = origin.airport_code
JOIN dim_airport dest
    ON stg.destination_airport = dest.airport_code
JOIN dim_date dd
    ON TO_DATE(stg.date, 'YYYY-MM-DD') = dd.full_date;


"""


cursor.execute(create_fact_table)
cursor.execute(truncate)
cursor.execute(get_and_insert_records)
conn.commit()