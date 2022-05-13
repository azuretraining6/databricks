# Databricks notebook source
import requests, json, datetime
from datetime import date
from datetime import timedelta
import os
host_url = 'https://adb-4784284663471480.0.azuredatabricks.net/api/2.0/preview/permissions/jobs/286007879330485'

payload = {"access_control_list": [{"user_name": "newuser@ngkazureclass.xyz","permission_level": "CAN_VIEW"}]}


headers = {"Authorization" : "Bearer " + os.environ['DATABRICKS_TOKEN']}
api_get = requests.patch(host_url, headers=headers, json={"access_control_list": [{"user_name": "newuser@ngkazureclass.xyz","permission_level": "CAN_VIEW"}]}).text

print((api_get))



# COMMAND ----------

import requests
import json
import os

instance_id = 'adb-4784284663471480.0.azuredatabricks.net'

api_version = '/api/2.0'
api_command = '/preview/scim/v2/Users'
url = f"https://{instance_id}{api_version}{api_command}"
api_get = requests.get(url).text
print(api_get)

# COMMAND ----------

host_url = 'https://adb-4784284663471480.0.azuredatabricks.net/api/2.0/preview/scim/v2/Users'
import requests, json, datetime
from datetime import date
from datetime import timedelta
import os


#Uses Python Request Library to access Databricks API
#Initializes variables for storage and to be passed into logic
#Converts API GET data into iterable JSON

headers = {"Authorization" : "Bearer " + os.environ['DATABRICKS_TOKEN']}
api_get = requests.get(host_url, headers=headers).text
print(api_get)
data = json.loads(api_get)
ids = data['token_infos']

# COMMAND ----------


