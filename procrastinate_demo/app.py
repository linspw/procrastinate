from typing import Type

import procrastinate

USE_ASYNC = True


import_paths = ["procrastinate_demo.tasks"]

connector_class: Type[procrastinate.BaseConnector]
if USE_ASYNC:
    connector_class = procrastinate.AiopgConnector
else:
    connector_class = procrastinate.Psycopg2Connector

app = procrastinate.App(connector=connector_class(), import_paths=import_paths)
app.open()
