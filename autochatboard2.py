import paho.mqtt.client as mqtt
import datetime
def msg(client,user_data,message):
    print('\n',message.topic)
    time=datetime.datetime.now()
    time1=list(time)
    time2=
    print('recieved message=',str(message.payload.decode("utf-8")))
sub=input('enter subcriber topic\n')
pub=input('enter publish topic\n')    
client=mqtt.Client()

client.connect('iot.eclipse.org',1883)
client.loop_start()

client.subscribe(sub)
while (1): 
   chat = input("Enter text: \n") 
   if chat == 'QUIT': 
       break  
   else: 
       client.publish(pub, chat)
       client.on_message=msg



