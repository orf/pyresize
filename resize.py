import platform
import os
import sys

clientos = platform.system()

def resize_screen(rows, columns):
    if clientos == 'Windows':
	os.system("mode {rows},{columns}".format(rows=rows,columns=columns))
    elif clientos in {'Linux', 'Darwin'} or clientos.startswith('CYGWIN'):
	sys.stdout.write("\x1b[8;{columns};{rows}t".format(rows=rows,columns=columns))
