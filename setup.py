#!/usr/bin/env python3

from distutils.core import setup

setup(name='rock_paper_scissors',
      version='1.0',
      description='Python Rock Paper Scissors Game',
      author='Fatma Zohra Dahmane',
      author_email='dahmane.fzohra@gmail.com',
      packages=['rock_paper_scissor'],
      package_dir={'rock_paper_scissors': 'rock_paper_scissors'},
      entry_points={'console_scripts': ['rock-paper-scissors=rock_paper_scissors.run_game:main']}
      )
