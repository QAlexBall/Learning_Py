'''
假设开发一个安装向导,或者更常见的安转程序.
'''

class Wizard():

    def __init__(self, src, rootdir):
        self.choices = []
        self.rootdir = rootdir
        self.src = src
    
    def preferences(self, command):
        self.choices.append(command)
    
    def execute(self):
        for choice in self.choices:
            if list(choice.values())[0]:
                print("Copying binaries --", self.src, " ", choice, " to ", self.rootdir)
            else:
                print("No Operation")

if __name__ == '__main__':
    wizard = Wizard('command1.py', './')
    wizard.preferences({'python': True})
    wizard.preferences({'java': False})
    print(wizard.choices)
    wizard.execute()