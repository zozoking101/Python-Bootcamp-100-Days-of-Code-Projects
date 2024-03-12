import smtplib
import getpass

my_email = "evilestminion22@outlook.com"
recipient = "zoe.oladokun@gmail.com"
password = getpass.getpass("Enter password: ")
message = """
Subject: Mail sent using python
Hi Zoe, 

I sent this email to myself from a test account.

Thanks,
Test Account
"""

connection = smtplib.SMTP("smtp.mail.outlook.com", port=587)

status_code, response = connection.ehlo()
print(f"[*] Echoing the server: {status_code}: {response}")

status_code, response = connection.starttls()
print(f"[*] Starting TLS connection: {status_code}: {response}")

status_code, response = connection.login(my_email, password)
print(f"[*] Logging in: {status_code}: {response}")

connection.sendmail(from_addr=my_email, to_addrs=recipient, msg=message)

connection.quit()
