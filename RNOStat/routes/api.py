from ..blueprint import RSBlueprint
from ..constants import _MINER_VERSIONS, GET, POST
from ..supports import JSONRequired
from flask import make_response, jsonify, request


RS_API = RSBlueprint("RNOStatistics API", __name__, prefix="/api/")


@RS_API.route("/check", methods=POST)
@JSONRequired
def RS_API_VersionCheck():
    return "Y"
