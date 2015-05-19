#!/usr/bin/env python

from distutils.core import setup

setup(name='robogif',
      version='1.0',
      description='Simple Android screen recorder',
      long_description='RoboGif allows you to simply record the screen of your 4.4+ Android device and then convert the recording to high-quality GIF or video.\n Requires adb and ffmpeg to be installed on the system.',
      author='Jernej Virag',
      license="Apache",
      author_email='jernej@virag.si',
      packages=['robogif'],
      scripts=['script/robogif'],
      classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Utilities"
      ]
     )