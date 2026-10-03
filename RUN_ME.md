# Run and capture the lab

1. Install Python 3 and Git. In this folder, run `python -m pip install -r requirements.txt`.
2. Run `python network_inventory.py` and capture its terminal output.
3. Reserve a writable Cisco IOS XE DevNet Sandbox supporting ietf-interfaces and ietf-ip.
   Use the host, HTTPS port, username, password and VPN directions supplied by your reservation.
   No current Sandbox endpoint or credentials are hardcoded in this package.
4. Set the environment variables below using your actual connection details.
   In PowerShell:
```
$env:RESTCONF_BASE_URL = "https://YOUR_SANDBOX_HOST:443"
$env:RESTCONF_USERNAME = "YOUR_USERNAME"
$env:RESTCONF_PASSWORD = Read-Host "Sandbox password"
python restconf_monitor.py
python interface_automation.py
```
   For a trusted lab CA, set RESTCONF_CA_BUNDLE to its PEM file path. If the
   Sandbox uses a self-signed certificate and no CA is available, the lab-only
   option is `$env:RESTCONF_INSECURE = "1"`; the script prints a warning.
5. Capture monitor output with HTTP code and interface enabled values. Enabled
   is administrative configuration; it does not prove link operational status.
6. Capture automation output showing PUT status, GET status and verification.
   PUT replaces Loopback100 configuration if it already exists. Use your writable
   lab reservation and check for conflicting use first. The chosen address is
   192.0.2.100/32, description RESTCONF practical quiz, enabled true.
7. Run `python automation_project/network_check.py`. Capture its output,
   inventory.json and output.json, then capture `git -C automation_project log --oneline`
   and `git -C automation_project status`.
8. Add the live screenshots to the report and complete section and dates before
   submitting. The supplied report labels Tasks 2 and 3 as live execution pending.
   Local output images are rendered captures of genuine saved stdout, not GUI screenshots.

The ZIP includes the project .git directory and its commit. Extract all files,
including hidden files, to retain the repository. No passwords are committed.
