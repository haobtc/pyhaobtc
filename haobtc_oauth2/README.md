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
