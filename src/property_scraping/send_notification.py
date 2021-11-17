import smtplib, ssl
from load_config import load_config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import constants

config = load_config('config.yml')

def send_notification():
    port = 465
    smtp_server = 'smtp.gmail.com'

    message = MIMEMultipart('mixed')
    message['From'] = config['EMAIL_ADDRESS']
    message['To'] = config['EMAIL_ADDRESS']
    message['Subject'] = 'Rent Compilation Data'
    msg_content = '<h4>Hi There,<br><br> Rent compilation data is ready as attached. <br><br>Regards, <br>CompareX </h4>\n'
    body = MIMEText(msg_content, 'html')
    message.attach(body)
    attachment_path = constants.results_path
    try:
        with open(attachment_path, "rb") as attachment:
            p = MIMEApplication(attachment.read())
            p.add_header('Content-Disposition', "attachment; filename= %s" % attachment_path.split("//")[-1])
            message.attach(p)
    except Exception as e:
        print(str(e))

    msg_full = message.as_string()

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(config['EMAIL_ADDRESS'], config['EMAIL_PASSWORD'])
            server.sendmail(config['EMAIL_ADDRESS'], [config['EMAIL_ADDRESS']], msg_full)
        print ('-'*30)
        print ("Email Notification -> Message has been sent.")
        print ('-'*30)
    except Exception as e:
        print (e)
