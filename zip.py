# /usr/bin/pyhon

import sys
import os
import json
from numpy import frombuffer
from glob import glob
import skimage.external.tifffile as tifffile

name = sys.argv[1]
testing = int(sys.argv[2]) if len(sys.argv) > 2 else 0

print('downloading data\n')
if testing:
  status = os.system('s4cmd.py get -r s3://neuro.datasets.private/challenges/neurofinder.test/%s' % name)
else:
  status = os.system('s4cmd.py get -r s3://neuro.datasets/challenges/neurofinder/%s' % name)

if not status == 0:
  raise Exception('error during download, aborting!')

print('packaging data\n\n')
os.system('cp neurofinder-datasets/README.md %s/' % name)
os.system('cp neurofinder-datasets/example.py %s/' % name)
os.system('cp neurofinder-datasets/example.m %s/' % name)
os.system('cp neurofinder-datasets/example.js %s/' % name)
os.system('mv %s neurofinder.%s' % (name, name))

if testing:
  print('removing sources\n\n')
  os.system('rm -rf neurofinder.%s/sources' % name)
else:
  print('renaming sources\n\n')
  os.system('mv neurofinder.%s/sources neurofinder.%s/regions' % (name, name))
  os.system('mv neurofinder.%s/regions/sources.json neurofinder.%s/regions/regions.json' % (name, name))

if len(glob('neurofinder.%s/images/*.tiff' % name)) == 0:
  print('converting images to tif\n\n')
  with open('neurofinder.%s/images/conf.json' % name) as f:
      blob = json.load(f)
      dims = blob['dims']
      dtype = blob['dtype']
  files = sorted(glob('neurofinder.%s/images/*/*.bin' % name))
  if len(files) == 0:
    files = sorted(glob('neurofinder.%s/images/*.bin' % name))
  def toarray(f):
      with open(f) as fid:
          return frombuffer(fid.read(),dtype).reshape(dims, order='F')
  os.system('mkdir neurofinder.%s/images-tif' % name)
  for i, f in enumerate(files):
      im = toarray(f)
      im = im.clip(0, im.max()).astype('uint16')
      tifffile.imsave('neurofinder.%s/images-tif/image%05g.tiff' % (name, i), im)
  os.system('rm -rf neurofinder.%s/images' % name)
  os.system('mv neurofinder.%s/images-tif neurofinder.%s/images' % (name, name))
else:
  print('skipping tiff conversion\n\n')

print('creating zip\n\n')
os.system('zip -r neurofinder.%s.zip neurofinder.%s' % (name, name))

print('copying zip to s3\n\n')
os.system('s4cmd.py put -f neurofinder.%s.zip s3://neuro.datasets/challenges/neurofinder/ ' % name)

print('cleaning up\n\n')
os.system('rm -rf neurofinder.%s' % name)
os.system('rm -rf neurofinder.%s.zip' % name)