import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
sender_email_id = input()
sender_email_id_password = input()
receiver_email_id = input()
s.login(sender_email_id, sender_email_id_password)
message = "Message_you_need_to_send"
s.sendmail(sender_email_id, receiver_email_id, message)
s.quit()