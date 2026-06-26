import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="flight_weather_analytics",
    user="admin",
    password="postgres"
)

cursor=conn.cursor()