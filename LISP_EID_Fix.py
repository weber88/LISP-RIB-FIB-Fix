#!/usr/bin/env python
#
#
"""

     Python Code for NXOS Bug CSCur33701
     Copyright (c) 2014 World Wide Technology, Inc.
     All rights reserved.

     Written by:
     Joe Weber, World Wide Technology

     Revision history:
     18 January 2015  |  1.0 initial version


"""
import cisco


def lisp_rib(eid_IP):
    """
    Function to provide RIB output interface
    """	
    eid1 = cisco.cli('show ip route ' + eid_IP + ' | in \*via')
    eid2 = eid1.split(',')
    eid3 = [x.strip(' ') for x in eid2]
    eid = eid3[1]
    return eid


def lisp_fib(eid_IP):
    """
    Function to provide FIB output interface
    """
    modules = 18
    eid_fiblist = []
    while modules != 0:
        modules -= 1
        try:
            module = str(modules)
            eid1 = cisco.cli('show forwarding route ' + eid_IP + ' module ' + module + ' | in ' + eid_IP)
            eid_fib1 = eid1.split('\n')
            for x in eid_fib1:
                y = x.split(" ")
                z = filter(None, y)
                eid_fib = z[2]
                eid_fiblist.append(eid_fib)
            return eid_fiblist
        except:
            pass
    return eid_fiblist



def eidlist():
    """
    Gathering LISP EIDs by line of 'show lisp eid sum' output
    """
    eidlist = []
    eidlist1 = cisco.cli('sh lisp dyn sum | ex Dyn-EID | ex VRF | ex Packet')
    eidlist2 = str(eidlist1)
    eidlist3 = eidlist2.split('\n')[:-1]
    for x in eidlist3:
        y = x.split(" ")
        z = filter(None, y)
        zz = z[1]
        eidlist.append(zz)
    return eidlist



def main():
    """
    Function to fix Cisco Bug CSCur33701
    """
    #
    # Loop for Main output
    #
    eidlist1 = eidlist()        
    for eid in eidlist1:
        eidrib = lisp_rib(eid)
        eidfib = lisp_fib(eid)
        for fib in eidfib:
            if fib != eidrib:
                cisco.cli('clear ip route ' + eid)
                print "LISP EID {} - Found RIB-FIB out of sync and fixed".format(eid)
            else:
                continue

if __name__ == '__main__':
    main()