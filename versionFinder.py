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

if __name__ == "__main__" :
	"""
	Main program to test version finder
	"""

	testPackage = 'numpy'
	O = versionFinder(testPackage)

	print O
		
