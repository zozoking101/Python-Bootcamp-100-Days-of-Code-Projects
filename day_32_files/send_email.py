from email.message import EmailMessage
import smtplib
import ssl


my_email = "zoe.oladokun@gmail.com"
recipient = "zoe.oladokun@stu.cu.edu.ng"

with open("password.txt") as f:
    password = f.read()

subject = "Email sent using python"
body = """
Hello from myself!
"""

email_message = EmailMessage()

email_message["From"] = my_email
email_message["To"] = recipient
email_message["Subject"] = subject
email_message.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 587, context=context) as connection:
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=recipient, msg=email_message.as_string())
    connection.quit()
