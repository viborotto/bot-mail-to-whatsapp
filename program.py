import imaplib, email, getpass
from email import policy
import time
from twilio.rest import Client

account_sid = 'getAccountSIDTwilio'
auth_token = 'authTokenTwilio'
client = Client(account_sid, auth_token)

imap_host = 'imap.gmail.com'
username = 'email@gmail.com'
password = 'senha!email'

# init imap connection
mail = imaplib.IMAP4_SSL(imap_host, 993)
# rc, resp = mail.login(imap_user, password)

# select only unread messages from inbox
mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
mail.login(imap_user, password)
mail.select('Inbox')


status, data = mail.search(None, '(UNSEEN)')

# for each e-mail messages, print text content
for num in data[0].split():
    # get a single message and parse it by policy.SMTP (RFC compliant)
    status, data = mail.fetch(num, '(RFC822)')
    email_msg = data[0][1]
    email_msg = email.message_from_bytes(email_msg, policy=policy.SMTP)

    print("\n----- MESSAGE START -----\n")

    print(str(email_msg['Subject']))

    # print only message parts that contain text data
    for part in email_msg.walk():
        if part.get_content_type() == "text/plain":
            for line in part.get_content().splitlines():
                print(line)

    print("\n----- MESSAGE END -----\n")
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=line,
        to='whatsapp:+5511992346309'
    )
