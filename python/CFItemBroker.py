#CFItemBroker.py
#An often used bit of code to add or remove a number of objects
#Useful for removing items (like in payment or as part of
#an inventory check)  This is also useful for setting the number 
#of a newly created item(s) as it will check for existing item(s) and add 
#the appropriate number of new items avoiding such sillyness as the 
#number of the existing items being reset.
#This will not check for the existence of an item as that would better
#be done in the calling script so you can be flexable.
#			
#ToddMitchell

import CFPython

class Item:

    def __init__(self, object):
        self.object = object
        self.numberof = CFPython.GetQuantity(self.object)

    def add(self, number):
        tmp = (self.numberof + number)-1
        CFPython.SetQuantity(self.object, tmp)
        return 1
        
    def subtract(self, number):
        remainder = self.numberof - number       
        if remainder >= number:
            CFPython.SetQuantity(self.object, remainder)
            return 1
        elif remainder == 0:
            CFPython.RemoveObject(self.object)
            return 1
        else:
            return 0
