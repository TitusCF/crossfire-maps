# python_kick.py - handler for global KICK event
#
# Copyright (C) 2004 Todd Mitchell
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#

import CFPython
import sys
import os.path
sys.path.append(os.path.join(CFPython.GetDataDirectory(),CFPython.GetMapDirectory(),'python'))
import CFLog

activator = CFPython.WhoIsActivator()
name = CFPython.GetName(activator)

log = CFLog.CFLog()
log.kick_update(name)
