# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.2.4
#   kernelspec:
#     display_name: Python [conda env:python37base]
#     language: python
#     name: conda-env-python37base-py
# ---

from google.cloud import bigquery
from google.cloud import storage
import pandas as pd
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="code/cred.json"
client = bigquery.Client(project="trkit00")

# +
#parameter
minDate = "2020-04-01"
if 'mindate' in os.environ.keys():
  minDate = os.environ["mindate"]

dataset = "BGN5EL24"

# -

sql = """
SELECT date, COUNT(*) hits
FROM (
SELECT DATE(EventTime) date 
FROM `%s`
WHERE DATE(EventTime) > "%s"
)
GROUP BY date 
ORDER BY date ASC
"""%("trkit00."+dataset+".events", minDate)


df=client.query(sql).to_dataframe()
Output = ""
for i,r in df.iterrows():
    Output += "%s\t%s\n"%(r["date"], r["hits"])

storageClient = storage.Client()
bucket = storageClient.get_bucket('datataskiodemo')
fileName = "ExtractDemo-from-"+minDate+".txt"
blob = bucket.blob(fileName)
blob.upload_from_string(Output)


