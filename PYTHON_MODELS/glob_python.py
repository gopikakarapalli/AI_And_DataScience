'''
 glob — Unix style pathname pattern expansion
'''

import glob
file = glob.glob('*')
print(file)

txt_file=glob.glob('*.txt')
print('txt_file:',txt_file)


py_file=glob.glob('P*.py')
print('P*_file:',py_file)


txt_file=glob.glob('*.tx*')
print('tx*_file:',txt_file)

txt_file=glob.glob('*.tx?')# one chr
print('tx?_file:',txt_file)



py_file=glob.glob('[A-Z]*.py')
print('[a-z]_file:',py_file)



root=glob.glob('*/')
print('root:',root)








'''

he glob module finds all the pathnames matching a specified pattern according
to the rules used by the Unix shell, although results are returned in arbitrary order.
No tilde expansion is done, but *, ?, and character ranges expressed with [] will be correctly matched.
This is done by using the os.listdir() and fnmatch.fnmatch() functions in concert, and not by actually invoking a subshell.
Note that unlike fnmatch.fnmatch(), glob treats filenames beginning with a dot (.) as special cases. (For tilde and shell variable expansion,
use os.path.expanduser() and os.path.expandvars().)
'''
