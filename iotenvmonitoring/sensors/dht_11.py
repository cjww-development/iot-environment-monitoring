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

import Adafruit_DHT
import random


class DHT11:
    def __init__(self, pin, test_mode):
        self.pin = pin
        self.test_mode = test_mode
        self.sensor = Adafruit_DHT.DHT11

    def attempt_read(self):
        if self.test_mode:
            return "{0:.2f}".format(random.random()), "{0:.2f}".format(random.uniform(0, 100))
        else:
            return Adafruit_DHT.read(self.sensor, self.pin)
