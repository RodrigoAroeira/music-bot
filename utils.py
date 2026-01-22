import re

_TITLE_NOISE = re.compile(
    r"\s*[\(\[].*?(remaster|live|edit|version|explicit).*?[\)\]]",
    re.IGNORECASE,
)
_SPOTIFY_TRACK_RE = re.compile(r"open\.spotify\.com/track/([a-zA-Z0-9]+)")


def normalize_title(title: str) -> str:
    title = title.lower()
    title = _TITLE_NOISE.sub("", title)
    title = re.sub(r"[^\w\s]", "", title)
    return re.sub(r"\s+", " ", title).strip()


_FEAT = re.compile(r"\b(feat|ft)\.? .*$", re.IGNORECASE)


def normalize_artist(artist: str) -> str:
    artist = artist.lower()
    artist = _FEAT.sub("", artist)
    return artist.strip()


def extract_spotify_track_id(url: str) -> str | None:
    m = _SPOTIFY_TRACK_RE.search(url)
    if not m:
        return None
    return m.group(1)
