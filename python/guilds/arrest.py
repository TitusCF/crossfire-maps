import random,Crossfire,CFGuilds,sys,string
from CFGuildClearance import CheckClearance
activator=Crossfire.WhoIsActivator()
whoami=Crossfire.WhoAmI()

Crossfire.SetReturnValue(1)

def find_player(object):
    while (object.Type != 1) : #1 is type 'Player'
        object = object.Above
        if not object:
            return 0
    return object

x3=1
y3=8
Params=Crossfire.ScriptParameters().split()
Approved="Access granted" if activator != None and CheckClearance(Params,activator) else "Access denied"
x= 26
y=0
guildname = Params[0]
guild=CFGuilds.CFGuild(guildname)
guildrecord=CFGuilds.CFGuildHouses().info(guildname)
ActionRequired=Params[2]

# things which are not a player are ok
if activator == None or activator.Type != Crossfire.Type.PLAYER:
    Approved = 'Access granted'


if (Approved != 'Access granted'):
    if (ActionRequired == "A"):
        activator.Teleport(Crossfire.ReadyMap('/scorn/misc/jail'),int(15),random.choice([1,3]))
    elif (ActionRequired == "D"):
        x4=random.randint(21, 23)
        y4=random.randint(22,24)
        Corpse = activator.Map.ObjectAt(int (21), int (0))
        Curse = activator.Map.ObjectAt(int(x4),int(y4))
        mymap = activator.Map
        Corpse.Name = str("%s's body" %(activator.Name))
        Corpse.Race = str("%s's Curse" %(activator.Name))
        Corpse.Weight = 1
        Curse.Name = str("%s's Curse" %(activator.Name))
        Corpse.Teleport(mymap, activator.X, activator.Y)
        Curse.InsertInto(activator)
        Curse1=activator.CheckArchInventory("amulet")
        #whoami.Say(str(Curse1))
        #whoami.Say(str(Curse))
        Curse1.Applied = 1

        activator.Teleport(mymap,int(23),int(0))



#        whoami.Say('y')
#	    whoami.Say(Approved)
	#activator.Teleport(mymap,int(x1),int(Y1))
# else:
#	whoami.Say(Approved)

#else:
#	whoami.Say('Say enter to request entry')
