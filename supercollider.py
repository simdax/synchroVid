
# open supercollider
import shlex,  subprocess

#oscPort=57121
args="sclang -D supercollider/scCode.sc -u "+str(57120)
proc1=subprocess.Popen(shlex.split(args))

