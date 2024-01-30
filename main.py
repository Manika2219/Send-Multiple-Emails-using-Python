import smtplib as s
ob= s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('sender mail','sender password')
subject="Test Python"
body="I Love Python sending this using python code"
massage="subject:{}\n\n{}".format(subject, body)
listadd=['Receiver Emails']
ob.sendemail('Sender Email',listadd,massage)
print("send a mail")
ob.quit()

