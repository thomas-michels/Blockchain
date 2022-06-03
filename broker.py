from datetime import datetime
from json import dumps
from time import sleep
from confluent_kafka import Producer

def delevery_report(err, msg):
    if err is not None:
        print(f"Message failed - {err}")

    else:
        print(f"Message success - topic: {msg.topic()}")

print("Connecting")
producer = Producer({"bootstrap.servers": 'pkc-epwny.eastus.azure.confluent.cloud:9092',
                    "security.protocol": "SASL_SSL",
                    "sasl.mechanisms": "PLAIN",
                    "sasl.username": "WYRFUG5BZBPJY3WL",
                    "sasl.password": "NjgVbaohPVooqCg492LkQxysl7X6YCHcmCB3YXcVkmWg5h9qU+aIqCZVPsp1EWOO"
                    })
print(f"{datetime.now()}: connected")

for e in range(1000):
    # producer.poll(0)
    data = {'number' : e}
    producer.produce('numtest', str(data).encode("utf-8"), callback=delevery_report)
    print(f"{datetime.now()}: Sended - {data}") 
    sleep(5)

producer.flush()
