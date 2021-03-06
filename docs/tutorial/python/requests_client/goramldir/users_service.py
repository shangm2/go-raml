# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.


class UsersService:
    def __init__(self, client):
        self.client = client

    def users_byUsername_get(self, username, headers=None, query_params=None, content_type="application/json"):
        """
        Get information on a specific user
        It is method for GET /users/{username}
        """
        uri = self.client.base_url + "/users/" + username
        return self.client.get(uri, None, headers, query_params, content_type)

    def users_get(self, headers=None, query_params=None, content_type="application/json"):
        """
        Get list of all developers
        It is method for GET /users
        """
        uri = self.client.base_url + "/users"
        return self.client.get(uri, None, headers, query_params, content_type)

    def users_post(self, data, headers=None, query_params=None, content_type="application/json"):
        """
        Add user
        It is method for POST /users
        """
        uri = self.client.base_url + "/users"
        return self.client.post(uri, data, headers, query_params, content_type)
