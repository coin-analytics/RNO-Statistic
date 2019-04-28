from flask import Flask


class FlaskApp(Flask):
    def __init__(self, **config):
        super().__init__(config.get("name", __name__))

        self._host      = config.get("host", "localhost")
        self._port      = config.get("port", 8080)
        self._debug     = config.get("debugging", False)
        self._threaded  = config.get("threading", True)

    def extract_config(self):
        return {
            "host": self._host,
            "port": self._port,
            "debug": self._debug,
            "threaded": self._threaded
        }

    def start(self):
        self.run(**self.extract_config())

