from flask_apscheduler import APScheduler
from flask import jsonify

class StatsManager():
    def __init__(self):
        self.success_last_minute = 0
        self.success_last_hour = 0
        self.success_last_day = 0
        self.failed_last_minute = 0
        self.failed_last_hour = 0
        self.failed_last_day = 0
        self.scheduler = APScheduler()

    def start_jobs(self):
        self.scheduler.add_job(func=self.clear_minute, trigger='interval', id='minute', seconds=60)
        self.scheduler.add_job(func=self.clear_hour, trigger='interval', id='hour', seconds=60*60)
        self.scheduler.add_job(func=self.clear_day, trigger='interval', id='day', seconds=60*60*24)
        self.scheduler.start()

    def add(self, success):
        if success:
            self.success_last_minute += 1
            self.success_last_hour += 1
            self.success_last_day += 1
        else:
            self.failed_last_minute += 1
            self.failed_last_hour += 1
            self.failed_last_day += 1


    def clear_minute(self):
        self.success_last_minute = 0
        self.failed_last_minute = 0

    def clear_hour(self):
        self.success_last_hour = 0
        self.failed_last_hour = 0

    def clear_day(self):
        self.success_last_day = 0
        self.failed_last_day = 0

    def get(self):
        return jsonify({
                "success_minute": self.success_last_minute,
                "success_hour": self.success_last_hour,
                "success_day": self.success_last_day,
                "failed_minute": self.failed_last_minute,
                "failed_hour": self.failed_last_hour,
                "failed_day": self.failed_last_day,
            })
