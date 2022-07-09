from dischook import Webhook
import time

wh = Webhook("your webhook URL")
message = wh.send("Hello World!")
time.sleep(1)
message.edit("This message just got edited!")
time.sleep(1)
message.edit("Wow, I can edit again!")
