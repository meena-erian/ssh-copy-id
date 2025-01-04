# ssh-copy-id

A Windows-friendly replication of the Linux `ssh-copy-id` CLI.

## About

On Linux, `ssh-copy-id` is a convenient command for installing your public key on a remote machine. This tool fills that gap on Windows. It's not as extensive as the original Linux command, but it uses a very similar syntax and is sufficient for most basic use cases.

## Prerequisites

- **Windows** (Windows 7/8/10/11) with:
  - Python 3.6+ installed  
  - OpenSSH client (either installed via Windows Features on Windows 10+ or other methods like Git for Windows)
  - PowerShell (typically included on Windows 7+; if not, install it)

## Installation

```sh
pip install sshcopyid
```

This installs the command-line tool `ssh-copy-id` into your Python scripts directory (often at `C:\Users\<USERNAME>\AppData\Local\Programs\Python\PythonXX\Scripts\` on Windows).

## Usage

```
usage: ssh-copy-id [-h] [-p PORT] [-i PUB_KEY_PATH] target

Copy the current user's SSH public key to a remote machine.
(This CLI is intended for use under Windows only.)

positional arguments:
  target                username@host (The username and hostname/IP of the remote host)

optional arguments:
  -h, --help            Show help message and exit
  -p PORT, --port PORT  The SSH port number of the remote machine (default: 22)
  -i PUB_KEY_PATH, --identity-file PUB_KEY_PATH
                        Path to the public key file to copy (default: %USERPROFILE%\.ssh\id_rsa.pub)
```

### Example

```sh
# Copy your default key to a remote host on port 22
ssh-copy-id myuser@192.168.1.100

# Specify a custom port (e.g., 2200)
ssh-copy-id -p 2200 myuser@192.168.1.100

# Specify a custom public key file
ssh-copy-id -i C:\Users\myuser\.ssh\id_ed25519.pub myuser@myserver.com
```

When it succeeds, you'll be able to SSH into the remote host without entering your password, just like the original `ssh-copy-id`.

## Contributing

1. Fork the project and clone locally.  
2. Create a new branch for your work.  
3. Commit and push to your repository.  
4. Create a pull request in GitHub.  

Improvements and PRs are always welcome!

## How to Build and Publish a New Version (for maintainers)

1. **Update the version number** in `setup.py` (e.g., `version='0.0.7'`).
2. **Ensure you have the necessary tools** installed:
   ```sh
   pip install setuptools wheel twine
   ```
3. **Build your distribution**:
   ```sh
   # From the top-level project directory (where setup.py is located):
   python setup.py sdist bdist_wheel
   ```
   This command creates a `dist/` folder containing `.tar.gz` and `.whl` files.
4. **(Optional) Test your package on TestPyPI**:
   ```sh
   twine upload --repository-url https://test.pypi.org/legacy/ dist/*
   ```
   Then install from TestPyPI to verify everything works:
   ```sh
   pip install --index-url https://test.pypi.org/simple/ sshcopyid
   ```
5. **Upload to the real PyPI**:
   ```sh
   twine upload dist/*
   ```
6. **Confirm installation** from PyPI:
   ```sh
   pip install --upgrade sshcopyid
   ```

That’s it! The new version is now available on PyPI. Users can `pip install sshcopyid` and get your latest fixes and features.
