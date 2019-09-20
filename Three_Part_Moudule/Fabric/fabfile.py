from fabric import task

@task
def upload_and_mv(c):
    if c.run('ls', warn=True):
        c.put('./fabric_test.py', remote='/home/nb201/')
        c.run('cat /home/nb201/fabric_test.py')
