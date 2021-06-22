#Sending mail to multiple users from your Gmail account 
import smtplib
li = ["kmeghanath99@gmail.com", "kmeghanath99@gmail.com"]
for dest in li:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    sender_email_id = input()
    sender_email_id_password = input()
    s.login(sender_email_id, sender_email_id_password)
    message = "Message_you_need_to_send"
    s.sendmail(sender_email_id, dest, message)
    s.quit()