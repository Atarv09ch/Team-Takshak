import os
from twilio.rest import Client

def sendMSG(msg, ph_no) :
    account_atarva = "ACb8b05c3a3b447064a4dc61295ef83455"
    auth_token = "210d506d352e5754ba5edc140001988a"
    client = Client(account_atarva, auth_token)
    message = client.messages.create(
      body=msg,
      from_="+12707704034",
      to=ph_no
    )
    return (message.atarva)
