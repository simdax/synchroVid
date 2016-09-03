(

("hello ! SuperCollider s'ouvre avec le port "++NetAddr.langPort).postln;

//ShutDown.add({"supercollider s'éteint ".postln});
Zyn.port=0;
"duSon.sc".loadRelative;

OSCdef(\quit, {0.exit}, \quit).permanent_(true);
OSCdef(\play, { arg msg;
	var seed, offset;
	#seed, offset=msg[1..]???[0,0];
	("playing avec seed et offset de : "++[seed, offset]).postln;
	(
		Pdef(\tout) <> (seed:seed, offset:offset)
	).play
}, \play).permanent_(true)

)