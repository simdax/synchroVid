// =====================================================================
// SuperCollider Workspace
// =====================================================================

~port=57120;
Pdefn(\offset, 50)

NetAddr("localhost", 9000).sendMsg("/Panic")
NetAddr("localhost", ~port).sendMsg("/play")

NetAddr("localhost", ~port).sendMsg("/pause")
NetAddr("localhost", ~port).sendMsg("/resume")
NetAddr("localhost", ~port).sendMsg("/offset", 50)

~timeline.go


