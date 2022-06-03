"""
    File to run App
"""

from kafka import KafkaConsumer
from json import loads
from datetime import datetime

consumer = KafkaConsumer(
    'numtest',
     bootstrap_servers=['localhost:29092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')),
     api_version=(0,11,0))
    

for message in consumer:
    message = message.value
    print(f"{datetime.now()}: {message}")