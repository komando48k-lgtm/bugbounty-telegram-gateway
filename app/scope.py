import re

_HOST = re.compile(r"^(?=.{1,253}$)(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,63}$", re.I)

def normalize_host(value: str) -> str:
    value = value.strip().lower().rstrip(".")
    if value.startswith("https://"): value = value[8:]
    elif value.startswith("http://"): value = value[7:]
    value = value.split("/", 1)[0].split(":", 1)[0]
    if not _HOST.fullmatch(value): raise ValueError("Use a hostname such as example.com")
    return value

def require_in_scope(db, host: str) -> str:
    host = normalize_host(host)
    if not db.in_scope(host): raise ValueError("Target is not registered in the local authorized scope")
    return host
