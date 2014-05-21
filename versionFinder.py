"""
Looks for the version of a given python package
"""

import sys

__version_info__ = ('0','1','2','beta')
__version__ = '.'.join(__version_info__)

def versionFinder(moduleName):
	"""
	takes in a package name and checks for the version information
	"""

	_theModule = __import__(moduleName)

	return _theModule.version.version

def testversionFinder():
	#does not work on python3
	import sys
	if sys.version_info.major != 2:
		err_message = "warning, python version not version 2, test not set for python3"
		sys.stderr.write (err_message)
		assert False
		return False

	testPackage = 'numpy'
	O = versionFinder(testPackage)

	print O
	
	assert True
	return True

		
if __name__ == "__main__" :
	"""
	Main program to test version finder
	"""

	testversionFinder()
