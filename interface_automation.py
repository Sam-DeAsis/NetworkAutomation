"""Task 3: PUT Loopback100, then GET and compare its configuration."""
import sys
import requests
from restconf_common import connection

EXPECTED = {
    'name': 'Loopback100',
    'description': 'RESTCONF practical quiz',
    'type': 'iana-if-type:softwareLoopback',
    'enabled': True,
    'ietf-ip:ipv4': {'address': [{'ip': '192.0.2.100', 'netmask': '255.255.255.255'}]},
}
PAYLOAD = {'ietf-interfaces:interface': EXPECTED}

def matches(actual):
    addresses = actual.get('ietf-ip:ipv4', {}).get('address', [])
    ip_matches = any(a.get('ip') == '192.0.2.100' and
                     (a.get('netmask') == '255.255.255.255' or a.get('prefix-length') == 32)
                     for a in addresses)
    return (all(actual.get(k, True if k == 'enabled' else None) == EXPECTED[k]
                for k in ('name', 'description', 'type', 'enabled')) and ip_matches)

def main():
    try:
        session, base = connection()
        url = base + '/interface=Loopback100'
        with session:
            response = session.put(url, json=PAYLOAD, timeout=(10, 30))
            print(f'PUT HTTP status code: {response.status_code}')
            response.raise_for_status()
            if response.status_code not in (200, 201, 204):
                raise ValueError('Unexpected PUT status; configuration not confirmed.')
            print('Configuration request succeeded.')
            verification = session.get(url, timeout=(10, 30))
            print(f'GET HTTP status code: {verification.status_code}')
            verification.raise_for_status()
            actual = verification.json()['ietf-interfaces:interface']
            if not matches(actual):
                raise ValueError('Retrieved Loopback100 does not match the expected configuration.')
            print('Verification PASSED: Loopback100, enabled=True, 192.0.2.100/32')
            print('Description: ' + actual['description'])
        return 0
    except requests.RequestException as exc:
        print(f'Configuration/verification failed: {type(exc).__name__}')
    except (ValueError, KeyError, TypeError) as exc:
        print(f'Configuration/verification failed: {exc}')
    return 1
if __name__ == '__main__':
    sys.exit(main())
