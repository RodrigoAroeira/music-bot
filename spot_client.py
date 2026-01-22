from __future__ import annotations
import base64
import time
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

import requests

if TYPE_CHECKING:
    from spot_types import TrackJson


@dataclass
class SpotifyClient:
    client_id: str
    client_secret: str
    __access_token: str | None = field(init=False, default=None)
    __expires_at: float = field(init=False, default=0)

    def get_track(self, track_id: str) -> TrackJson:
        resp = requests.get(
            f"https://api.spotify.com/v1/tracks/{track_id}",
            headers=self.__headers(),
            timeout=10,
        )
        resp.raise_for_status()
        return resp.json()

    def get_album(self, album_id: str) -> dict:
        _ = album_id
        raise NotImplementedError("get_album was not yet implemented")

    def __auth_header(self) -> dict[str, str]:
        creds = f"{self.client_id}:{self.client_secret}"
        encoded = base64.b64encode(creds.encode()).decode()
        return {"Authorization": f"Basic {encoded}"}

    def __ensure_token(self) -> None:
        if self.__access_token and time.time() < self.__expires_at:
            return

        resp = requests.post(
            "https://accounts.spotify.com/api/token",
            headers=self.__auth_header(),
            data={"grant_type": "client_credentials"},
            timeout=10,
        )
        resp.raise_for_status()
        data = resp.json()

        self.__access_token = data["access_token"]
        self.__expires_at = data["expires_in"] - 30

    def __headers(self) -> dict[str, str]:
        self.__ensure_token()
        return {"Authorization": f"Bearer {self.__access_token}"}
