__author__ = 'v.chernov'
import time
import shutil
import os
import sys
from optparse import OptionParser

import init_logger


logger = init_logger.init_logger('copy_worker')


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
                logger.info("File copied from '%s' to '%s'" % (source, destination))
            elif os.path.isdir(source):
                copytree(source, destination)
                logger.info("Dir contents copied from '%s' to '%s'" % (source, destination))
            else:
                logger.warning("Is not dir or file '%s'" % source)
            time.sleep(timeout)
    except:
        logger.error("Unexpected error: %s" % sys.exc_info()[0])


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-s", "--source", dest="source", help='Copies from.')
    parser.add_option("-d", "--destination", dest="destination", help='Copies to.')
    parser.add_option("-t", "--timeout", dest="timeout", default=3600 * 6,
                      help="Timeout in sec. Default = 3600 * 6 (6 hours)")
    (options, args) = parser.parse_args()

    copy_worker(options.source.strip(), options.destination.strip(), float(options.timeout))