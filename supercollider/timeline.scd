(
~timeline=(
	time:inf, offset:0,
	pattern:Pdef(\dispatch),
	fps:1/25,
	toggle:{ arg s;
		var toggle={arg rout; if(rout.isPlaying)
			{rout.stop}
			{rout.play}
		};
		toggle.(s.tmpPattern);
		toggle.(s.routine)
	},
	ini:{ arg s;
		s.tmpPattern=Pdef(\timeline,Pfindur(
			Pfunc
			{s.time-s.offset}.asStream,
			PFF(Pfunc{s.offset}, s.pattern)
		));
		s.win=Slider(Window("timeline", 200@40).front, 200@30)
		.onClose_{s.routine.stop; Zyn.panic; s.tmpPattern.stop}
		// .action_{arg self;
		// 	if(s.time==inf){self.value=0}
		// 	{s.offset=s.value*s.time}
		// }
		.keyDownAction_{
			arg self, c;
			switch(c, $ , {s.toggle})
		}
		.mouseUpAction_{
			arg self;
			if(s.time==inf){} // do nothing
			{
				s[\offset]=s.time*self.value;
				Zyn.panic;
				if(s.tmpPattern.isPlaying)
				{s.tmpPattern.stop;s.tmpPattern.play}
			}
		};
		s.routine=Task({
			var b=0;
			while{true}{
				{
					b=s.win.value;
					s.win.value_(b+((s.time/s.fps).reciprocal));
				}.defer;
				s.fps.wait;
			};
		});
	};
)
)

