from confluent_kafka import Consumer, Producer


c = Consumer(
    {
        "bootstrap.servers": "pkc-epwny.eastus.azure.confluent.cloud:9092",
        "security.protocol": "SASL_SSL",
        "sasl.mechanisms": "PLAIN",
        "sasl.username": "WYRFUG5BZBPJY3WL",
        "sasl.password": "NjgVbaohPVooqCg492LkQxysl7X6YCHcmCB3YXcVkmWg5h9qU+aIqCZVPsp1EWOO",
        "group.id": "mygroup",
        "auto.offset.reset": "earliest",
    }
)
producer = Producer(
    {
        "bootstrap.servers": "pkc-epwny.eastus.azure.confluent.cloud:9092",
        "security.protocol": "SASL_SSL",
        "sasl.mechanisms": "PLAIN",
        "sasl.username": "WYRFUG5BZBPJY3WL",
        "sasl.password": "NjgVbaohPVooqCg492LkQxysl7X6YCHcmCB3YXcVkmWg5h9qU+aIqCZVPsp1EWOO",
    }
)

c.subscribe(["numtest"])

def delevery_report(err, msg):
    if err is not None:
        print(f"Message failed - {err}")

    else:
        print(f"Message success - topic: {msg.topic()}")

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue
    
    producer.produce('redirect', str(msg).encode("utf-8"), callback=delevery_report)
    print("Received message: {}".format(msg.value().decode("utf-8")))

c.close()
