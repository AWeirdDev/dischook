class AllowedMentions:
  """
  Represents discord's `allowed_mentions` field.
  """
  def no_ping():
    return {
      "parse": []
    }

  def parse(*choices: list):
    ch = []
    for c in choices:
      ch.append(c)
    return {
      "parse": ch
    }


  def users(*users: list) -> dict:
    u = []
    for us in users:
      u.append(str(us))
    return {
      "users": u
    }

  def roles(*roles: list) -> dict:
    r = []
    for ro in roles:
      r.append(str(ro))

    return {
      "roles": r
    }
  
  def custom(parse: list, roles: list=None, users: list=None) -> dict:
    return {
      "parse": parse,
      "roles": roles,
      "users": users
    }
