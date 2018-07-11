from es_ops import get_sources_for_region
from crontab import CronTab
from pathlib import Path
import os

directory = Path(__file__).parent.parent.resolve() #pylint: disable=no-member
if "VIRTUAL_ENV" in os.environ:
    pybin = directory / "bin" / "python"
else:
    pybin = "/usr/bin/python"

cron = CronTab(user=True)

def add_job_to_cron(obj):
    schedule,cmd,id = obj["schedule"],obj["cmd"],obj["id"]
    command = f"{cmd} | {pybin} {directory}/processor.py {id}"
    j = cron.new(command=command,comment=id)
    j.setall(schedule)

def checker(region):
    src = get_sources_for_region(region)
    for item in src:
        if len(list(cron.find_comment(item["id"]))) == 0:
            add_job_to_cron(item)
    src_id = [item["id"] for item in src]
    for item in cron:
        if item.comment not in src_id:
            cron.remove(item)
    cron.write()


if __name__ == "__main__":
    checker("bluesteel")
