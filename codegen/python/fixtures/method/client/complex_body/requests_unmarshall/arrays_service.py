
from .Animal import Animal
from .api_response import APIResponse
from .unhandled_api_error import UnhandledAPIError
from .unmarshall_error import UnmarshallError


class ArraysService:
    def __init__(self, client):
        self.client = client

    def arrays_post(self, data, headers=None, query_params=None, content_type="application/json"):
        """
        handle array
        It is method for POST /arrays
        """
        uri = self.client.base_url + "/arrays"
        resp = self.client.post(uri, data, headers, query_params, content_type)
        try:
            if resp.status_code == 201:
                resps = []
                for elem in resp.json():
                    resps.append(Animal(elem))
                return APIResponse(data=resps, response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def arrays_put(self, data, headers=None, query_params=None, content_type="application/json"):
        """
        another form of array
        It is method for PUT /arrays
        """
        uri = self.client.base_url + "/arrays"
        resp = self.client.put(uri, data, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                resps = []
                for elem in resp.json():
                    resps.append(Animal(elem))
                return APIResponse(data=resps, response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)
