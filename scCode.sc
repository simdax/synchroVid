"hello".postln;

ShutDown.add({"goodbye".postln});

OSCdef(\quit, {0.exit}, \quit);
OSCdef(\io, {arg in; in.postln}, \startup);
