import json
from random import randint
from time import sleep

from channels.generic.websocket import WebsocketConsumer

class KiteConsumer(WebsocketConsumer):

	def connect(self):
		self.accept()

		for i in range(1000):
			self.send(json.dumps({"message": randint(1, 100)}))
			sleep(1)

	def disconnect(self, close_code):
		pass

	# receive message from WebSocket
	def receive(self, text_data):
		text_data_json = json.loads(text_data)
		message = text_data_json['message']
		# send message to WebSocket
		self.send(text_data=json.dumps({'message': message}))