import websocket
import base64

def task_solving(ws, message):

    if "FLAG" in message:
        print("+++++++++++++++")
        print(message)
        print("+++++++++++++++")

    else:
        print("###############")
        
        print(message)
        
        if "(" in message:
            splitted_message = message.split(': ')[1].split('(')[0]
        else:
            splitted_message = message.split(': ')[1]

        print(splitted_message)
        
        decoded_task = str(base64.b64decode(splitted_message), encoding='utf-8')
        print(f"Decoded Task: {decoded_task}")

        solve = eval(decoded_task.split('= ')[1])
        print(f"Answer: {solve}")

        ws.send(str(solve))

        print("###############\n\n")  

ws = websocket.WebSocketApp("ws://62.173.140.174:16011/ws", on_message=task_solving)

ws.run_forever()