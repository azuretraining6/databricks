# Databricks notebook source
job_id="363021292832768"
host_url = 'https://adb-4784284663471480.0.azuredatabricks.net/api/2.0/preview/permissions/jobs/' + job_id
user_name="newuser@ngkazureclass.xyz"

# COMMAND ----------

import requests
import os
payload = {"access_control_list": [{"user_name": user_name,"permission_level": "CAN_VIEW"}]}
headers = {"Authorization" : "Bearer " + os.environ['DATABRICKS_TOKEN']}
api_get = requests.patch(host_url, headers=headers, json=payload).text

print((api_get))



# COMMAND ----------


