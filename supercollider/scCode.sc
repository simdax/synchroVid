(
// live module
"../live/main.scd".loadRelative;

("hello ! SuperCollider s'ouvre avec le port "++NetAddr.langPort).postln;

//ShutDown.add({"supercollider s'éteint ".postln});
"duSon.scd".loadRelative;
"timeline.scd".loadRelative;

~dic=(
	quit: {0.exit},
	play: { arg msg;
		var seed, time;
		seed=msg[1] ? 0;
		time=msg[2] ? 10;
		("playing avec seed de : "++[seed]).postln;
		~timeline.time=time;
		defer{~timeline.go}
	},
	pause: {Pdef(\tout).pause;
		NetAddr("localhost", 9000).sendMsg("/Panic")},
	resume: {Pdef(\tout).resume},
	offset: {arg msg;
		Pdefn(\offset, msg[1]/1000);
		NetAddr("localhost", 9000).sendMsg("/Panic");
		Pdef(\tout).stop; Pdef(\tout).play;
	},
);
~dic.collect({|a, b|
	OSCdef(b, a, b).permanent_(true)
});


)

