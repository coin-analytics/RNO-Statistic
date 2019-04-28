# RNOMiner API Document

## On Version Check
> POST /ap/check

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
  "status": -1,
  "message": "업데이트가 필요합니다. 확인을 누르면 사이트로 이동합니다."
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
  "message": "None"
}
```

- Example 2 (No Logging)
```json
{
  "status": -1,
  "message": "로그 수집이 일시 중단되었습니다."
}
```

## On Login
> POST /api/report/kick

### / Request
- POST Payload

    | Name | Type | Content | Example |
    |:----:|:----:|:-------:|:--------|
    | wallet | String | 로그인된 마이닝 지갑주소 |  |
    | weight | Float | 지갑계정의 가중치 | 1.5 |
    | archi | String | CPU 이름 | i7-7500U |
    | hertz | Float | CPU 동작속도 | 2.70Ghz |
    
### / Response
None

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
