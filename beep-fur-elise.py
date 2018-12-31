a,b,c,d,e,f,g = 220, 246 , 261,293,329,349,383
aflat,asharp,bflat,csharp,dflat,dsharp,eflat,fsharp,gflat,gsharp = 208,233,233,277,277,311,311,370,370,415

try:
  import winsound
except ImportError:
  import os
  def playmusic(array):
    x = 0
    i = 0
    while i < len(array):
      os.system('beep -f %s -l 270' % (array[i]))
      print array[i]
      i = i + 1
else:
  def playmusic(array):
    x = 0
    i = 0
    while i < len(array):
        winsound.Beep(	array[i]	, 300)
        print array[i]
        i = i + 1

#fur elise
notes = e, dsharp, e,dsharp, e, b, d, c, a,c,e,a,b,e,gsharp,b,c,e,e,dsharp,e,dsharp,e,b,d,c,a,c,e,a,b,e,c,b,a
playmusic(notes)
