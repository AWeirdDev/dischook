from dischook import Webhook, Button, ActionRow, Style

my_row = ActionRow(
  Button(
    style=Style.green,
    label="Click here?",
    emoji="<:concerned:969632310905417758>", # you can place custom emojies like this!
    custom_id="epic_button_id"
  ),
  Button(
    style=Style.URL,
    label="Learn More",
    url="https://discord.com/app"
  )
)
w = Webhook("your discord webhook URL")
w.send("Hello World, and here's some buttons:", components=[my_row])
