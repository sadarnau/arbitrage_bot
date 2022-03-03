import json
from time import time
import websocket
import os
from dotenv import load_dotenv

load_dotenv()


def handleOpen(ws):
    print("OPEN")
    ws.send(
        json.dumps(
            {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "eth_subscribe",
                "params": ["newHeads"],
            }
        )
    )


def handleError(ws, error):
    print(error, flush=True)


def handleClose(ws, close_status_code, close_msg):
    print("close")


def handleMessage(ws, message):
    print(message)


def listen2Socket():
    ws = websocket.WebSocketApp(
        "wss://polygon-mainnet.g.alchemy.com/v2/" + os.getenv("ALCHEMY_KEY"),
        on_open=handleOpen,
        on_close=handleClose,
        on_error=handleError,
        on_message=handleMessage,
    )
    ws.run_forever()


listen2Socket()


# try:
#     ws = create_connection("wss://polygon-mainnet.g.alchemy.com/v2/" + ALCHEMY_KEY)
# except Exception as error:
#     print("Connection error :", repr(error))
#     time.sleep(3)

# ws.send(
#     json.dumps(
#         {"jsonrpc": "2.0", "id": 1, "method": "eth_subscribe", "params": ["newHeads"]}
#     )
# )

# ws.
