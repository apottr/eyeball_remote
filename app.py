from es_ops import get_sources_for_region
from crontab import CronTab

cron = CronTab(user=True)

def add_job_to_cron(job):
    pass

def checker(region):
    for item in get_sources_for_region(region):
        if len(list(cron.find_command(item["cmd"]))) == 0:
            print(item)
            

if __name__ == "__main__":
    print(get_sources_for_region("bluesteel"))
