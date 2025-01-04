import sys
import os
import subprocess
from argparse import ArgumentParser
from shutil import which

class SafeParser(ArgumentParser):
    def error(self, message):
        self._print_message(f'error: {message}\n', sys.stderr)
        self.print_help(sys.stderr)
        sys.exit(2)

def main():
    # Check if running on Windows
    if not sys.platform.startswith('win'):
        sys.stderr.write(
            "Warning: This tool is designed for Windows. Use on non-Windows at your own risk.\n\n"
        )

    parser = SafeParser(
        description=(
            "Copy the current user's SSH public key to a remote machine.\n"
            "Intended for Windows to replicate ssh-copy-id-like functionality."
        ),
        add_help=False
    )

    # Mutually exclusive group for help
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-h', '--help', action='help', help="Show help message and exit.")

    parser.add_argument(
        'target',
        help="username@host (The username and hostname/IP of the remote host)"
    )
    parser.add_argument(
        '-p', '--port',
        dest='port',
        help="The SSH port number on the remote machine (default is 22)."
    )
    parser.add_argument(
        '-i', '--identity-file',
        dest='pub_key_path',
        default=os.path.join(os.environ.get('USERPROFILE', ''), '.ssh', 'id_rsa.pub'),
        help=(
            "Path to the public key file to copy "
            "(default: %(default)s). Use if your key is named differently."
        )
    )

    args = parser.parse_args()

    # Ensure SSH is installed
    if which("ssh") is None:
        sys.stderr.write(
            "error: 'ssh' command not found on this system. Please install/enable OpenSSH.\n"
        )
        sys.exit(1)

    # Make sure the specified public key file exists
    if not os.path.exists(args.pub_key_path):
        sys.stderr.write(
            f"error: The specified public key file does not exist: {args.pub_key_path}\n"
        )
        sys.exit(1)

    # Build an SSH command string for user reference
    ssh_cmd_list = ["ssh"]
    if args.port:
        ssh_cmd_list.extend(["-p", str(args.port)])
    ssh_cmd_list.append(args.target)
    ssh_cmd_str = " ".join(ssh_cmd_list)

    # Build the actual PowerShell command that pipes the key
    # On many Windows versions, 'powershell.exe' is recognized as 'powershell'
    powershell_cmd = f"type {args.pub_key_path} | ssh "
    if args.port:
        powershell_cmd += f"-p {args.port} "
    powershell_cmd += (
        f"{args.target} "
        "'mkdir -p .ssh && touch .ssh/authorized_keys && cat >> .ssh/authorized_keys'"
    )

    # Full command to execute
    # On some systems, you might need to specify 'powershell.exe' or add '-ExecutionPolicy Bypass'
    full_cmd = ["powershell", "-Command", powershell_cmd]
    # full_cmd = ["powershell.exe", "-ExecutionPolicy", "Bypass", "-Command", powershell_cmd]

    print(f"Copying public key: {args.pub_key_path}")
    print(f"To remote host: {args.target}")
    try:
        subprocess.check_call(full_cmd)
        print("Key copied successfully!")
    except subprocess.CalledProcessError as exc:
        sys.stderr.write("error: Failed to copy the key to the remote machine.\n")
        sys.exit(exc.returncode)

    print(f"\nNow try running:\n  {ssh_cmd_str}\n")
    print("If successful, it will no longer prompt for a password.")
