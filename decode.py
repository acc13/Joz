#!/usr/bin/python
# Copyright 2014 Andrew Chang
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""
decode string
"""

import sys
import base64

class Decoder:
    """decode string"""
    tmpfilename = "tmp"

    @staticmethod
    def decode(str, alph1):
        """64 bit decoding using custom alphabet alph1"""
        alph2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
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
                    
    
    

def main():
    str = 'ucaUCo4NmA88Tws8BoQsKAXdBcDn'
    alph1 = 'gP9jOzA75VyIW6FRuHZimQcLB1rCTKpGN8hdEXw0eY3kMx+/JDUntsob4a2qfSvl'
    
    Decoder.decode(str, alph1)
        
    sys.exit(0)    
        
if __name__ == '__main__':
    main()
