from apscheduler.schedulers.blocking import BlockingScheduler
from fantasy.tasks import update_fpl

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    update_fpl()

sched.start()