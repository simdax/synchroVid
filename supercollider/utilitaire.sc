// =====================================================================
// SuperCollider Workspace
// =====================================================================

~port=57121;
Pdefn(\offset, 50)

NetAddr("localhost", 9000).sendMsg("/Panic")
NetAddr("localhost", ~port).sendMsg("/play")

NetAddr("localhost", ~port).sendMsg("/pause")
NetAddr("localhost", ~port).sendMsg("/resume")
NetAddr("localhost", ~port).sendMsg("/offset", 50)




OSCFunc({Slider().front}, \test)
NetAddr("localhost", ~port).sendMsg("/test")
