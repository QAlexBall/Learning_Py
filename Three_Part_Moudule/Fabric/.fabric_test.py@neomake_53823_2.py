from fabric import SerialGroup, Connection

nb201 = 'nb201@192.168.13.201'

result = SerialGroup(nb201).run('hostname')
print(result)


def disk_free(c):
    uname = c.run('uname -s', hide=True)
    if 'Linux' in uname.stdout:
        command = "df -h"
        return c.run(command, hide=True).stdout.strip()
    print("error")
    err = "No idea how to get disk spce on {}!".format(uname)
    #  raise Exit(err)
    print('error')

print(disk_free(Connection(nb201)))


# superuser privileges via auto-response
from invoke import Responder
def superuser_privileges():
    c = Connection(nb201)
    sudopass = Responder(
        pattern=r'\[sudo\] password:',
        response='mypassword\n',
    )
    c.run('sudo whoami', pty=True, watchers=[sudopass])


# The sudo helper
import getpass
from fabric import Config

def user_sudo():
    sudo_pass = getpass.getpass("What's your sudo password?")
    config = Config(overrides={'sudo': {'password': sudo_pass}})
    c = Connection(nb201, config=config)
    c.sudo('whoami', hide='stderr')

# Transfer files
def transfer_files():
    result = Connection(nb201).put('./fabric_test.py', remote='/home/nb201/')
    print("Uploaded {0.local} to {0.remote}".format(result))

# Multiple actions
c = Connection(nb201)
def upload_and_mv():
    c.put('./fabric_test.py', remote='/home/nb201/')
    c.run('mv /home/nb201/fabric_test.py /home/nb201/a.py')

# bring it all together
from fabric import SerialGroup as Group
def use_pool():
    pool = Group(nb201, 'me@127.0.0.1')
    pool.put('./fabric_test.py', remote='/home/nb201/')  # ???
    pool.run('mv /home/nb201/fabric_test.py /home/nb201/a.py')



