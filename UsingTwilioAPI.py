import requests
from twilio.rest import TwilioRestClient
from twilio.rest import Client

account_sid = "AC4c926dfa217a670c02944c1dcce0e21f" #account sid
auth_token = "e594f305ba3b1a558623a20d1debfa83" #auth token

client = Client(account_sid, auth_token)

number_to_text = "+19099976615"
twilio_number = "+19513360631"

message_body = "Using API!!!!"
media = "https://5.imimg.com/data5/TB/IF/MY-41399105/potato-500x500.jpg"

"""
Create / Send --- Post Method
"""

message = client.messages.create(
	to = number_to_text, 
	from_ = twilio_number,
	body = message_body,
	media_url = media)
print(message.sid)
print(message.media_list.list())
"""
status_callback = send message to url
message = client.messages.create(
	to = number_to_text,
	from = twilio_number,
	body = message,
	media_url = media_url,
	status_callback = ""
	)
"""