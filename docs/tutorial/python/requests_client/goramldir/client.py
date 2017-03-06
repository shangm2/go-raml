import requests

from .users_service import  UsersService 


class Client:
    def __init__(self, base_uri = "http://localhost:5000"):
        self.base_url = base_uri
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})
        
        self.users = UsersService(self)
    
    def set_auth_header(self, val):
        ''' set authorization header value'''
        self.session.headers.update({"Authorization":val})

    def get(self, uri, headers, params):
        res = self.session.get(uri, headers=headers, params=params)
        res.raise_for_status()
        return res

    def post(self, uri, data, headers, params):
        if type(data) is str:
            res = self.session.post(uri, data=data, headers=headers, params=params)
        else:
            res = self.session.post(uri, json=data, headers=headers, params=params)
        res.raise_for_status()
        return res

    def put(self, uri, data, headers, params):
        if type(data) is str:
            res = self.session.put(uri, data=data, headers=headers, params=params)
        else:
            res = self.session.put(uri, json=data, headers=headers, params=params)
        res.raise_for_status()
        return res

    def patch(self, uri, data, headers, params):
        if type(data) is str:
            res = self.session.patch(uri, data=data, headers=headers, params=params)
        else:
            res = self.session.patch(uri, json=data, headers=headers, params=params)
        res.raise_for_status()
        return res