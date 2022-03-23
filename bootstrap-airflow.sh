#!/usr/bin/env bash

mkdir -p ./dags ./logs ./plugins ./data/raw
echo -e "AIRFLOW_UID=$(id -u)" > .env
