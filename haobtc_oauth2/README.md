# py-oauth2


## Installation

```

pip install haobtc-oauth2

```

## Usage

### authorize_url

```python

from pyoauth2 import Client
params = { SITE_URL = 'https://haobtc.com',                 # optional 
           AUTHORIZE_URL = '/auth/oauth/authorize/',        # optional 
           TOKEN_URL = '/auth/settings/oauth/get_token/',   # optional   
           RESOURCE_URL = '/api/v1/user/profile'}           # optional 

client = Client(client_id, client_secret, params)

authorize_url = client.auth_code.authorize_url()

print authorize_url # https://haobtc.com/auth/oauth/authorize/?response_type=code&client_id=b3ca01d932e643faa32d

``` 

#### get acccess token 

```python

token = client.auth_code.get_token(code)
print token   # 04a889136a6c412aa658

```

> token is set expired at 7 days.


#### get user profile

```python 
user_info = client.get_user_profile({ 'access_token' : token })
print user_info
``` 

```python
{
    user_info: {
        privider: "haobtc",
        uuid: "604515dd07a74cff97cea1656dd462e1",
        raw_info: {
            username: "han",
            address: "18ojqY44LwUM9qm6iJtZHNHMVsiCRg1dDz"
        }
    },
    code: 0
}
```


## OAuth 全局返回码说明

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
| 40015     | oauth application blocked oauth 被禁用|

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
