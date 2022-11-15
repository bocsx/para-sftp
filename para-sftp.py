#!/usr/bin/python3 -u
#
# para-sftp.py
#

import sys, json, os, subprocess, difflib
from datetime import datetime
from os import path
import re

from time import sleep
import threading
from threading import Thread
import tempfile

import gnupg
import logging


def log_it( logfile, message, to_console ):

    if to_console:
        sys.stdout.write( message + '\n' )

    logging.basicConfig(format='%(asctime)s %(message)s', filename=logfile,level=logging.INFO)
    for mline in message.split('\n'):
        logging.info( mline )


def usage():

    print('\nUsage:\n    ' + sys.argv[0] + ' options\n')
    print('''Options:
    -c connect_string
    -k private_key_file
    -b batch_file
    -m - maximum number of connections in parallel
    -d - delete local files after upload
    -r - delete remote files after download

Example:
    para-sftp.py -m 2 -d -c user1@sftp-site.hu:2222 -k priv.key -b b1.sftp -c user2:password123@other-site.hu:2224 -b b2.sftp -b b3.sftp
''')
    sys.exit( 1 )


max_parallel=4
delete_uploaded=False
delete_downloaded=False

#log_it( vcheck_log, sys.argv[0] + ' started.', False )

#while True:
#    try:
#        fin=subprocess.Popen(['tail', '--lines=0', '-F', filelist ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#        for line in tailF(fin):
#            line=line.decode()
#            if re.search(':', line):
#                (date, time, hostname, domain, user, file)=line.split(':')
#                file=file.rstrip()
#                while( threading.active_count()-1 >= max_parallel ):
#                    sleep( sleep_interval )

#                t = Thread(target=check_one_file, args=(domain, user, file))
#                t.start()
#            else:
#                continue
#    except:
#        log_it( vcheck_log, filelist + " error: " + str( sys.exc_info() ), False)

#    sleep( sleep_interval )
