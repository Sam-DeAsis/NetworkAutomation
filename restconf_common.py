"""Shared HTTPS configuration; credentials come from environment variables."""
import os
from urllib.parse import urlparse
import requests

def connection():
    base = os.environ.get('RESTCONF_BASE_URL', '').rstrip('/')
    username = os.environ.get('RESTCONF_USERNAME', '')
    password = os.environ.get('RESTCONF_PASSWORD', '')
    parsed = urlparse(base)
    if parsed.scheme != 'https' or not parsed.hostname or parsed.path not in ('', '/') or parsed.username or parsed.query or parsed.fragment:
        raise ValueError('Set RESTCONF_BASE_URL to https://SANDBOX_HOST:PORT (no path).')
    if not username or not password:
        raise ValueError('Set RESTCONF_USERNAME and RESTCONF_PASSWORD from your Sandbox reservation.')
    session = requests.Session()
    session.auth = (username, password)
    session.headers.update({'Accept': 'application/yang-data+json', 'Content-Type': 'application/yang-data+json'})
    session.verify = os.environ.get('RESTCONF_CA_BUNDLE') or True
    if os.environ.get('RESTCONF_INSECURE') == '1':
        print('WARNING: TLS certificate verification disabled for the lab.')
        session.verify = False
    return session, base + '/restconf/data/ietf-interfaces:interfaces'
