from datetime import datetime


class Email:
    sender: str
    receiver: str
    subject: str
    body: str
    timeStamp = datetime

    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.timeStamp = datetime.now()

    def getSender(self):
        return self.sender

    def getReceiver(self):
        return self.receiver

    def getSubject(self):
        return self.subject

    def getBody(self):
        return self.body

    def getTimeStamp(self):
        return self.timeStamp
