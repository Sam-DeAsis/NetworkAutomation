# Python Network Automation Practical Quiz

Four Cisco network automation exercises for ITS 163-1L.

## Files
- `network_inventory.py`: three Cisco devices as a list of dictionaries; displays all devices, UP devices and operational count.
- `restconf_monitor.py`: HTTPS RESTCONF GET of `/restconf/data/ietf-interfaces:interfaces`, interface names, enabled status, HTTP code and error handling.
- `interface_automation.py`: PUT Loopback100 then GET and compare its configuration; address 192.0.2.100/32, enabled true.
- `restconf_common.py`: shared connection settings used by both RESTCONF scripts; keep this file beside them.
- `automation_project/`: JSON inventory, simulated checks, saved output and usage documentation.

## Quick start
```sh
python -m pip install -r requirements.txt
python network_inventory.py
python automation_project/network_check.py
```
See `RUN_ME.md` for Cisco Sandbox connection settings and RESTCONF execution.
Supply your own Sandbox reservation host, port and credentials through environment variables.
Do not commit credentials. Use a writable lab reservation for configuration.

## Validation status
Inventory and mini-project simulation ran locally. RESTCONF success and failure
paths were checked with mocked responses; live Sandbox execution remains pending.
The enabled flag is administrative configuration, not measured operational state.
The mini project uses simulation, which is permitted by Task 4.

## Git
All exercise files are committed together at the repository root. The
`automation_project` directory is part of this repository, so its files are
tracked without a nested repository or submodule.
