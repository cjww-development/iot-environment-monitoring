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

import time
from iotenvmonitoring.aws.sqs.publisher import SQSPublisher
from iotenvmonitoring.sensors.dht_11 import DHT11
from iotenvmonitoring.models.env_data import EnvData
from iotenvmonitoring.logging.logger import Logger
from iotenvmonitoring.config.config_loader import ConfigLoader


class App:
    def __init__(self):
        conf = ConfigLoader().conf
        self.logger = Logger().logger
        self.publisher = SQSPublisher("env-data")
        self.sensor = DHT11("dht11")
        self.wait_time = conf['app.wait-time']

    def run(self):
        while True:
            hum, temp = self.sensor.attempt_read()
            if hum is not None and temp is not None:
                self.logger.info("[App] - [run] - Capture environment data, building message")
                msg = EnvData(temperature=temp, humidity=hum).to_json_msg()
                self.publisher.send_message(msg)
            else:
                self.logger.warn("[App] - [run] - No readings at the moment; trying again later")
            time.sleep(self.wait_time)
