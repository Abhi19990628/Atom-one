import paho.mqtt.client as mqtt
import random
import time
import threading

# MQTT Broker settings
BROKER = "broker.hivemq.com"  # Public MQTT broker
PORT = 1883
TOPIC_TEMP = "Atom/temperature"
TOPIC_HUM = "Atom/humidity"

# MQTT Client setup
client = mqtt.Client()

def connect_mqtt():
    client.connect(BROKER, PORT, 60)
    print("Connected to MQTT Broker!")

# Function to generate and publish temperature
def generate_temperature():
    while True:
        temp = round(random.uniform(20.0, 40.0), 2)  # Random temp between 20.0 and 40.0
        client.publish(TOPIC_TEMP, str(temp))
        print(f"Published Temperature: {temp}")
        time.sleep(0.5)  # Publish every 0.5 seconds

# Function to generate and publish humidity
def generate_humidity():
    while True:
        hum = round(random.uniform(30.0, 90.0), 2)  # Random humidity between 30.0 and 90.0
        client.publish(TOPIC_HUM, str(hum))
        print(f"Published Humidity: {hum}")
        time.sleep(0.5)  # Publish every 0.5 seconds

# Main function to start threads
def main():
    connect_mqtt()
    # Start threads for temperature and humidity
    temp_thread = threading.Thread(target=generate_temperature)
    hum_thread = threading.Thread(target=generate_humidity)
    temp_thread.daemon = True  # Threads stop when main program exits
    hum_thread.daemon = True
    temp_thread.start()
    hum_thread.start()
    
    # Keep the main thread running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping...")
        client.disconnect()

if __name__ == "__main__":
    main()