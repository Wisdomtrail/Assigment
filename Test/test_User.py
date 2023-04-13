from unittest import TestCase

from EmailApp.Email import Email
from EmailApp.User import User


class TestUser(TestCase):
    user = User("sunday", "sunday@gmail.com")

    def test_get_name(self):

        name = self.user.getName()
        self.assertEqual("sunday", name)

    def test_get_email(self):

        mail = self.user.getEmail()
        self.assertEqual("sunday@gmail.com", mail)

    def test_receive_mail(self):
        email = Email("sunday@gmail.com", "alice@gmail.com", "hello alice", "how are you")
        self.user.receiveMail(email)
        inbox = self.user.getInbox()
        self.assertEqual("hello alice", email.getSubject())
        self.assertEqual(1, inbox.__len__())
        sender = email.getSender()
        self.assertEqual("sunday@gmail.com", sender)
