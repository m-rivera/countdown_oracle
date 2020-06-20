#!/usr/bin/env python

from setuptools import setup

setup(name='countdown_oracle',
      description='Play Countdown Letters in the command line.',
      author='Miguel Rivera',
      author_email='miguel.rivera@hotmail.fr',
      packages=['countdown_oracle',
                'countdown_oracle.src',
                'countdown_oracle.scripts'],
      scripts=['countdown_oracle/scripts/countdown.py'],
      install_requires=['nltk']
      )

