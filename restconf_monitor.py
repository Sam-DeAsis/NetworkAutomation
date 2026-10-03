"""Task 2: retrieve IOS XE interface configuration using RESTCONF."""
import sys
import requests
from restconf_common import connection

def main():
    try:
        session, url = connection()
        with session:
            response = session.get(url, timeout=(10, 30))
            print(f'HTTP status code: {response.status_code}')
            response.raise_for_status()
            interfaces = response.json()['ietf-interfaces:interfaces']['interface']
            if not isinstance(interfaces, list):
                raise ValueError('Interface data must be a list.')
            print(f"{'Interface':<28} Enabled (administrative)")
            for interface in interfaces:
                # enabled defaults to true in the IETF interface model.
                enabled = interface.get('enabled', True)
                print(f"{interface['name']:<28} {enabled}")
            print(f'Interfaces retrieved: {len(interfaces)}')
        return 0
    except requests.RequestException as exc:
        print(f'Connection/request failed: {type(exc).__name__}')
    except (ValueError, KeyError, TypeError) as exc:
        print(f'Configuration/response error: {exc}')
    return 1
if __name__ == '__main__':
    sys.exit(main())
