import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Function to send a verification email
def send_verification_email(email, verification_link):
    # Replace with your email sending code using smtplib or an email library
    smtp_server = 'your_smtp_server'
    smtp_port = 587
    smtp_username = 'your_username'
    smtp_password = 'your_password'
    sender_email = 'your_sender_email'

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = email
    message['Subject'] = 'Verify your registration'

    body = f'Click the following link to verify your registration: {verification_link}'
    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, email, message.as_string())
        server.quit()
    except Exception as e:
        print(f"Failed to send email: {str(e)}")