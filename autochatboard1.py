import speech_recognition as sr
import time
import paho.mqtt.client as mqtt
d={'hii':'hello','how are you':'me fine ','and you':',me too','where are you':'at jaipur','what is going on':'i am on training dear','which training dear':'summer training ','in which technology':'in machine learning','great dear':'thanking you'}
sub=input('enter subsribe topic\n')
pub=input('enter pub topic\n')
client=mqtt.Client()
f=0
def msg(client,userdata,message):
    print(message.topic)
    c=str(message.payload.decode("utf-8"))
    print('        ',c)
    print("return")
    if(c in d):
        client.publish(pub,d[c])
    else:
        client.publish(pub,'error')
        f=1
client=mqtt.Client()
a=client.connect('iot.eclipse.org',1883)
client.loop_start()
client.subscribe(sub)
while(1):
    client.on_message=msg
    if f==1:
        break
