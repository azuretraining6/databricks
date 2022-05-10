# Databricks notebook source
# MAGIC %sh
# MAGIC date

# COMMAND ----------

# MAGIC %sh
# MAGIC curl -X GET --header "Authorization: Bearer $DATABRICKS_TOKEN" \
# MAGIC https://adb-4784284663471480.0.azuredatabricks.net/api/2.0/secrets/scopes/list

# COMMAND ----------

# MAGIC %sh
# MAGIC databricks secrets list-scopes --output JSON

# COMMAND ----------

dbutils.fs.mount(
source = "wasbs://databrickssecret@devopsdemongk.blob.core.windows.net",
mount_point = "/mnt/mymount",
extra_configs = {"fs.azure.account.key.devopsdemongk.blob.core.windows.net":dbutils.secrets.get(scope = "blobfileread", key = "blobread")})


# COMMAND ----------

df = spark.read.text("/mnt/mymount/sample.txt")
df.show()

# COMMAND ----------


