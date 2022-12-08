import os

# os.system('cd ,')

out = os.popen('cd ,').read()
print(out)


class Comand:
    
    def __init__(self):
        pass
    
    def exec(self, cmd):
        os.system(cmd)
    
    def exec_out(self, cmd):
        return os.popen(cmd).read()