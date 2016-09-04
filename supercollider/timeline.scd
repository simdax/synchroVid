(

~timeline=(
	time:100, pattern:Pdef(\tout), fps:1/25,
	pl:{ arg s, temps=s.time, offset=0;
		s.tmpPattern=Pfindur(temps, PFF(offset, s.pattern)).play
	},
	timeline:{ arg s;
	 	var a=Slider(Window("timeline", 200@40).front, 200@30)
		.onClose_{r.stop; Zyn.panic; s.tmpPattern.stop} 
		.mouseUpAction_{
			arg self;
			var tps=s.time*self.value;
			//var a=NetAddr("localhost", NetAddr.langPort);
			Zyn.panic; s.tmpPattern.stop; 
			s.pl(s.time-tps, tps)
		}; 
		var r=Routine({
			var b=0;
			while{true}{
				{
					b=a.value;
					a.value_(b+((s.time/s.fps).reciprocal));
				}.defer;
				s.fps.wait;
			};
		});
		r.play
	},
	go:{arg s;
		s.pl; s.timeline
	},
);
)

