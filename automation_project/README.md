# Mini Network Automation Project

Purpose: read three Cisco devices from a JSON inventory, simulate availability,
display UP/DOWN results, and save output.json. This exercise uses simulation,
not ping, RESTCONF, or actual network reachability.

## Usage
Requires Python 3. Run `python network_check.py` from this directory.
Paths are relative to the script, so running it from another directory also works.
Edit inventory.json to change hostname, management_ip, device_type, location,
and simulated_status (UP or DOWN). Invalid device entries are recorded as DOWN
with an error reason. Invalid JSON, missing files, fewer than three devices,
and output write errors produce an error and exit code 1.

## Git
This supplied folder is already initialized and committed. Inspect with
`git status` and `git log --oneline`. After your own changes, run:
```
git add inventory.json network_check.py README.md output.json
git commit -m "Update network inventory and check results"
```
