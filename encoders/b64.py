import base64

# TODO add optional params?
requiredParams = {
    'encode': {
              },
    'decode': {
              }
    }

def encode(data, params=None):
    return base64.b64encode(data)

def decode(data, params=None):
    return base64.b64decode(data)
