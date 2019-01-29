import requests

username = "AC4c926dfa217a670c02944c1dcce0e21f" #account sid
password = "e594f305ba3b1a558623a20d1debfa83" #auth token

number_to_text = "+19099976615"
twilio_number = "+19513360631"

message_body = "Hi, this is my text message"
media = "https://5.imimg.com/data5/TB/IF/MY-41399105/potato-500x500.jpg"

def xml_pretty(xml_string):
	import xml.dom.minidom
	xml = xml.dom.minidom.parseString(xml_string)
	pretty_xml_ = xml.toprettyxml()
	print(pretty_xml_)

base_url = "https://api.twilio.com/2010-04-01/Accounts"
message_url = base_url + "/" + username + "/Messages"
auth_cred = (username, password)
post_data = {
	"From": twilio_number,
	"To": number_to_text,
	"Body": message_body,
	"MediaUrl": "https://5.imimg.com/data5/TB/IF/MY-41399105/potato-500x500.jpg"
}
r = requests.post(message_url, data=post_data, auth=auth_cred)

print(r.status_code)
xml_pretty(r.text)

message_url_ind = message_url + "/MM2d905b36843a430d84496e606d1b53c6"
get_r = requests.get(message_url_ind,auth = auth_cred)

xml_pretty(get_r.text)