#  Copyright 2019 CJWW Development
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from iotenvmonitoring.scheduler.apscheduler import APScheduler
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()


def printer():
    print("I'm printed every second!")

def printer_two():
    print("I'm printed every 5 seconds!")


scheduler.add_job(printer, 'interval', id='printer', seconds=1)
scheduler.add_job(printer_two, 'interval', id='printer_two', seconds=5)
def run():
    scheduler.start()
