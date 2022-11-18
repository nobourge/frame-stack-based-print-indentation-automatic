import sys
import auto_indent

sys.stdout = AutoIndent(sys.stdout)

def f(x):
   print "f(%s)" % x
   if x == 0:
       return 0
   elif x == 1:
       return 1
   else:
       return f(x-1) + f(x-2)

f(6)
