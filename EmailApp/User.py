from EmailApp.Email import Email


class User:
    name: str
    email: str
    inbox = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.inbox = []

    def getName(self):
        return self.name

    def getEmail(self):
        return self.email

    def receiveMail(self, email: Email):
        self.inbox.append(email)

    def getInbox(self):
        return self.inbox