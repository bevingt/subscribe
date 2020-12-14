import base64

def base64_encode(data):
    return base64.b64encode(data.encode()).decode("utf-8")