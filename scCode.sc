"hello".postln;

ShutDown.add({"goodbye".postln});

"duSon.sc".loadRelative;

OSCdef(\quit, {0.exit}, \quit);
OSCdef(\io, {arg in; in.postln}, \startup);

OSCdef(\play, {
	(Pdef(\tout) <> (seed:0)).play
}, \play)