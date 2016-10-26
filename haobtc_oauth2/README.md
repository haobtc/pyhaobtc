# py-oauth2


## Installation

```

pip install haobtc-oauth2

```

## Usage

```

from pyoauth2 import Client

client = Client(client_id, client_secret)

authorize_url = client.auth_code.authorize_url()
# or use
# REDIRECT_URL = 'http://localhost:3000'
# authorize_url = client.auth_code.authorize_url(redirect_uri=REDIRECT_URL)
print authorize_url

token = client.auth_code.get_token(code)
print token
user_info = client.auth_code.get_resource()
print user_info

```

## oauth 全局返回码说明

| 返回码     | 返回说明   |
| ----------| -------- |
| 0         | 请求成功  |
| 40001     | 缺少参数|
| 40002     | 非法client_id |
| 40003     | 请求地址未注册 |
| 40004     | 错误的 grant_type |
| 40005     | 错误的 response_type |
| 40006     | redirect_uri不匹配 |
| 40007     | client_secret不匹配 |
| 40008     | access_token 不存在或者已过期 |
| 40009     | authorization_code 不存在或已过期 |
| 40010     | refresh_token 不存在或已过期 |
| 40011     | invalid_user 用户不存在或者已被删除|
| 40012     | invalid_credencial 未授权|
| 40013     | invalid_request_scheme 错误的请求协议|
| 40014     | invalid_request_method 错误的请求方法|

## License

MIT

## Reference

https://github.com/liluo/py-oauth2

## Submitting a Pull Request
* Fork the repository.
* Create a topic branch.
* Implement your feature or bug fix.
* Add, commit, and push your changes.
* Submit a pull request.
