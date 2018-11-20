from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
msg = MIMEMultipart()
msg['From'] = "ajajay271@gmail.com"
msg['To'] = "ajajaykmr@gmail.com"
msg['Subject'] = "TestMail"

body = "<a href=""https://www.google.com/""> click to show google </a>"
msg.attach(MIMEText(body,'html'))
print(msg)
password = "Ajay@271"
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(msg['From'], password)
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()