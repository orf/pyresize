import platform
import os
import sys

clientos = platform.system()

def resize_screen(x,y):
    if clientos == 'Windows':
	os.system("mode {rows},{columns}".format(rows=x,columns=y))
    elif clientos in {'Linux', 'Darwin'} or clientos.startswith('CYGWIN'):
	sys.stdout.write("\x1b[8;{columns};{rows}t".format(rows=x,columns=y))
