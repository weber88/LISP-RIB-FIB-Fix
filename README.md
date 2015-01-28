# LISP-RIB-FIB-Fix
# This python code was written to fix a LISP Bug in Nexus 7k or 77k series switches running Locator ID Separation Protocol (LISP).
# The code should be loaded into the bootflash://scripts directory on the Nexus 7k or 77k in the VDC that is running LISP.
# You may need to create the directory with the "mkdir" command.
# The command to run the script LISP_EID_Fix.py is "source LISP_EID_Fix.py".
# The python script will check the RIB and compare it to the FIB on each line card (supports all form factors of Nexus 7k or 77k).
# It will run the "clear ip route {EID with issue}" for EIDs that are found to have their RIB and FIB pout of synch.
#
# Note - you may see the EID fixed multiple time, that has to do with each card having its own FIB.
#
# Enjoy!
# -Joe Weber
