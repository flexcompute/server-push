from unittest import TestCase

from src.notification import MessageSender


class TestMessage(TestCase):
    def test_send(self):
        MessageSender(user_id="AIDAU77I6BZ25DGMJ633P", task_id="1234").send(csv_record="98%")
