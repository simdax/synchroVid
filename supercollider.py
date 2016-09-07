
# open supercollider
import shlex,  subprocess
import time

time.sleep(1)
oscPort=57120
args="sclang -D supercollider/scCode.sc -u "+str(oscPort)
proc1=subprocess.Popen(shlex.split(args))


