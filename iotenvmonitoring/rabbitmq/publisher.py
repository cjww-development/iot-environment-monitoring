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

import pika
from iotenvmonitoring.config.config_loader import ConfigLoader


class Publisher:
    def __init__(self, publisher_name):
        self.publisher_name = publisher_name
        self.conf = ConfigLoader().conf
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(self.conf[f'rabbitmq.publishers.{publisher_name}.host']))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.conf[f'rabbitmq.publishers.{publisher_name}.queue'])

    def basic_publish(self, msg):
        self.channel.basic_publish(
            exchange='',
            routing_key=self.conf[f'rabbitmq.publishers.{self.publisher_name}.queue'],
            body=msg
        )

    def close_connection(self):
        self.connection.close()
