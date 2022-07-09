"""
Errors
"""

class FormatError(Exception):
  """String, or other type of format error."""
  pass

class UnknownEmoji(Exception):
  """Cannot find an emoji, or the format is invalid"""
  pass

class Invalid(Exception):
  pass

class ApiResponse(Exception):
  """API Response Error"""
  pass
