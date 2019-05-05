# RNOMiner API Document

## Functional Error
> 모든 API 처리 중 오류 발생 시, 다음 내용을 메시지박스로 출력

### Response
```json
{
  "status": 9001,
  "message": "시스템 처리 중 오류가 발생하였습니다. 오류코드는 `pENPbv3vnkrg` 이며, 지속적인 오류 발생 시 c01n.4n4lyt1cs@gmail.com에 제보해주시기 바랍니다."
}
```

## On Version Check
> POST /api/check

### / Request
- POST Payload

    | Name | Type | Content | Example |
    |:----:|:----:|:-------:|:--------|
    | version | String | 마이너 버전명 | 1.2-c4-2019042701 |

### / Response
- Example 1 (Up-to-date)
```json
{
  "status": 1,
  "message": null
}
```

- Example 2 (Update required)
```json
{
  "status": 2001,
  "message": "업데이트가 필요합니다. 확인을 누르면 사이트로 이동합니다."
}
```

- Example 3 (Unspecified version name)
```json
{
  "status": 2002,
  "message": "유효하지 않은 마이너 버전입니다."
}
```

## On Ping
> GET /api/report/

### / Request
None

### / Response
- Example 1  (Success)
```json
{
  "status": 1,
  "message": null
}
```

- Example 2 (No Logging)
```json
{
  "status": 2100,
  "message": "로그 수집이 일시 중단되었습니다."
}
```

## On Login
> POST /api/report/kick

### / Request
- POST Payload

    | Name | Type | Required | Content | Example |
    |:----:|:----:|:--------:|:-------:|:--------|
    | wallet | String | Required | 로그인된 마이닝 지갑주소 |  |
    | weight | Float | Required | 지갑계정의 가중치 | 1.5 |
    | archi | String | Optional | CPU 이름 | i7-7500U |
    | hertz | Float | Optional | CPU 동작속도 | 2.70Ghz |
    | threads | Integer | Required | 작동 스레드 수 | 4 |
    
### / Response
- Example 1 (Success)
```json
{
  "status": 1,
  "message": null
}
```

## On minedCoin
> POST /api/report/mined

### / Request
- POST Payload

    | Name | Type | Content | Example |
    |:----:|:----:|:-------:|:--------|
    | wallet | String | 로그인된 마이닝 지갑주소 |  |
    | weight | Float | 지갑계정의 가중치 | 1.5 |
    | cores | Integer | 채굴에 사용중인 코어 수 | 4 |
    | solve_time | Integer | 한 개 해시 해결에 걸린 시간(ms) | 3437 |
    | coin | Float | 채굴된 코인 개수 | 0.04234 |
    | hashString | String | Solve한 hashString | dV83sd93mD== |
    | nonce | Integer | 찾아낸 nonce 값 | 9385712 |
    | nBit | Integer | RNO 서버에서 주어진 nBit 값 | 4 |
    
### / Response
None
