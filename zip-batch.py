# /usr/bin/pyhon

import os
import sys
import muffle

training = ['00.00', '00.01', '00.02', '00.03', '00.04', '00.05', '00.06', '00.07', '00.08', '00.09', '00.10', '00.11', '01.00', '01.01', '02.00', '02.01', '03.00']

testing = ['00.00.test', '00.01.test','01.00.test', '01.01.test','02.00.test', '02.01.test', '03.00.test']

selection = sys.argv[1] if len(sys.argv) > 1 else 'both'

if selection == 'training' or selection == 'both':
  print 'processing training datasets'
  for name in training:
    print 'working on: dataset %s' % name
    status = os.system('python neurofinder-datasets/zip.py %s 0' % name)
    if not status == 0:
      raise Exception('failure processing dataset %s' % name)

if selection == 'testing' or selection == 'both':
  print 'processing testing datasets'
  for name in testing:
    print 'working on: dataset %s' % name
    status = os.system('python neurofinder-datasets/zip.py %s 1' % name)
    if not status == 0:
      raise Exception('failure processing dataset %s' % name)