import twilio
from twilio.rest import Client 
 
account_sid = 'AC24859f27775492518fce0f1068fe93d0' 
auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' 
client = Client(account_sid, auth_token) 
def send_love():

    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='You are the best mom in the world',      
                              to='whatsapp:+1555555555555' 
                          ) 
 
    print(message.sid)

