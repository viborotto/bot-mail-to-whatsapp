from twilio.rest import Client

account_sid = 'getAccountSIDTwilio'
auth_token = 'authTokenTwilio'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14000000000',
    body='Hello from Python To Whatsapp',
    to='whatsapp:+5511000000000'
)

print(message.sid)
