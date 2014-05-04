#!/usr/bin/python

"""
log writting module, run as standalone to test
"""

import os, datetime, sys

def logWrite(logFile, message, head=''):
	"""
	logWrite writes a given message to a logfile, led by a timestamp.
	A header for the line can be added (like INFO or ERROR).
	If the given filename does not exist then it will create the file,
	if it does exist then it appends the file
	"""

        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if os.path.exists(logFile):
		try:
	                log = file(logFile, "a")
		except IOError:
			print "cannot open " + logFile + " for appending!"
			return False
        else:
		try:
	                log = file(logFile, "w")
		except IOError:
			print "cannot open " + logFile + " for writting!"
			return False

        logMessage = head + ' ' + timestamp + ' ' + message + '\n'

	try:
	        log.write(logMessage)

	except IOError:
		print "error when writting to log " + logFile
		return False

        log.close

        return True

if __name__ == "__main__":


	logfile = 'testwrite.log'
	fail = "Test failed"

	print "tesing logger modules\n"

	print "testing write of a logfile (will overwrite existing test logwrite)..."
	retur = logWrite(logfile, "this is a test write")
	print "return from test write: " + str(retur)
	if not retur:
		print "write failed, exiting test"
		sys.exit(fail)

	print "testing log file append (appends to prior created log file)..."
	retur = logWrite(logfile, "this is a test append")
	print "return from test append: " + str(retur)
	if not retur:
		print "append failed, exiting test"
		sys.exit(fail)

	print "\nVerifying creation files..."
	if os.path.exists(logfile):
		print "log file found: " + logfile
	else:
		print "log file not found: " + logfile
		sys.exit(fail)		

	print "\nVerifying file contents..."
	print "expected contents:"
	print "<timestamp> this is a test write"
	print "<timestamp> this is a test append"

	file = open(logfile, 'r')
	for line in file:
		print line

