import time
import sys
import getopt
import shutil
import os
from optparse import OptionParser

def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

def main(source, destination, timeout):    
    try:
        while True:
            if os.path.isfile(source):   
                shutil.copy(source, destination)
            elif os.path.isdir(source):                
                copytree(source, destination)
            else:
                print("Is not dir or file")
                raise
            time.sleep(timeout)
    except KeyboardInterrupt:
        print("Quitting the program")
    except:
        print("Unexpected error")
        raise
    
if __name__ == "__main__":
   
    parser = OptionParser()
    parser.add_option("-s", "--source", dest="source", default='C:\\x32_shit\\catalog-goods_10000.xml', help='Copies from.')
    parser.add_option("-d", "--destination", dest="destination", default='C:\\products\\source\\catalog-goods_10000.xml', help='Copies to.')
    parser.add_option("-t", "--timeout", dest="timeout", default = 3600 * 6, help = "Timeout in sec. Default = 3600 * 6 (6 hours)")
    (options, args) = parser.parse_args()
    
    main(options.source, options.destination, options.timeout)



