from pathlib import Path
import datetime as dt


START_DATE = dt.datetime(2021, 1, 1)

# Endpoint URL
URL = (
    "https://catalog.goteborg.se/rowstore/dataset/12e75096-583d-4c0b-afac-093e90d8489e"
)

DATA_ROOT_PATH = Path("/tmp/data/raw")

default_args = {
    "depends_on_past": False,
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": dt.timedelta(minutes=5),
}
