import OSC

net = OSC.OSCClient()
net.connect(("localhost", 57121))   # connect to SuperCollider

def msg(m, args=None):
    #print args
    net.send(OSC.OSCMessage("/"+str(m)))
        
    
