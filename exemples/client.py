from lysia.models.events.api import ReadyPayload
from lysia.implementations.client import Client

client = Client("TOKEN")

client.start()
