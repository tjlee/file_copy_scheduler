__author__ = 'v.chernov'
import sys
import time
import os
from optparse import OptionParser

import init_logger


logger = init_logger.init_logger('delete_worker')


def remove_dir_contents(source):
    for dir_file in os.listdir(source):
        file_path = os.path.join(source, dir_file)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                logger.info("File removed: '%s'" % file_path)
        except:
            logger.error("Error: %s" % sys.exc_info()[0])


def delete_worker(source, timeout):
    try:
        while True:
            if os.path.exists(source):
                if os.path.isfile(source):
                    os.remove(source)
                    logger.info("File removed '%s'" % source)
                elif os.path.isdir(source):
                    remove_dir_contents(source)
            else:
                logger.warning("File or dir is not exists '%s'" % source)
            time.sleep(timeout)
    except:
        logger.error("Unexpected error: %s" % sys.exc_info()[0])


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-s", "--source", dest="source", help='Deletes from.')
    parser.add_option("-t", "--timeout", dest="timeout", default=3600 * 6,
                      help="Timeout in sec. Default = 3600 * 6 (6 hours)")
    (options, args) = parser.parse_args()

    delete_worker(options.source.strip(), float(options.timeout))