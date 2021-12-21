# Databricks notebook source
# MAGIC %pip install 2to3

# COMMAND ----------

# MAGIC %sh 2to3 -w bs4

# COMMAND ----------

import datetime

before = datetime.datetime.now()
import bs4
print(datetime.datetime.now() - before)

# COMMAND ----------


