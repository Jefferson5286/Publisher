from email.message import EmailMessage
from aiosmtplib import SMTP
from .html import email_confirm

from config import env


async def send_confim_code(content: list):
    message = EmailMessage()

    message['To'] = content[0]
    message['Subject'] = 'Meu subject'
    message['From'] = env.BREVO_EMAIL_USER

    message.set_content('Sim')
    message.add_alternative(email_confirm('nano', env.BASE_URL), subtype='html')

    async with SMTP(hostname=env.BREVO_EMAIL_HOST, port=env.BREVO_EMAIL_PORT, start_tls=True, use_tls=False) as smtp:
        await smtp.login(env.BREVO_EMAIL_USER, env.BREVO_EMAIL_PASSWORD)
        await smtp.send_message(message)
