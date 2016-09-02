import OSC

c = OSC.OSCClient()
c.connect(("localhost", 57121))   # connect to SuperCollider

def bob():
    c.send(OSC.OSCMessage("/startup", ))

def kill():
    c.send(OSC.OSCMessage("/quit"))
    
