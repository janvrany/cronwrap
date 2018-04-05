cronwrap
===========================================

A cron job wrapper that wraps jobs and enables better error reporting and command timeouts.


Installing
===========

To install cronwrap simply do::

    $ sudo easy_install cronwrap
    $ cronwrap -h


Example
===========

Basic example of usage::

    $ cronwrap -h

        usage: cronwrap [-h] [-c CMD] [-e EMAILS] [-t TIME] [-k] [-r] [-v]

        A cron job wrapper that wraps jobs and enables better error reporting and
        command timeouts. Version 1.3

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
