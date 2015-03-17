__author__ = 'v.chernov'
import time
import shutil
import os
import logging
import sys
from optparse import OptionParser


def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


def copy_worker(source, destination, timeout):
    try:
        while True:
            if os.path.isfile(source):
                shutil.copy(source, destination)
            elif os.path.isdir(source):
                copytree(source, destination)
            else:
                logging.warning("Is not dir or file %s" % source)
                raise
            time.sleep(timeout)
    except:
        logging.error("Unexpected error: %s" % sys.exc_info()[0])
        raise Exception("Unexpected error")


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-s", "--source", dest="source", help='Copies from.')
    parser.add_option("-d", "--destination", dest="destination", help='Copies to.')
    parser.add_option("-t", "--timeout", dest="timeout", default=3600 * 6,
                      help="Timeout in sec. Default = 3600 * 6 (6 hours)")
    (options, args) = parser.parse_args()

    copy_worker(options.source.strip(), options.destination.strip(), float(options.timeout))