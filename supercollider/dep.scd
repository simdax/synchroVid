(
var simDeps="PFF,Zyn,ext,patternsSC".split($,);
var deps="TabbedView2";
var path="https://github.com/simdax/";

simDeps.do { |x|
    Quarks.install(path+/+x);
};
deps.do { |x|
    Quarks.install(x)
}; 

)