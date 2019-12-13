# importing required modules
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

try:
    # create template for html
    template = Template(Path("template.html").read_text())

    message = MIMEMultipart()

    sender_name = input("Please enter name of the sender:  ")
    message["from"] = sender_name

    # Receiver and message details
    receiver_email_id = input("Please enter the receiver email id:  ")
    message["to"] = receiver_email_id

    # Subject of the email
    message_subject = input("Please enter the subject of the email:  ")
    message["subject"] = message_subject

    # Reciever name
    enter_name = input("Please enter name of the email receiver  ")
    body = template.substitute({"name": enter_name})

    # Attaching html and image files
    message.attach(MIMEText(body, "html"))
    message.attach(MIMEImage(Path("image.png").read_bytes()))

    # Connecting and sending gmail using smtp protocol
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        sender_email = input("Please enter sender email id:  ")
        sender_password = input("Please enter sender email password:  ")
        smtp.login(sender_email, sender_password)
        smtp.send_message(message)
        print("sent...")
except:
    print("You did not enter correct details")
    print("Please enter details once again")

# Fellow following step, if you face problem with SMTPAuthenticationWError
# Go to admin.google.com
# From the admin console, select “Security”
# Select “Basic settings”
# Scroll down to “Less secure apps”
# Go to settings for less secure apps ››
# Check the radio button “Allow users to manage their access to less secure apps”
# Save the changes
# Open this link being sign in as the super administrator https://www.google.com/settings/security/lesssecureapps
# Check the radio button Turn On the access for less secure apps
# Unlock Captcha using this link https://accounts.google.com/DisplayUnlockCaptcha