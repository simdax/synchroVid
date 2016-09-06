(
var deps="PFF,Zyn".split($,);
var path="https://github.com/simdax/";

deps.do { |x|
	x.postln;
    Quarks.install(path+/+x);
};


)