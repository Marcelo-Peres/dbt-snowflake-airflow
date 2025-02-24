from datetime import datetime
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator

default_args = {
    "owner": "Marcelo Peres",
    "depends_on_past": False,
}

with DAG(
    dag_id="dbt-snowflake-process",
    default_args=default_args,
    start_date=datetime(2024, 10, 31), 
    schedule_interval="@hourly",
    catchup=False,
    tags=["dbt", "snowflake"],
) as dag:

    run_intermediate = DockerOperator(
        task_id="run_intermediate",
        image="dbt-snowflake", 
        container_name="intermediate",
        api_version="auto",
        auto_remove=True,
        command="dbt run --models intermediate --profiles-dir .", 
        docker_url="tcp://docker-proxy:2375",
        network_mode="airflow_default",
        mount_tmp_dir=False,
    )
    
    run_marts = DockerOperator(
        task_id="run_marts",
        image="dbt-snowflake",
        container_name="marts",  
        api_version="auto",
        auto_remove=True,
        command="dbt run --models marts --profiles-dir .",  
        docker_url="tcp://docker-proxy:2375",
        network_mode="airflow_default",
        mount_tmp_dir=False, 
    )

    run_intermediate >> run_marts
