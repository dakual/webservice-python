from datetime import datetime
from flask import jsonify
import uuid

class Response:
  def __init__(self, message):
    self.id = uuid.uuid1()
    self.message = message
    self.timestamp = datetime.now()

  def get(self):
    return jsonify(
        self.id,
        self.message,
        self.timestamp
    )