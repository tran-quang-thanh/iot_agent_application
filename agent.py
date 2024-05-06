from pymodbus.client import AsyncModbusTcpClient as ModbusClient
import time
from paho.mqtt import publish 
import json
import asyncio


async def run_async_client(host, port):
    mbclient = ModbusClient(host, port=port)
    await mbclient.connect()
    assert mbclient.connected

    while True:
        try:
            # Read value of coil 1
            coil = await mbclient.read_coils(1, 1)
            print("coil: ", coil.bits)

            # Read values from holding registers 2 and 3
            holding = await mbclient.read_holding_registers(2, 2)
            print("holding: ", holding.registers)

            data = {
                'coil': coil.bits,
                'holding': holding.registers
            }

            publish.single(
                topic="iot",
                payload=str(json.dumps(data)),
                hostname="test.mosquitto.org"
            )

        except KeyboardInterrupt:
            mbclient.close()
            return
        
        except Exception as e:
            print(e)

        time.sleep(5)

if __name__ == '__main__':
    asyncio.run(
        run_async_client('127.0.0.1', port=5020)
    )