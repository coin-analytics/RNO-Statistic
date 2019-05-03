from ..blueprint import RSBlueprint
from ..constants import _MINER_VERSIONS, GET, POST
from ..supports import FormDataRequired
from ..reports import SuccessResponse, FailureResponse
from flask import make_response, jsonify, request


RS_API = RSBlueprint("RNOStatistics API", __name__, prefix="/api/")


@RS_API.route("/check", methods=POST)
@FormDataRequired("version")
def RS_API_VersionCheck():
    version = request.form.get("version")

    if version in _MINER_VERSIONS:
        if version != _MINER_VERSIONS[-1]:
            return FailureResponse(
                message="업데이트가 필요합니다. 확인을 누르면 사이트로 이동합니다."
            ).make_response()
        else:
            return SuccessResponse().make_response()

    return FailureResponse(
        message="유효하지 않은 마이너 버전입니다."
    ).make_response()

