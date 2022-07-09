from typing import Union
from ..errors import FormatError

defaultColor = 0x2f3136

class Embed(object):
  """
  Represents a Discord Webhook Embed.

  :param title: The embed title
  :type title: str

  :param description: The embed description (body content)
  :type description: str

  :param color: The embed color
  :type color: Union[int, str]

  :param url: The url for the title
  :type url: str
  """
  def __init__(self, title: str=None, description: str=None, color: Union[int, str]=defaultColor, url: str=None) -> None:
    if isinstance(color, str):
      if (color.startswith("#")) or (color.startswith("0x")):
        color.replace("#", "0x", 1)
      else:
        raise FormatError(f"\nInvalid color hex! (Example: 0x0995ec OR '#0995ec')\n")
      color = int(color, base=16)
    self.json = {
      "title": title,
      "description": description,
      "color": color,
      "url": url,
      "fields": []
    }

  def set_footer(self, text: str=None, icon_url: str=None) -> None:
    """
    Sets the embed footer.

    :param text: The footer text to display.
    :type text: str

    :param icon_url: The footer's icon url.
    :type icon_url: str
    
    """
    self['footer'] = {
      "text": text,
      "icon_url": icon_url
    }
    return None

  def add_field(self, name: str, value: str, inline: bool=True) -> None:
    """
    Add a field to the embed.

    :param name: The field title
    :type name: str

    :param value: The field content
    :type value: str

    :param inline: Inline? (Default is True)
    :type inline: bool
    """
    if len(self.json['fields']) > 25:
      raise FormatError(f"\nLimit of embed fields reached: 25, cannot add {len(self.json['fields'])} of them.")
    self.json['fields'].append({
      "name": name,
      "value": value,
      "inline": inline
    })
    return None

  def set_thumbnail(self, url: str) -> None:
    """
    Sets the embed thumbnail.

    :param url: The embed thumbnail image url.
    :type url: str
    """
    self.json['thumbnail'] = {
      "url": url
    }
    return None

  def set_image(self, url: str) -> None:
    """
    Sets the embed large image.

    :param url: The embed large image url.
    :type url: str
    """
    self.json['image'] = {
      "url": url
    }
    return None

  def set_author(self, name: str=None, icon_url: str=None, url: str=None) -> None:
    """
    Sets the embed author.

    :param name: Author name
    :type name: str

    :param icon_url: The author's icon url (avatar)
    :type icon_url: str

    :param url: A link to the author's page url
    :type url: str
    """
    self.json['author'] = {
      "name": name,
      "icon_url": icon_url,
      "url": url
    }

# welcome to the world of tomorrow
