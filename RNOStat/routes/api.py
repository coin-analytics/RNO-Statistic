from ..blueprint import RSBlueprint
from ..constants import _MINER_VERSIONS, GET, POST
from ..supports import FormDataRequired
from ..reports import SuccessResponse, FailureResponse
from flask import request, current_app
from random import choice
from string import ascii_letters, digits, punctuation
from traceback import format_exc


def randomString(stringLength=7):
    letters = ascii_letters   \
              + ascii_letters \
              + ascii_letters \
              + digits        \
              + punctuation[:5]
    return ''.join(choice(letters) for i in range(stringLength))


RS_API = RSBlueprint("RNOStatistics API", __name__, prefix="/api/")


@RS_API.errorhandler(500)
def RS_InternalErrorHandler(ex):
    randCode = randomString(12)

    open("{}/logs/{}.log".format(current_app.base_directory, randCode)).write(
        format_exc(ex)
    )

    return FailureResponse(
        code=9001,
        message=f"시스템 처리 중 오류가 발생하였습니다. 오류코드는 `{randCode}` 이며, 지속적인 오류 발생"
        f"시 c01n.4n4lyt1cs@gmail.com에 제보해주시기 바랍니다."
    )


@RS_API.route("/check", methods=POST)
@FormDataRequired("version")
def RS_API_VersionCheck():
    version = request.form.get("version")

    if version in _MINER_VERSIONS:
        if version != _MINER_VERSIONS[-1]:
            return FailureResponse(
                code=2001,
                message="업데이트가 필요합니다. 확인을 누르면 사이트로 이동합니다."
            ).make_response()
        else:
            return SuccessResponse().make_response()

    return FailureResponse(
        code=2002,
        message="유효하지 않은 마이너 버전입니다."
    ).make_response()


@RS_API.route("/report", methods=GET)
def RS_API_ReportPing():
    isLogging = current_app.custom_config.get("logging")

    if isLogging:
        return SuccessResponse().make_response()

    return FailureResponse(
        code=2100,
        message="로그 수집이 일시 중단되었습니다."
    ).make_response()


@RS_API.route("/report/kick", methods=POST)
@FormDataRequired("wallet", "weight", "archi", "hertz", "threads")
def RS_ReportKick():
    wallet  = request.form.get("wallet")
    weight  = request.form.get("weight")
    archi   = request.form.get("archi")
    hertz   = request.form.get("hertz")
    threads = request.form.get("threads")

    Log = current_app.models.KickLog(
        wallet,
        weight,
        archi,
        hertz,
        threads
    )

    current_app.db.session.add(Log)
    current_app.db.session.commit()

    return SuccessResponse().make_response()
