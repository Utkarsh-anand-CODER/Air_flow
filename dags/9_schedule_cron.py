from airflow.sdk import dag,task
from pendulum import datetime
from airflow.timetables.trigger import CronPartitionTimetable
#function within fuction
@dag(
    dag_id="first_schedule_cron_dag",
    start_date=datetime(year=2026,month=10,day=17, tz="Asia/Kolkata"),
    schedule="*/10 * * * *",
    is_paused_upon_creation=False,
    catchup=False,
)
def first_schedule_cron_dag():
    @task.python
    def first_task():
        print("This is the first task")

    @task.python
    def second_task():
        print("This is the second task")

    @task.python
    def third_task():
            print("This is the third task")

    first=first_task()
    second=second_task()
    third=third_task()

    first>>second>>third

first_schedule_cron_dag()
