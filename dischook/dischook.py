from .parse import parse
from typing import Optional
from .components.embeds import Embed
import requests, re
from .errors import Invalid, ApiResponse
from .prop import AllowedMentions


DEFAULT = {
  "Content-Type": "application/json"
}

DEFAULT_MENTION = {}

class WebhookMessage(object):
  def __init__(self, url, json):
    self.json = json
    self.url = url

  @property
  def content(self):
    return self.json['content']

  @property
  def embeds(self):
    return self.json['embeds']

  @property
  def components(self):
    return self.json['components']

  def edit(self, content: str=None, embed: Embed=None, embeds: list=None, components: list=None) -> object:
    """
    Edits the sent webhook message, returns WebhookMessage object.

    :param content: Message content
    :type content: str
    :param embed: A Discord Embed
    :type embed: Embed

    :param embeds: A list of discord embeds
    :type embeds: list

    :param components: A list of components (action rows)
    :type components: list
    """

    if embed:
      _embeds = [embed.json]
    elif embeds:
      _embeds = []
      for e in embeds:
        _embeds.append(e.json)
    else:
      _embeds = None
    
    r = requests.patch(self.url, json={
      "content": content,
      "embeds": _embeds,
      "components": components
    })
    self.json = r.json()
    return WebhookMessage(self.url, r.json())

  

class Webhook():
  """
  Represents a discord webhook object.

  :param url: The webhook url
  :type url: str

  :param headers: Request headers (Optional)
  :type headers: Optional[dict]
  """
  def __init__(self, url: str, headers: Optional[dict]=DEFAULT):
    self.url = parse(url).url
    self.headers = headers
    self.handlers = []

  
  def get_message(self, message_id: int, thread_id: int=None) -> WebhookMessage:
    """
    Finds a sent webhook's message by its id.

    :param message_id: The sent webhook's message ID.
    :type message_id: int

    :param thread_id: If the message was sent in a thread, thread id is required
    :type thread_id: int
    
    """
    url = self.url
    qu = ""
    if thread_id:
      qu = f"?thread_id={thread_id}"
    r = requests.get(url + "/messages/" + str(message_id) + qu)
    
    return WebhookMessage(url + "/messages/" + str(message_id) + qu, r.json())

  def send(self, content: str=None, avatar_url: str=None, username: str=None, embed: Embed=None, embeds: list=None, components: list=None, thread_id: int=None, allowed_mentions: dict=DEFAULT_MENTION) -> WebhookMessage:
    """
    Sends a discord webhook message, returns WebhookMessage object.

    :param content: Message content
    :type content: str

    :param avatar_url: The webhook bot's avatar url.
    :type avatar_url: str

    :param username: The webhook bot's username.
    :type username: str

    :param embed: A Discord Embed
    :type embed: Embed

    :param embeds: A list of discord embeds
    :type embeds: list

    :param components: A list of components (action rows)
    :type components: list

    :param thread_id: Your thread id
    :type thread_id: int

    :param allowed_mentions: Mentions allowed. Check `dishook.AllowedMentions`
    """
    
    query = "?wait=true"
    if thread_id:
      query = query + f"&thread_id={thread_id}"

    if embed:
      _embeds = [embed.json]
    elif embeds:
      _embeds = []
      for e in embeds:
        _embeds.append(e.json)
    else:
      _embeds = None
    
    _components = []
    if components:
      rq = requests.get(self.url)
      if not rq.json()['application_id']:
        raise Invalid("\nSeems like you're trying to use a REGULAR webhook to send a message with components...\nIn short, this webhook wasn't created by a Discord Bot, so you cannot send components by using this webhook.\n")
      if len(components) >= 5:
        raise Invalid(f"Each message can send up to 5 action rows, you cannot send {len(components)} action rows.")

      for c in components:
        _components.append(c.json)
    
    r = requests.post(self.url + query, json={
      "content": content,
      "embeds": _embeds,
      "avatar_url": avatar_url,
      "username": username,
      "components": _components,
      "allowed_mentions": allowed_mentions
    }, headers=self.headers)
    try:
      r.json()['id']
    except:
      raise ApiResponse(f"\n{r.json()}\n")

    if thread_id:
      q = f"?thread_id={thread_id}"
    else:
      q = ""
    return WebhookMessage(self.url + "/messages/" + r.json()['id'] + q, r.json())
