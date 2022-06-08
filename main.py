import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('sender email','Sender password')
server.sendmail('sender email','receiver email','type your message')


# make sure must turn on Less secure app access
# steps to turn on:

#1) go to Security
#2) make sure turn off 2_step verification
#3) turn on Less secure app access
