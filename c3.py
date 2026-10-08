from airflow.sdk import dag, task
from airflow.providers.standard.operators.bash import BashOperator


@dag(dag_id="etl_operators_demo")
def midterm_dag():

    @task.python
    def start():
        return "Pipline started."

    @task.bash
    def download():
        return "echo Downloading file..."

    @task.bash
    def process():
        return "echo Processing file..."

    bash_oldstyle = BashOperator(
        task_id="process",
        bash_command="echo Processing file...",
    )

    @task.python
    def finish():
        return "Pipline finished."

    @task.python
    def new():
        return "what changed."

    start() >> download() >> bash_oldstyle >> finish() >> new()


midterm_dag()

# when we created the initaial dag it assigned a version to the file. After its run when we made changes to file and re run it
# Airflow changes the version number to something like ver1 -> ver2
