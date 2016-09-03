(

Pdef(\a,
Pbind(
		\type, \midi,
		\midiout, MIDIOut(0),
		\degree, Prand([0,1,2,3],inf ),
		\dur, Prand([0.5,1,2], inf),
	)
);

Pdef(\b, Pbind(
	\chan, 1,
	\degree, Pkey(\degree) + [0,2,4],
	\dur, 2
));

Pdef(\tout, {arg seed=0, offset=0;
	PFF(offset,
		Ppar([
			Pbind(),
			Pdef(\b)
		]) <> Pseed(seed, Pdef(\a))
	)
}
)

)



