from pyspark.sql import SparkSession
import os


db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

spark = (
    SparkSession.builder
    .appName("LoadCuratedToPostgres")
    .master("local[*]")
    .config("spark.jars.packages", "org.postgresql:postgresql:42.7.3")
    .getOrCreate()
)

jdbc_url = f"jdbc:postgresql://{db_host}:{db_port}/{db_name}"

properties = {
    "user": db_user,
    "password": db_password,
    "driver": "org.postgresql.Driver"
}

print("JDBC URL:", jdbc_url)

# 1. Test DB connection
test_df = spark.read.jdbc(
    url=jdbc_url,
    table="(SELECT 1 AS test) t",
    properties=properties
)

test_df.show()




# 2. Read curated parquet
df = spark.read.parquet("data/curated/flight_weather_curated/")

print("Curated rows:", df.count())
df.printSchema()

# 3. Test write small data first
df.limit(10).write.jdbc(
    url=jdbc_url,
    table="spark_test",
    mode="overwrite",
    properties=properties
)

print("Test write completed: spark_test")

# 4. Write full curated data to staging table
df.write.jdbc(
    url=jdbc_url,
    table="stg_flight_weather",
    mode="overwrite",
    properties=properties
)

print("Full load completed: stg_flight_weather")



spark.stop()