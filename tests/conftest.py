import pytest
from unittest.mock import Mock

class DummyResponse:
    def __init__(self, success=True, result=None):
        self.Success = success
        self.Result = result

@pytest.fixture
def zeep_service():
    service = Mock()
    service.Login = Mock()
    service.Logout = Mock()
    return service

@pytest.fixture
def zeep_clients(zeep_service):
    api = Mock()
    api.service = zeep_service

    data = Mock()
    data.service = Mock()

    zeep = Mock()
    zeep.api = api
    zeep.data = data
    zeep.close = Mock()
    zeep.__enter__ = Mock(return_value=zeep)
    zeep.__exit__ = Mock(return_value=None)

    return zeep
