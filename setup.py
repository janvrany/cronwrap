#!/usr/bin/env python
# Copyright (c) 2007 Qtrac Ltd. All rights reserved.
# This module is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

import sys
from setuptools import setup

install_requires = []
if sys.version_info < (2, 7):
    install_requires.append('argparse>=1.1')

setup(name='cronwrap',
      version = '2.0',
      author="amix the lucky stiff",
      author_email="amix@amix.dk",
      url="http://www.amix.dk/",
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
      ],

      install_requires=install_requires,

      scripts=['scripts/cronwrap'],
      platforms=["Any"],
      license="BSD",
      keywords='cron wrapper crontab cronjob',
      description="A cron job wrapper that wraps jobs and enables better error reporting and command timeouts.",
      long_description="""\
Example
===========

Basic example of usage::

    $ cronwrap -h

        usage: cronwrap [-h] [-c CMD] [-e EMAILS] [-t TIME] [-k] [-r] [-v]

        A cron job wrapper that wraps jobs and enables better error reporting and
        command timeouts. Version 2.0

        optional arguments:
          -h, --help            show this help message and exit
          -c CMD, --cmd CMD     Run a command. Could be `cronwrap -c "ls -la"`.
          -e EMAILS, --emails EMAILS
                                Email following users if the command crashes or
                                exceeds timeout. Could be `cronwrap -e
                                "johndoe@mail.com, marcy@mail.com"`. Uses system's
                                `mail` to send emails. If no command (cmd) is set a
                                test email is sent.
          -t TIME, --time TIME  Set the maximum running time.If this time is passed an
                                alert email will be sent.The command will keep running
                                even if maximum running time is exceeded.The default
                                is 1 hour `-t 1h`. Possible values include: `-t
                                2h`,`-t 2m`, `-t 30s`.
          -k, --kill            Will kill the process if the maximum running time is
                                exceeded. This argument will only apply when the -t
                                (or --time) argument is set.
          -r, --retry           Retry when the command errors out.
          -v, --verbose         Will send an email / print to stdout on successful
                                run.

    Send out a timeout alert to cron@my_domain.com:
    $ cronwrap -c "sleep 2" -t "1s" -e cron@my_domain.com
    
    Send out a timeout alert to cron@my_domain.com and kill the command:
    $ cronwrap -c "sleep 2" -t "1s" -k -e cron@my_domain.com

    Send out an error alert to cron@my_domain.com:
    $ cronwrap -c "blah" -e cron@my_domain.com
    
    Retry a failed command continuously
    $ cronwrap -c "blah" -r -e cron@my_domain.com

    Don't send any reports:
    $ cronwrap -c "ls" -e cron@my_domain.com

    Send a successful report to cron@my_domain.com:
    $ cronwrap -c "ls" -e cron@my_domain.com -v

""")
