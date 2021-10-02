from argparse import ArgumentParser
import sys
import os

class SafeParser(ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

def main():
    parser = SafeParser(
        description='Copy current user\'s ssh keys to a remote machine',
        add_help=False
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-h','-?', help="print this help",  action='help')
    # group.add_argument(
    #     '-f',
    #     help="force mode -- copy keys without trying to check if they are already installed",
    #     action="store_true"
    # )
    # group.add_argument(
    #     '-n', 
    #     help="dry run    -- no keys are actually copied",
    #     action="store_true"
    # )
    parser.add_argument(dest='target',
        help="username@host, The username and hostname/ip of the remote host"
    )
    #parser.add_argument('-i', dest='[identity_file]')
    parser.add_argument('-p', dest='port')
    #parser.add_argument('-F', dest='alternative ssh_config file')
    args = parser.parse_args()
    cmd = 'type $env:USERPROFILE\.ssh\id_rsa.pub | ssh '
    sshcmd = 'ssh ' + args.target
    if args.port:
        cmd += '-p ' + str(args.port) + ' '
        sshcmd += '-p ' + str(args.port)
    if args.target:
        cmd += args.target
    else:
        parser.print_help()
    cmd += " 'cat >> .ssh/authorized_keys'"
    cmd = "powershell -Command \"" + cmd + "\""
    os.system(cmd)
    print("Done\nNow try " + sshcmd + " to verify that it no longer asks you for the password")


if __name__ == '__main__':
    main()
