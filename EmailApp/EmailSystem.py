from EmailApp.Email import Email
from EmailApp.User import User


class EmailSystem:
    Users = []
    count = 0

    def __init__(self):
        self.users = []

    def addUser(self, user: User):
        self.users.append(user)
        self.count += 1

    def countUser(self):
        return self.count

    def getUserByEmail(self, email):
        for user in self.users:
            if user.getEmail() == email:
                return user

        return None

    def sendEmail(self, sender, receiver, subject, body):
        recipient = self.getUserByEmail(receiver)
        if recipient is not None:
            email = Email(sender, receiver, subject, body)
            recipient.receiveMail(email)