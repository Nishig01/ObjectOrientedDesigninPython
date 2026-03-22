# Lets you define a subscription mechanism to notify multiple objects about any events
# that happen to the object they’re observing.

class EventSystem:
    def __init__(self):
        self._listeners = {} #dictionary created

    def subscribe(self, event:str, callback):
        self._listeners.setdefault(event, []).append(callback)

    def emit(self, event:str, data=None):
        for callback in self._listeners.get(event, []): # Multiple callbacks in single event --> "order_placed": [callback_function_1, callback_function_2]
            callback(data)


events = EventSystem()
events.subscribe("order_placed", lambda data: print(f"Email sent for {data}"))
events.subscribe("order_placed", lambda data: print(f"Inventory updated for {data}"))
events.emit("order_placed", "Order #123")
# Email sent for Order #123
# Inventory updated for Order #123

