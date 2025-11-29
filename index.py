# Install Twilio 
# !pip install twilio

from twilio.rest import Client

# Twilio credentials
account_id = "YOUR_ACCOUNT_ID"
auth_token = "YOUR_AUTH_TOKEN"
client = Client(account_id, auth_token)


message = client.messages.create(
    body="Hello! what are doing" 
    from_="+7850891099",    
    to="‪+918094159270‬")     

}
print("Message sent! ID:", message.id)
