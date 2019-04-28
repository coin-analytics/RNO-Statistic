import logging
import traceback
from flask import Flask


class FlaskApp(Flask):
    def __init__(self, **config):
        self.name = config.get("name", __name__)
        super().__init__(self.name)

        self._host      = config.get("host", "localhost")
        self._port      = config.get("port", 8080)
        self._debug     = config.get("debugging", False)
        self._threaded  = config.get("threading", True)

        self.logger = logging.getLogger("{0}.{1}".format(self.__class__.__qualname__, self.name))

    def extract_config(self):
        return {
            "host": self._host,
            "port": self._port,
            "debug": self._debug,
            "threaded": self._threaded
        }

    def register_mass_blueprints(self, bps):
        for bp in bps:
            try:
                self.register_blueprint(bp.blueprint)
            except Exception as ex:
                self.logger.warning("Blueprint `{name}` was not registered\n\n ----- {name} -----\n{tb}".format(
                    name=bp.name,
                    tb=traceback.format_exc(ex)
                ) )

    def start(self):
        self.run(**self.extract_config())

