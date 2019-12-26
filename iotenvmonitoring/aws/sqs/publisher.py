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

import boto3
from iotenvmonitoring.logging.logger import Logger
from iotenvmonitoring.config.config_loader import ConfigLoader


class SQSPublisher:
    def __init__(self, queue):
        self.logger = Logger().logger
        self.conf = ConfigLoader().conf
        self.confName = queue
        self.queue = self.conf[f'aws.sqs.{queue}.name']
        self.client = boto3.client(
            'sqs',
            region_name=self.conf[f'aws.sqs.{queue}.region'],
            use_ssl=self.conf[f'aws.sqs.{queue}.ssl'],
            endpoint_url=self.conf[f'aws.sqs.{queue}.endpoint-url']
        )

    def send_message(self, msg):
        resp = self.client.send_message(
            QueueUrl=self.conf[f'aws.sqs.{self.confName}.queue-url'],
            MessageBody=msg
        )
        self.logger.info(f'[SQSPublisher] - [send_message] - Published message to sqs at {self.queue} with messageId {resp["MessageId"]}')
        return resp
