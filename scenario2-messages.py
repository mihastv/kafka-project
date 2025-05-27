from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='192.168.1.106:9092')

start = time.time()
for i in range(10000):
    msg = f'{{"msg_num": {i}, tthis $% a testtthis is a testtthis is a testtthis is a testtthis is a %^&*}}'
    producer.send('scenario2', msg.encode('utf-8'))
producer.flush()
end = time.time()

print(f"Sent 10,000 messages in {end - start:.2f} seconds")