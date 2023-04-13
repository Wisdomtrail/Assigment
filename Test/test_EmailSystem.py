from unittest import TestCase

from EmailApp.EmailSystem import EmailSystem
from EmailApp.User import User


class TestEmailSystem(TestCase):
    email_system = EmailSystem()
    sunday = User("sunday", "sunepa@gmail.com")
    alice = User("Alice", "alice@gmail.com")
    email_system.addUser(sunday)

    def test_add_user(self):
        self.assertEqual(1, self.email_system.countUser())

    def test_get_user_by_email(self):
        self.assertEqual(self.sunday, self.email_system.getUserByEmail("sunepa@gmail.com"))

    def test_send_email(self):
        self.email_system.sendEmail(self.sunday.getEmail(), self.alice.getEmail(), "babe", "i love you")
        inbox = self.alice.getInbox()
        self.assertEqual("babe i love you", inbox)
