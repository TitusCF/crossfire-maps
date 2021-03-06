"""
Created by: Joris Bontje <jbontje@suespammers.org>

This script implements the apply event for mailboxes. When a mailbox is
opened, check the player's mail and create objects if necessary.
"""

import Crossfire
import CFMail

activator = Crossfire.WhoIsActivator()
mail = CFMail.CFMail()
whoami = Crossfire.WhoAmI()

total = mail.countmail(activator.Name)

if total > 0:
    activator.Write("You have %d mail!" % total)
    elements = mail.receive(activator.Name)
    for element in elements:
        type, fromname, message = element
        if type == 1:
            msgob = whoami.CreateObject('scroll')
            msgob.Name = "mail F: %s T: %s" % (fromname, activator.Name)
            msgob.NamePl = msgob.Name
            msgob.Message = message
            msgob.Value = 0
        elif type == 2:
            msgob = whoami.CreateObject('note')
            msgob.Name = 'newspaper D: '+fromname
            msgob.NamePl = 'newspapers D: '+fromname
            msgob.Message = message
            msgob.Value = 0
        elif type == 3:
            msgob = whoami.CreateObject('diploma')
            msgob.Name = 'warning F: '+fromname+' T: '+activator.Name
            msgob.NamePl = 'warnings F: '+fromname+' T: '+activator.Name
            msgob.Message = message
            msgob.Value = 0
        else:
            Crossfire.Log(Crossfire.LogError, 'ERROR: unknown mailtype\n')
else:
    activator.Write("You haven't got any mail.")
