"""Task 1: list and dictionary based Cisco device inventory."""
devices = [
    {"hostname": "R1", "management_ip": "192.0.2.1", "device_type": "Cisco IOS XE router", "location": "Makati", "status": "up"},
    {"hostname": "SW1", "management_ip": "192.0.2.2", "device_type": "Cisco Catalyst switch", "location": "Intramuros", "status": "up"},
    {"hostname": "R2", "management_ip": "192.0.2.3", "device_type": "Cisco IOS XE router", "location": "Bulacan", "status": "down"},
]
def display(items):
    print(f"{'Hostname':<10} {'Management IP':<16} {'Device type':<24} {'Location':<12} Status")
    print('-' * 80)
    for d in items:
        print(f"{d['hostname']:<10} {d['management_ip']:<16} {d['device_type']:<24} {d['location']:<12} {d['status'].upper()}")
def main():
    print('ALL DEVICES')
    display(devices)
    operational = [d for d in devices if d['status'].lower() == 'up']
    print('\nUP DEVICES')
    display(operational)
    print(f"\nOperational devices: {len(operational)} / {len(devices)}")
if __name__ == '__main__':
    main()
