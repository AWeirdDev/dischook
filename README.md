# dischook
Welcome To The Official dischook Docs!

We've updated the latest version of dischook.

## Getting Started
Installing:
```
pip install git+https://github.com/AWeirdScratcher/dischook
```

## Simple Discord Webhook
Send a message with username "Happy Bot":
```py
from dischook import Webhook
wh = Webhook("your discord webhook URL")
wh.send("Hello World!", username="Happy Bot", avatar_url="Insert Avatar URL here") # sends a message
```

![success](https://user-images.githubusercontent.com/90096971/177906114-970c951b-60c6-4f0d-80e0-0dc74bdec2cb.png)

***

Sending Embeds:
```py
from dischook import Webhook, Embed
wh = Webhook("your discord webhook URL")

embed = Embed(title="Great Embed", description="Great description (maybe)", color=0x0995ec) # color should use hex
embed2 = Embed(title="Another Embed Appears!")
wh.send("Hello again!", username="Happy Bot", embeds=[embed, embed2])
```

![image](https://user-images.githubusercontent.com/90096971/177906698-cd0d9cc2-4115-4a2c-9af8-bf42a3602c95.png)

### Find more examples [here](), including how to send **components** using webhooks.

***

![dischookholder](https://user-images.githubusercontent.com/90096971/177905091-5b432c07-4d0f-444b-a209-ce527861b581.png)
