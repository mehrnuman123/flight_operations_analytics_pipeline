import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col

spark = (
    SparkSession.builder
    .appName("FlightWeatherPipeline")
    .master("local[*]")
    .getOrCreate()
)

df = spark.read.parquet("data/processed/")



# data qulity checks
rows_count=df.count()
print("row_count", rows_count)
columns_count=df.columns
print("cols count", columns_count)
duplicated_count=df.drop_duplicates().count()
print("duplicates count", duplicated_count)
null_count_in_each_columns= {c: df.filter(col(c).isNull()).count() for c in df.columns}
print("null count each col", null_count_in_each_columns)

df.printSchema()


# business rule just for understanding -----------

print("arrival_delay less than -200 :", df.filter(col("arrival_delay") < -200).count())

print("hourlyvisibility_x less than 0 :",df.filter(col("hourlyvisibility_x") < 0).count())

print("hourlywindspeed_x less than 0 :",df.filter(col("hourlywindspeed_x") < 0).count())



# data cleaning

df = df.dropDuplicates()

df = df.filter(
    col("carrier_code").isNotNull()
)
df = df.filter(
    col("flight_number").isNotNull()
)

# fillna replaces null values with default values, i:e 0
df = df.fillna({
    "delay_weather": 0,
    "delay_carrier": 0
})




# create useful columns

df = df.withColumn(
    "delay_category",
    when(col("arrival_delay") > 15, "delayed").otherwise("on_time")
)

df = df.withColumn(
    "weather_risk",
    when(col("hourlywindspeed_x") > 20, "high_wind")
    .when(col("hourlyvisibility_x") < 5, "low_visibility")
    .otherwise("normal")
)

df.write.mode("overwrite").parquet("data/curated/flight_weather_curated/")



spark.stop()
