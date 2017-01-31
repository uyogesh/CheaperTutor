from django.http import HttpResponse
from channels.handler import AsgiHandler


def http_consumer(message):
    response = HttpResponse("Hello! you asked for path %s" % message.content['path'])

    for chunk in AsgiHandler.encode_response(response):
        message.reply_channel.send(chunk)
