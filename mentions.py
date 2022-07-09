from dischook import Webhook, AllowedMentions

allowed = AllowedMentions.no_ping()
wh = Webhook("your discord webhook URL")
wh.send("I like chocolate! <@your-id>", allowed_mentions=allowed)
# you won't get mentioned!
