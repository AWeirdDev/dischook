from dischook import Webhook, ActionRow, Select, Option

my_row = ActionRow(
  Select(
    options=[
      Option(
        label="Hello World!",
        value="wow",
        description="This is a default option!",
        emoji="😎", # standard emojies
        default=True # default option
      ),
      Option(
        label="You found me!",
        value="found",
        description="Oops! You found me! I'm not a good hider.",
        emoji="😳",
        default=False
      )
    ],
    placeholder="The placeholder!" # you cannot see the placeholder because of the default option.
  )
)
wh = Webhook("your discord webhook url")
wh.send(components=[my_row])
