from datetime import datetime
from unittest import TestCase

from EmailApp.Email import Email


class TestEmail(TestCase):
    email = Email("sunday", "alice", "hello babe", "how are you")

    def test_get_sender(self):
        sender = self.email.getSender()
        self.assertEqual("sunday", sender)

    def test_get_receiver(self):
        receiver = self.email.getReceiver()
        self.assertEqual("alice", receiver)

    def test_get_subject(self):
        subject = self.email.getSubject()
        self.assertEqual("hello babe", subject)

    def test_get_body(self):
        body = self.email.getBody()
        self.assertEqual("how are you", body)

    def test_get_time_stamp(self):
        date = self.email.getTimeStamp()
        self.assertEqual(datetime.now(), date)
