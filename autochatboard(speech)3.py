import speech_recognition as sr
import time
import paho.mqtt.client as mqtt
def msg(client,userdata,message):
    print(message.topic)
    print('recieved message=',str(message.payload.decode('utf-8')))
sub=input('enter subsribe topic')
pub=input('enter pub topic')
client=mqtt.Client()
a=client.connect('iot.eclipse.org',1883)
client.loop_start()
client.subscribe(sub)
r=sr.Recognizer()
chat='gf'
while(1):
    with sr.Microphone() as s:
        print('please speak')
        a=r.listen(s)
    chat=r.recognize_google(a)
    print('chat'+'1')
    client.publish(pub,chat)
    client.on_message=msg
