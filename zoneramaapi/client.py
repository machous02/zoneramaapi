from hashlib import sha256

from zoneramaapi.zeep.sync import ZeepSyncClients


class ZoneramaClient:
    _zeep: ZeepSyncClients
    logged_in_as: int | None

    def __init__(self):
        self._zeep = ZeepSyncClients()

    def __enter__(self):
        self._zeep.__enter__()
        return self

    def __exit__(self, *_):
        self.close()
        return

    def close(self):
        self._zeep.close()
        if self.logged_in:
            self.logout()

    def login(self, username: str, password: str) -> bool:
        service = self._zeep.api.service
        response = service.Login(username, sha256(bytes(password, "utf-8")).hexdigest())
        self.logged_in_as = response.Result if response.Success else None
        return response.Success

    def logout(self) -> bool:
        if not self.logged_in:
            return False

        service = self._zeep.api.service
        response = service.Logout()

        if response.Success:
            self.logged_in_as = None

        return response.Success

    @property
    def logged_in(self) -> bool:
        return self.logged_in_as is not None
