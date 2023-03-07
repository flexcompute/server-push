class Dev:
    simcloud_event_bridge = "arn:aws:events:us-east-1:343549021813:event-bus/simcloud-event-bus-dev"
    datetime_format: str = "YYYY-MM-DDTHH:mm:ss.SSS[Z]"


class Prod(Dev):
    simcloud_event_bridge = ""


Settings = Dev()
