from .errors import FormatError
import re
from .colors import bcolors

class Parsed():
  def __init__(self, url):
    self.url = url

def parse(url):
  if not url.startswith("https://discord.com/api/webhooks/"):
    raise FormatError("This is not a discord webhook URL!\n")
  if "?" in url:
    qu = re.search(r'\?.*\=.*', url).group()
    print(f"{bcolors.warning}You don't need to add query strings in the URL.\nI've removed query String: '{qu}'{bcolors.end}")
    url = url.replace(qu, "")
  return Parsed(url)
