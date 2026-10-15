from airflow.sdk import dag,task
from airflow.operators.bash import BashOperator

#function within fuction
@dag(
    dag_id="bash_dag",
)
def bash_dag():
    @task.python
    def first_task():
        print("This is the first task")

    @task.python
    def second_task():
        print("This is the second task")

    @task.bash
    def bash_task():
        return "echo https://airflow.apache.org/"

    run_task_oldschool=BashOperator(
        task_id="run_task_oldschool",
        bash_command="echo https://airflow.apache.org/",
    )

    @task.python
    def version_task():
         print("This is the version task.DAG version 2.0!")

    first=first_task()
    second=second_task()
    bash_modern=bash_task()
    run_task_oldschool=run_task_oldschool
    version=version_task()

    first>>second>>bash_modern>>run_task_oldschool>>version

bash_dag()
