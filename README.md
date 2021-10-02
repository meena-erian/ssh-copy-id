# ssh-copy-id

Simplified replication of the linux ssh-copy-id cli for windows

## About 

Since the CLI ssh-copy-id is missing when you're using a windows OS as the SSH client,
This package is meant as a simple alternative. It's not as extensive as the original linux based shell
command but it works as a simple alternative and uses pretty much the same syntax

## Setup

On a windows OS, make sure you have python3 installed, and then install `sshcopyid` using `pip`

```
pip install sshcopyid
```

## Syntax
```
usage: ssh-copy-id [-h] [-p PORT] target

Copy current user's ssh keys to a remote machine. 
(This CLI is meant for use only under the windows platform)

positional arguments:
  target   username@host, The username and hostname/ip of the remote host

optional arguments:
  -h, -?   print this help
  -p PORT  The ssh port number of the remote machine
```

## Contributing

- Fork the project and clone locally.
- Create a new branch for what you're going to work on.
- Push to your origin repository.
- Create a new pull request in GitHub.
