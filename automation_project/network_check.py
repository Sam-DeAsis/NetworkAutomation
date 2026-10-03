"""Task 4: deterministic simulated Cisco network checks."""
import json
import ipaddress
import sys
from pathlib import Path
BASE = Path(__file__).resolve().parent

def main():
    try:
        devices = json.loads((BASE / 'inventory.json').read_text())
        if not isinstance(devices, list) or len(devices) < 3:
            raise ValueError('Inventory must be a list containing at least three devices.')
    except (OSError, ValueError) as exc:
        print(f'Cannot read inventory: {exc}')
        return 1
    results = []
    print('SIMULATED NETWORK CHECK — no live connections')
    for device in devices:
        result = {'hostname': 'UNKNOWN', 'management_ip': '', 'status': 'DOWN', 'mode': 'simulation'}
        try:
            if not isinstance(device, dict):
                raise ValueError('Device must be a dictionary.')
            result.update(hostname=device.get('hostname', 'UNKNOWN'), management_ip=device.get('management_ip', ''))
            for field in ('hostname', 'management_ip', 'device_type', 'location'):
                if not isinstance(device.get(field), str) or not device[field].strip():
                    raise ValueError(f'Missing or invalid {field}.')
            ipaddress.ip_address(device['management_ip'])
            status = device.get('simulated_status', '').upper()
            if status not in ('UP', 'DOWN'):
                raise ValueError('simulated_status must be UP or DOWN.')
            result['status'] = status
            result['reason'] = 'Configured simulation result'
        except (ValueError, TypeError, AttributeError) as exc:
            result['reason'] = str(exc)
        results.append(result)
        print(f"{result['hostname']:<10} {result['management_ip']:<16} {result['status']} ({result['reason']})")
    try:
        (BASE / 'output.json').write_text(json.dumps(results, indent=2) + '\n')
    except OSError as exc:
        print(f'Cannot save output: {exc}')
        return 1
    print(f"Operational devices: {sum(r['status'] == 'UP' for r in results)} / {len(results)}")
    print('Saved results to output.json')
    return 0
if __name__ == '__main__':
    sys.exit(main())
