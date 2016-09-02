
# open supercollider
import shlex,  subprocess

#oscPort=57121
args="sclang -D scCode.sc -u "+str(57121)
proc1=subprocess.Popen(shlex.split(args))
sc
