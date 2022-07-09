from typing import Union
import re, discord, string, random
from ..errors import UnknownEmoji, Invalid


class Style:
  """
  Button Styles
  """
  primary = CTA = blurple = blue = 1
  secondary = gray = grey = 2
  success = green = 3
  destructive = red = 4
  URL = url = link = 5
  

class Button(object):
  """
  Represents discord buttons.
  Note that buttons should be INSIDE an **actionrow**.

  :param style: The button style. Should be `int` or `Style`. For instance, `3` or `dishook.Style.green` for green color.
  :type style: Union[Style, int]

  :param label: The button label, should be `str`.
  :type label: str

  :param emoji: The button emoji. Should be a standard emoji like `🔥`, or a custom emoji like: `<:concerned:969632310905417758>` (str) or a discord emoji object.
  :type emoji: Union[str, int, discord.Emoji]

  :param custom_id: Custom ID of your button. By default, it will be set to a random generated ID.
  :type custom_id: str

  :param disabled: Whether the button is disabled or not. By default, it's set to `False`.
  :type disabled: bool

  :param url: The button URL if the style is `dishook.Style.URL`
  :type url: str
  """
  def __init__(self, style: Union[Style, int], label: str, emoji: Union[str, int, discord.Emoji]=None, custom_id: str=None, disabled: bool=False, url: str=None) -> None:
    if not custom_id:
      char = string.ascii_letters + string.digits
      custom_id = ''.join(random.choice(char) for i in range(15))

    if emoji:
      if isinstance(emoji, discord.Emoji):
        emoji = {
          "id": str(emoji.id),
          "name": str(emoji.name),
          "animated": emoji.animated
        }
      elif isinstance(emoji, str):
        qu = re.search(r'\<a?\:.*:[0-9]*\>', emoji)
        if qu:
          emojiID = re.search(r"\:[0-9]*\>", emoji).group()
          name = re.search(r"\:.*\:", emoji).group().replace(":", "")
          emoji = {
            "id": emojiID.replace(":", "").replace(">", ""),
            "name": name,
            "animated": emoji.startswith("<a:")
          }
        else:
          emoji = {
            "id": None,
            "name": emoji
          }

    self._type = "Button"

    if style !=5:
          
      self.json = {
        "type": 2,
        "style": style,
        "label": label,
        "emoji": emoji,
        "custom_id": custom_id,
        "disabled": disabled,
      }  
    else:
      self.json = {
        "type": 2,
        "style": style,
        "label": label,
        "emoji": emoji,
        "disabled": disabled,
        "url": url
      } 
      
    return None


class Option(object):
  """
  Option object for select menus.

  :param label: The option label.
  :type label: str

  :param value: The option value.
  :type value: str

  :param description: Option description
  :type description: str

  :param emoji: The button emoji. Should be a standard emoji like `🔥`, or a custom emoji like: `<:concerned:969632310905417758>` (str) or a discord emoji object.
  :type emoji: Union[str, int, discord.Emoji]

  :param default: Default Option?
  :type default: bool
  """
  def __init__(self, label: str, value: str, description: str=None, emoji: Union[int, str, discord.Emoji]=None, default: bool=False):
    
    if emoji:
      if isinstance(emoji, discord.Emoji):
        emoji = {
          "id": str(emoji.id),
          "name": str(emoji.name),
          "animated": emoji.animated
        }
      elif isinstance(emoji, str):
        qu = re.search(r'\<a?\:.*:[0-9]*\>', emoji)
        if qu:
          emojiID = re.search(r"\:[0-9]*\>", emoji).group()
          name = re.search(r"\:.*\:", emoji).group().replace(":", "")
          emoji = {
            "id": emojiID.replace(":", "").replace(">", ""),
            "name": name,
            "animated": emoji.startswith("<a:")
          }
        else:
          emoji = {
            "id": None,
            "name": emoji
          }
    self.json = {
      "label": label,
      "value": value,
      "description": description,
      "emoji": emoji,
      "default": default
    }



class Select(object):
  """
  Represents a discord select menu.

  :param options: Select options. Inside should be `dishook.Option`
  :type options: list

  :param placeholder: Select menu placeholder.
  :type options: str

  :param min_values: Minimum values should be selected.
  :type min_values: int

  :param max_values: Maximum values should be selected.
  :type max_values: int

  :param custom_id: Select menu's custom id.
  :type custom_id: str

  :param disabled: Whether the select menu is disabled or not.
  :type disabled: bool
  """
  def __init__(self, options: list, placeholder: str=None, min_values: int=1, max_values: int=1, custom_id: str=None, disabled: bool=False) -> None:
    if not custom_id:
      char = string.ascii_letters + string.digits
      custom_id = ''.join(random.choice(char) for i in range(15))

    self._type = "ActionRow"
    _options = []
    for op in options:
      _options.append(op.json)
      
    self.json = {
      "type": 3,
      "options": _options,
      "placeholder": placeholder,
      "custom_id": custom_id,
      "min_values": min_values,
      "max_values": max_values,
      "disabled": disabled
    }
    return None


class ActionRow(object):
  """
  Represents an action row.
  """
  def __init__(self, *components: Union[Button, Select]):
    if len(components) == 0:
      raise Invalid("\nThe ActionRow is empty.\n")
    check = []
    for c in components:
      check.append(c._type)
    if "ActionRow" in check and "Button" in check:
      raise Invalid("\nYou can only add one select menu in each action row.")
    elif "".join(check) == "Button"*len(check):
      if len(components) > 5:
        raise Invalid(f"\nThe limit of buttons in each action row is 5, you cannot add {len(components)} of them.")

    comp = []
    for c in components:
      comp.append(c.json)


    self.json = {
      "type": 1,
      "components": comp
    }
