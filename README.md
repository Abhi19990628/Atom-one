# Project Title

Real-Time IoT Dashboard using Python, MQTT, and Node-RED

## Description

This project demonstrates a simple IoT system where a Python script simulates random temperature and humidity data and publishes it to MQTT topics. A Node-RED dashboard subscribes to these topics and displays the values using gauges, offering a real-time monitoring interface.

---

## Project Structure
```
Atom-one/
│
├── data_generator.py # Publishes random sensor data to MQTT broker
└── README.md # Project documentation
```

---

## Tech Stack Used

- **Python** – for generating and publishing simulated data
- **MQTT (HiveMQ broker)** – for lightweight real-time messaging
- **Node-RED** – for building the real-time dashboard
- **paho-mqtt** – Python client for MQTT

---

## How to Run

### Step 1: Clone the Project

```bash
git clone https://github.com/Abhi19990628/Atom-one.git
cd Atom-one
```

### Step 2: Install Required Python Packages

```bash
pip install paho-mqtt
```

### Step 3: Run the Python Script

```bash
python data_generator.py
```

### You should see logs like:
```bash
Connected to MQTT Broker!
Published Temperature: 29.5
Published Humidity: 67.2
...
```

## Node-RED Setup

### 1. Install Node-RED
```bash
npm install -g --unsafe-perm node-red
```

#### Start Node-RED:
```bash
node-red
```
Visit: http://localhost:1880

### 3. View Dashboard
```bash
Visit: http://localhost:1880/ui
You’ll see real-time temperature and humidity gauges.
```

### Output Screenshot
```bash
Add your Node-RED dashboard screenshot here 
```

## Contact
```bash 
If you face any issues or want to connect, feel free to reach out:

📧 Email: abhiv5976@gmail.com

```

