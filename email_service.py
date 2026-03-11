import smtplib
from config import EMAIL_ADDRESS, EMAIL_PASSWORD

def send_email(receiver, subject, message):

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()

    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    email = f"Subject:{subject}\n\n{message}"

    server.sendmail(EMAIL_ADDRESS, receiver, email)

    server.quit()

    return "Email Sent Successfully"