import CFPython;
import os.path
import sys

print "Running python initialize script." 
sys.path.insert(0, os.path.join(CFPython.GetDataDirectory(), CFPython.GetMapDirectory(), 'python'))

import CFGuilds
print "Updating Guilds"
CFGuilds.GuildUpdate()
