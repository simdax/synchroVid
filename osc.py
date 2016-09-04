import OSC


net = OSC.OSCClient()
net.connect(("localhost", 57120))   # connect to SuperCollider

def msg(m, args=[]):
    net.send(OSC.OSCMessage("/"+str(m),args))
        
    
