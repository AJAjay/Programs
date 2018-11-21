from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
# construct the message in particular format
msg = MIMEMultipart()
msg['From'] = "from --> mail id"
msg['To'] = "to --> mail id"
msg['Subject'] = "subject of the mail"

body = "<a href=""https://www.google.com/""> click to show google </a> "
#attach the body of the message with specify the format
msg.attach(MIMEText(body,'html'))
#print(msg)
#add your password
password = "your password"
#define the smtp server here it is gmail
server = smtplib.SMTP("smtp.gmail.com", 587)
#start the server Transport layer security-- starttls() is ESMTP function to start ssl connection between two server 
server.starttls()
#login with email id and password
server.login(msg['From'], password)
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
