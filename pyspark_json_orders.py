# Initialize Spark session
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, col

spark = SparkSession.builder.appName('Spark Playground').getOrCreate()

#enter the file path here
file_path = "/datasets/orders.json"

#read the file
df = spark.read.format('json').option('multiline','true').load(file_path)

df_exploded = df.withColumn("products", explode(col("products"))).select("customer_id", "order_id", "products.product_name", "products.product_price")

# Display the final DataFrame using the display() function.
display(df_exploded)
