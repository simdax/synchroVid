(

Pdef(\a,
Pbind(
		\type, \midi,
		\midiout, MIDIOut(1),
		\degree, Prand([0,1,2,3],inf ),
		\dur, Prand([0.5,1,2], inf),
	)
);

Pdef(\b, Pbind(
	\chan, 1,
	\degree, Pkey(\degree) + [0,2,4],
	\dur, 2
));

Pdefn(\offset, 0);
Pdefn(\seed, 0);

Pdef(\tout,
	PFF(Pdefn(\offset).asStream,
		Ppar([
			Pbind(),
			Pdef(\b)
		]) <> Pseed(Pdefn(\seed), Pdef(\a))
	).trace
).quant_(0)

)

