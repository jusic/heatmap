import os
import glob

from distutils.core import setup, Extension
from distutils.command.install import install
from distutils.command.build_ext import build_ext

cHeatmap = Extension('cHeatmap', sources=['heatmap/heatmap.c', ])

setup(name='heatmap',
      version="2.2.1",
      description='Module to create heatmaps',
      author='Jeffrey J. Guy',
      author_email='jjg@case.edu',
      url='http://jjguy.com/heatmap/',
      license='MIT License',
      packages=['heatmap', ],
      py_modules=['heatmap.colorschemes', ],
      ext_modules=[cHeatmap, ],
      requires=["Pillow", ],
      test_suite="test",
      tests_require=["Pillow", ],
      )
