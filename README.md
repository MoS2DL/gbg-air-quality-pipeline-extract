# Gothenburg Air Quality Data Pipeline | Extraction

This repository contains a simple example of the extraction step in an ELT/ETL pipeline using the workflow manager [Apache Airflow](https://airflow.apache.org/).

The data extracted is from an API (see Links below) giving access to data related to air quality measurements in Gothenburg, Sweden, and is provided by Gothenburg Municipality for public use.
The data is accessible by date, with hourly resolution for that date, from four fixed stations/locations (Femman, Lejonet, Haga Norra and Haga Södra) as well as three mobile stations.
Note that all stations do not provide the same set of measurements.
The earliest date currently accessible using the API is 2021-01-01.
Data before this date can be accessed as an csv-file, available through the links below.

Upon succesfull execution the Airflow instance will back-fill data from 2021-01-01 up until the day before the execution date into the `data/raw` directory structure.
If Airflow is left running the dag is scheduled to trigger midst night according to the cron-interval `0 3 * * *`, and will automatically back-fill the previous day.

Please note that this Airflow setup is only suitable for local testing and orchestation of non-critical pipelines and **should not** be used for production when the availability of pipeline results are of critical importance.

The repository has been developed in a Linux environment.
With that said, it should work out of the box on a Mac and possibly in windows using WSL2.

<hr>

## Setup

1. Run the bootstrap script `bootstrap-airflow.sh` to create necessary directories and environment file with en environmental variable setting an Airflow user ID.
2. Run the command `docker-compose up airflow-init`
3. After initialization, Airflow can be started using the command `docker-compose up`.
4. The gui-interface can then be accessed by a browser through `localhost:8080`.
5. Default login credentials are user: `airflow` with the password: `airflow`.
6. The dag `gbg_air_quality_request_to_disc` can then be activated and will start back-filling data.

<hr>

## Links
[Gothenburg Open Data (In Swedish)](https://goteborg.se/wps/portal/start/kommun-o-politik/kommunfakta/oppna-data)


[Page for Air Quality Data API (In Swedish)](https://goteborg.se/wps/portal/start/kommun-o-politik/kommunfakta/oppna-data/oppna-data-soksida/oppna-data-datamangd#esc_entry=690&esc_context=6)

[API endpoint](https://catalog.goteborg.se/rowstore/dataset/12e75096-583d-4c0b-afac-093e90d8489e)
