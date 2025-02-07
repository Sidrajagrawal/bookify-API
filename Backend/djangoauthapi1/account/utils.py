from django.core.mail import EmailMessage
import os
import logging

logger = logging.getLogger(__name__)

class Util:
    @staticmethod
    def send_email(data):
        try:
            # Ensure "to_email" is a list
            to_email = data['to_email']
            if not isinstance(to_email, (list, tuple)):
                to_email = [to_email]

            email = EmailMessage(
                subject=data['subject'],
                body=data['body'],
                from_email=os.environ.get('EMAIL_FROM'),
                to=to_email,
            )
            # Add support for HTML emails if needed
            if data.get('is_html', False):
                email.content_subtype = 'html'

            email.send()
            logger.info(f"Email sent successfully to {to_email}")
        except Exception as e:
            logger.error(f"Failed to send email to {to_email}: {e}")
            raise
