from os import getenv

MONGOHOST = getenv("MONGOHOST", "localhost")
MONGOPORT = int(getenv("MONGOPORT", 27017))
MONGOUSER = getenv("MONGOUSER", "root")
MONGOPASS = getenv("MONGOPASS", "123123123")

FLASK_HOST = getenv("FLASK_HOST", "0.0.0.0")
FLASK_PORT = int(getenv("FLASK_PORT", 5009))
FLASK_DEBUG = getenv("FLASK_PORT", True)