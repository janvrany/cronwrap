cronwrap
===========================================

A cron job wrapper that wraps jobs and enables better error reporting and command timeouts.


Installing
===========

To install cronwrap simply do::

    $ sudo setup.py install
    $ cronwrap -h


Example
===========

Basic example of usage::

    $ cronwrap -h

        usage: cronwrap [-h] [-c CMD] [-e EMAILS] [-t TIME] [-k] [-kt KILLTIME] [-r]
                [-v]

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
                                even if maximum running time is exceeded.Possible
                                values include: `-t 2h`,`-t 2m`, `-t 30s`.
          -k, --kill            Kill the process if the maximum running time is
                                exceeded. This argument will only apply when the -t
                                (or --time) argument is set.
          -kt KILLTIME, --killtime KILLTIME
                                Kill the process when on a separate specified time
                                limit. This argument is separate / standalone from the
                                -t (--time) argument.Possible values include: `-kt
                                2h`,`-kt 2m`, `-kt 30s`.
          -r, --retry           Retry when the command errors out.
          -v, --verbose         Send an email / print to stdout on successful run.


    Send out a timeout alert to cron@my_domain.com:
    $ cronwrap -c "sleep 2" -t "1s" -e cron@my_domain.com
    
    Send out a timeout alert to cron@my_domain.com and kill the command:
    $ cronwrap -c "sleep 2" -t "1s" -k -e cron@my_domain.com
    
    Send out a timeout alert to cron@my_domain.com and kill the command at a different time:
    $ cronwrap -c "sleep 10" -t "2s" -kt "5s" -e cron@my_domain.com

    Send out an error alert to cron@my_domain.com:
    $ cronwrap -c "blah" -e cron@my_domain.com
    
    Retry a failed command continuously
    $ cronwrap -c "blah" -r -e cron@my_domain.com

    Don't send any reports:
    $ cronwrap -c "ls" -e cron@my_domain.com

    Send a successful report to cron@my_domain.com:
    $ cronwrap -c "ls" -e cron@my_domain.com -v
