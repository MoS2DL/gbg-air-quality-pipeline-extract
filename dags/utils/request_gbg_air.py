import datetime as dt
import json
from pathlib import Path
import requests


def query_and_save_results_to_disc(date: str, url: str, data_root: Path) -> None:
    """Query API and write response data to disc

    Creates a date-structured directory tree and saves response
    into JSON-file split by the hour

    The raw data points in the responses are written to disc, with the exeptions:
    1. Each data point in the responses are cleaned from padded white-spaces.
    2. The UTC-timestamp, at time of saving to disc, is included to each record
       for traceability.

    Parameters
    ----------
    date : str
      The requested date for the data using the form "YYYY-MM-DD".
    url : str
      URL to the Gothenburg Open Data endpoint.
    data_root : Path
      Python Path object containing the path to where the files will be saved

    """
    # GET request to the API endpoint
    response = requests.get(url, params={"date": date})
    assert response.status_code == 200
    # Extract the results from the response
    results = response.json()["results"]
    assert len(results) > 0 and len(results) <= 24

    # Split date string to be used in directory structure
    year, month, day = [
        val.lstrip("0") for val in date.split("-")
    ]  # Remove leading zeros using lstrip
    data_path = data_root / year / month / day
    data_path.mkdir(parents=True, exist_ok=True)

    save_time = f"{dt.datetime.now()}"
    n_values = 0
    for n, result in enumerate(results):
        result = {
            key: value.strip()
            for key, value in sorted(result.items(), key=lambda x: x[0])
        }  # Sort by the keys and remove padding white-spaces
        n_values += len(result)
        result["time_saved"] = save_time  # Add UTC-timestamp to the data
        result["data_origin"] = "gbg-air-quality-api"
        file_path = data_path / f"{n}.json"  # Enumerate digit defines file-name
        with open(file_path, "w") as json_file:
            json.dump(result, json_file)
    print(f"#records: {n+1}, #values: {n_values}")
