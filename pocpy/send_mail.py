'''
Ce POC utilise smtplib pour envoyer un e-mail via un serveur de messagerie SMTP.
'''

import smtplib
from email.mime.text import MIMEText

# Paramètres du serveur de messagerie
smtp_server = 'smtp.example.com'
smtp_port = 587
smtp_username = 'your_username'
smtp_password = 'your_password'

# Construction du message
msg = MIMEText('Ceci est un POC d\'envoi d\'e-mail avec Python.')
msg['Subject'] = 'POC d\'envoi d\'e-mail'
msg['From'] = 'sender@example.com'
msg['To'] = 'recipient@example.com'

# Connexion au serveur de messagerie et envoi du message
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    print('E-mail envoyé avec succès !')
