from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='192.168.1.106:9092')

start = time.time()
for i in range(100):
    msg = f'{{"msg_num": {i}}}'
    producer.send('scenario3', msg.encode('utf-8'))
    time.sleep(0.05)
producer.flush()
end = time.time()

print(f"Sent 500 messages in {end - start:.2f} seconds")