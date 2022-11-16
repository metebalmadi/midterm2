import paho.mqtt.client as mqtt
import json

# broker_address="localhost"
broker_address = "10.20.1.95"



# This is the Publisher
client = mqtt.Client()
topic = "se443/midterm2"

x =  { "StudentID":200304, "Name":"Meteb", "Surname":"Almadi", "Telephone":"0554271113", "Grade": 100}

y = json.dumps(x)

message = y

# message = "Hello from George V's Python client..."
if (client.connect(broker_address,1883,60) ==0):
	print ("Connected succesfully to "+broker_address)
	
client.publish(topic, message)
print ("Published in "+topic+", msg = "+message)
client.disconnect();