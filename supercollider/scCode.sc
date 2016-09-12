(
// live module
//"../live/main.scd".loadRelative;

("hello ! SuperCollider s'ouvre avec le port "++NetAddr.langPort).postln;

//ShutDown.add({"supercollider s'éteint ".postln});
"duSon.scd".loadRelative;
"timeline.scd".loadRelative;
"dic.scd".loadRelative;


)

