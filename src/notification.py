import json

import boto3
import arrow
from pydantic import BaseModel

from src.settings import Settings

client = boto3.client("events")


class MessageSender(BaseModel):
    user_id: str

    def send(self, csv_record):
        payload = {"source": "solver",
                   "type": "progress",
                   "userId": self.user_id,
                   "timestamp": arrow.utcnow().format(Settings.datetime_format),
                   "data": csv_record }
        message = {"userId": self.user_id, "payload": payload}
        try:
            response = client.put_events(Entries=[
                {'Source': 'simcloud.solver', 'DetailType': 'Simcloud::Websocket',
                 'Detail': json.dumps(message),
                 'EventBusName': Settings.simcloud_event_bridge}, ])
            print(f"Notification sent: {response}")
        except Exception as e:
            print(f"Notification failed: {e}")