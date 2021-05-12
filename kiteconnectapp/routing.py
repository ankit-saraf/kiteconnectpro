from django.urls import path
from . import consumers

websocket_urlpatterns = [
	path('ws/live-stream/', consumers.KiteConsumer, name="live-stream"),
]