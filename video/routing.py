from channels.routing import route

channel_routing = [
    route( "http.request", "video.consumers.http_consumer")
]