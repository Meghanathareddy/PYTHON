from os import close
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
fromaddr = input()
toaddr = input()
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['subject'] = "attachemt with pdf"
body = "I am Meghanatha Reddy"
msg.attach(MIMEText(body, 'plain')) # attach the body with the msg instance
filename = "percentages.pdf"
attachment = open(filename, "rb")
p = MIMEBase('application', 'octet-stream') # instance of MIMEBase and named as p
p.set_payload((attachment).read()) # To change the payload into encoded form
encoders.encode_base64(p) # encode into base64
p.add_header('Content-Disposition', "attachment; filename = %s" % filename)
msg.attach(p) # attach the instance 'p' to instance 'msg'
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
sender_email_id_password = input()
s.login(fromaddr, sender_email_id_password)
# Converts the Multipart msg into a string
text = msg.as_string()
s.sendmail(fromaddr, toaddr, text)
s.quit()