import json
import os
import sendgrid
from langchain_core.tools import Tool, StructuredTool
from sendgrid import Email, Content, To, Mail

sendGridApiKey = os.getenv("EMAIL_API_KEY")

def sendHtmlEmail(subject: str, body: str):
    print("sending html mail")
    sg = sendgrid.SendGridAPIClient(sendGridApiKey)
    from_email = Email("tech@absolutefoods.in")
    to_email = To("vijayarya326@gmail.com")
    subject = f"Mail from SideKick {subject}"
    content = Content("text/html", body)
    mail = Mail(from_email, to_email, subject, content)
    print("calling too")
    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()
    # Send an HTTP POST request to /mail/send
    response = sg.client.mail.send.post(request_body=mail_json)
    if response.status_code > 200:
        return "Mail sent successfully"
    else :
        return "Mailing failed"


sendHtmlEmailTool = StructuredTool.from_function(
    name="sendHtmlEmail",
    func=sendHtmlEmail,
    description="Useful for sending html email"
)
