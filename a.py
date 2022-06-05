from confluent_kafka import Consumer, Producer


c = Consumer(
    {
        "bootstrap.servers": "pkc-epwny.eastus.azure.confluent.cloud:9092",
        "security.protocol": "SASL_SSL",
        "sasl.mechanisms": "PLAIN",
        "sasl.username": "SXE57BOJVWTB2KK3",
        "sasl.password": "XoILmw1EPO1ggIUU6xY1iK7UodIKf5C5MSrLR+/frO8PQF3CIfpQrVHwJCdhmGdR",
        "group.id": "mygroup",
        "auto.offset.reset": "earliest",
    }
)
producer = Producer(
    {
        "bootstrap.servers": "pkc-epwny.eastus.azure.confluent.cloud:9092",
        "security.protocol": "SASL_SSL",
        "sasl.mechanisms": "PLAIN",
        "sasl.username": "SXE57BOJVWTB2KK3",
        "sasl.password": "XoILmw1EPO1ggIUU6xY1iK7UodIKf5C5MSrLR+/frO8PQF3CIfpQrVHwJCdhmGdR",
    }
)

c.subscribe(["Block"])

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
    
    producer.produce('Block', "teste", callback=delevery_report)
    print("Received message: {}".format(msg.value().decode("utf-8")))

c.close()
