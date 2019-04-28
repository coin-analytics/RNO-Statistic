from flask import Blueprint


class RSBlueprint:
    def __init__(self, *args, **kwargs):
        self.prefix = kwargs.get("prefix")
        if self.prefix: del kwargs["prefix"]

        self._blueprint = Blueprint(*args, **kwargs)
        self.route = self._blueprint.route

    @property
    def blueprint(self):
        return self._blueprint

    @property
    def url_prefix(self):
        return self.prefix

    @property
    def name(self):
        return self._blueprint.name
