from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING
from utils import normalize_artist, normalize_title


if TYPE_CHECKING:
    from spot_types import TrackJson


@dataclass(frozen=True, slots=True)
class Track:
    title: str
    artists: tuple[str, ...]
    duration_ms: int
    isrc: str | None = None
    album: str | None = None
    disc_num: int | None = None
    track_num: int | None = None
    release_year: int | None = None

    @staticmethod
    def from_spotify_json(track: TrackJson) -> Track:
        artists = tuple(normalize_artist(a["name"]) for a in track["artists"])
        album = track["album"]["name"].lower()

        release_year = None
        release_date = track["album"].get("release_date")
        if release_date:
            release_year = int(release_date[:4])

        return Track(
            title=normalize_title(track["name"]),
            artists=artists,
            duration_ms=track["duration_ms"],
            isrc=track["external_ids"].get("isrc"),
            album=album,
            disc_num=track.get("disc_number"),
            track_num=track.get("track_number"),
            release_year=release_year,
        )
