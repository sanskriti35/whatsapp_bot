import twilio
from twilio.rest import Client 
 
account_sid = 's0mething' 
auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' 
client = Client(account_sid, auth_token) 
def send_love():

    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Hey! This will go directly and automatically. If you want me to help you with this, please let me know',      
                              to='whatsapp:+1555555555555' 
                          ) 
 
    print(message.sid)

