# Iot Agent Application
A system that creates an agent to read data from device using modbus, monitoring and send to mqtt server.

## Requirements
- Python 3
- Node-red server to as the centralised platform

## Installation
### Python libraries
```
pip install -r requirements.txt
```
### Node red
- Install Node.js
- Install node-red as instructed in documentation `https://nodered.org/docs/getting-started/local`

## Execution
### Open separate terminatls and run in order
1. Server (Device)
2. Agent
3. Node red (Centralised Platform)

### Server
```
python server_async.py
```

### Agent
```
python agent.py
```

### Node red
- Open node-red by running
```
node-red
```

- Load `flows.json` file to node red