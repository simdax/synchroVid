// =====================================================================
// SuperCollider Workspace
// =====================================================================

Pdefn(\offset, 50)

NetAddr("localhost", 9000).sendMsg("/Panic")
NetAddr("localhost", 57120).sendMsg("/play")

NetAddr("localhost", 57120).sendMsg("/pause")
NetAddr("localhost", 57120).sendMsg("/resume")
NetAddr("localhost", 57120).sendMsg("/offset", 50)

Zyn.port=1