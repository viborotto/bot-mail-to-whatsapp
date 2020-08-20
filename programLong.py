import imaplib
import email
from email.header import decode_header
from twilio.rest import Client

account_sid = 'getAccountSIDTwilio'
auth_token = 'authTokenTwilio'
client = Client(account_sid, auth_token)

# account credentials
username = 'email@gmail.com'
password = 'senha!email'

# create an IMAP4 class with SSL
imap = imaplib.IMAP4_SSL("imap.gmail.com")
# authenticate
imap.login(username, password)

status, messages = imap.select("INBOX")
# number of top emails to fetch
N = 1
# total number of emails
messages = int(messages[0])

for i in range(messages, messages - N, -1):
    # fetch the email message by ID
    res, msg = imap.fetch(str(i), "(RFC822)")
    for response in msg:
        if isinstance(response, tuple):
            # parse a bytes email into a message object
            msg = email.message_from_bytes(response[1])
            # decode the email subject
            subject = decode_header(msg["Subject"])[0][0]
            if isinstance(subject, bytes):
                # if it's a bytes, decode to str
                subject = subject.decode()
            # email sender
            from_ = msg.get("From")
            # if the email message is multipart
            if msg.is_multipart():
                # iterate over email parts
                for part in msg.walk():
                    # extract content type of email
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    try:
                        # get the email body
                        body = part.get_payload(decode=True).decode()
                    except:
                        pass
                    if content_type == "text/plain" and "attachment" not in content_disposition:
                        # print text/plain emails and skip attachments
                        print(body)
                        message = client.messages.create(
                            from_='whatsapp:+14155238886',
                            body=body,
                            to='whatsapp:+5511942320406'
                        )
                    elif "attachment" in content_disposition:
                        # download attachment
                        filename = part.get_filename()
            else:
                # extract content type of email
                content_type = msg.get_content_type()
                # get the email body
                body = msg.get_payload(decode=True).decode()
                if content_type == "text/plain":
                    # print only text email parts
                    print(body)
                    message = client.messages.create(
                        from_='whatsapp:+14155238886',
                        body=body,
                        to='whatsapp:+5511942320406'
                    )
            print("=" * 100)
imap.close()
imap.logout()







