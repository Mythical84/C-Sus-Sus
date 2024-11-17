class Memory():
    def __init__(self):
        self.mem = []

    def createVar(self, var):
        print(var.to_bytes(1,'big'))


m = Memory()
m.createVar(126)
