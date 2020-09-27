import smtplib
import os
from email.message import EmailMessage

# GLOBAL CONSTANTS

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')


class send_Email():
    def __init__(self):
        self.send_it()
        pass
    def send_it(self):
        self.msg = EmailMessage()
        self.msg['Subject'] = "Job Vacancy Scrape"
        self.msg['From'] = EMAIL_ADDRESS
        self.msg['To'] = 'aosborne99@outlook.com'
        self.msg.set_content('Check the attachment to see the new job vacancies')
        self.msg.add_attachment(open("JuniorDevOpsJobs.csv", "r").read())

    # creates SMTP session 
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(self.msg)



