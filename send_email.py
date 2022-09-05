import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('email.html').read_text())
email = EmailMessage()
email['from'] = 'Joe Mama'
email['to'] = 'joe@gmail.com'
email['subject'] = 'You won 1,000,000 bitcoins!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('email@gmail.com', 'password123')
	smtp.send_message(email)