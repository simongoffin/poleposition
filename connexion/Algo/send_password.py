#-*- coding: utf-8 -*-
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate

def send_password(adresse,password):

    fromaddr = 'polepositionbe@gmail.com'
    toaddrs  = unicode(adresse)
    
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = COMMASPACE.join(toaddrs)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = "Pole Position password"
    text = 'Votre password pour votre compte Pole-Position est: '+password
    
    msg.attach( MIMEText(text) )


    # Credentials (if needed)
    username = 'polepositionbe@gmail.com'
    password = 'Gavroches1987'

    # The actual mail send
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs, msg.as_string())
        server.quit()
    except:
        return False
    return True
    
    
