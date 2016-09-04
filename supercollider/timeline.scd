(

a=(
time:10, pattern:Pbind(), fps:1/25,
pl:{ arg s;
	Pfindur(s.time, s.pattern).play
},
timeline:{ arg s;
	a=Slider().front; //10s
	Routine({
		var b=0;
		while{b!=1}{
			{
				b=a.value.postln;
				a.value_(b+((s.time/s.fps).reciprocal));
			}.defer;
			s.fps.wait;
		};
	}).play
}
);
)
