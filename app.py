from es_ops import get_jobs,
from crontab import Cron

cron = Cron(user=True)

def add_job_to_cron(job):


def checker():
    for item in cron:
        