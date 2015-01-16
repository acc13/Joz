#!/usr/bin/python
# Copyright 2014 Andrew Chang
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""
maps a given alphabet:
'gP9jOzA75VyIW6FRuHZimQcLB1rCTKpGN8hdEXw0eY3kMx+/JDUntsob4a2qfSvl'
to the 64 bit table:
'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

ucaUCo4NmA88Tws8BoQsKAXdBcDn
"""

import sys

import base64
coded_string = '''Q5YACgA...'''


class Decoder:
    """decodes string mapping given alphabet to 64 bit encoded chars"""
    tmpfilename = "tmp"

    @staticmethod
    def decode(str, alph1, alph2):
        """decodes str, mapping alphabet 1 to alphabet 2"""
        print(str)
        print(alph1)
        print(alph2)
        
        if len(alph1) != len(alph2):
            print ("alphabets must be same size.")
            return
            
        out = ''
        
        for char in str:
            out += (alph2[alph1.index(char)])
            
        print (base64.b64decode(out))
        
        return
                    
    
    

def usage():
    """print usage"""
    print('usage: -url url -email email -password password [-noemail]')
    sys.exit(1)
    
def main():
    """script main method"""
    
    '''
    #configloader tests
    args = sys.argv[1:]

    if not args or len(args) < 6:
        usage()
        
    if args[0] == '-url':
        url = args[1]
        del args[0:2]
    else:
        usage()'''
    
    str = 'ucaUCo4NmA88Tws8BoQsKAXdBcDn'
    alph1 = 'gP9jOzA75VyIW6FRuHZimQcLB1rCTKpGN8hdEXw0eY3kMx+/JDUntsob4a2qfSvl'
    alph2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    
    Decoder.decode(str, alph1, alph2)
        
    sys.exit(0)    
        
if __name__ == '__main__':
    main()
