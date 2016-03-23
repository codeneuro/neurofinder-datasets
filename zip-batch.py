# /usr/bin/pyhon

import os
import muffle

training = ['00.00', '00.01', '00.02', '00.03', '00.04', '00.05', '00.06', '00.07', '00.08', '00.09', '00.10', '00.11', '01.00', '01.01', '01.02', '01.03', '01.04', '02.00', '02.01', '03.00']

testing = ['00.00.test', '00.01.test','01.00.test', '01.01.test','02.00.test', '02.01.test', '03.00.test']

print 'processing training datasets'
for name in training:
  print 'working on: dataset %s' % name
  with muffle.on():
    status = os.system('python neurofinder-datasets/zip-one.py %s 0' % name)
  if not status == 0:
    raise Exception('failure processing dataset %s' % name)

print 'processing testing datasets'
for name in testing:
  print 'working on: dataset %s' % name
  with muffle.on():
    status = os.system('python neurofidner-datasets/zip-one.py %s 1' % name)
  if not status == 0:
    raise Exception('failure processing dataset %s' % name)