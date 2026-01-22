from typing import Literal, Optional, TypedDict


class ExternalUrls(TypedDict):
    spotify: str


class Artist(TypedDict):
    external_urls: ExternalUrls | None
    href: str
    id: str
    name: str
    type: Literal["artist"]
    uri: str


class Image(TypedDict):
    url: str
    width: int
    height: int


class Album(TypedDict):
    album_type: Literal["album"]
    artists: list[Artist]
    available_markets: list[str]
    external_urls: ExternalUrls
    href: str
    id: str
    images: list[Image]
    name: str
    release_date: str | None
    release_date_precision: Literal["day", "month", "year"]
    total_tracks: int
    type: Literal["album"]
    uri: str


class ExternalIds(TypedDict):
    isrc: str | None


class TrackJson(TypedDict):
    album: Album
    artists: list[Artist]
    available_markets: list[str]
    disc_number: int
    duration_ms: int
    explicit: bool
    external_ids: ExternalIds
    external_urls: ExternalUrls
    href: str
    id: str
    is_local: bool
    name: str
    popularity: int
    preview_url: Optional[str]
    track_number: int
    type: Literal["track"]
    uri: str
