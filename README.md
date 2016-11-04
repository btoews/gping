# GPing #

This is a fork of the python-ping project that strips out most everything and replaces it with gevent.
The point is to have an event driven ping utility for doing many concurrent pings...

## Run on the commandline ##

    # Ping some hostnames
    gping --hostnames=gnu.org,fsf.org,google.com,microsoft.com,googleusercontent.com,live.com,stackoverflow.com,141.1.1.1,8.8.8.8,192.168.123.1,192.168.999.1

## Demo: Top 100 domains ##

    # Ping the top 100 domains
    time python gping.py

## Use as library ##

    gp = GPing()
    gp.send("127.0.0.1",test_callback)
    gp.join()

## Install ##

This *should* be easy on your average \*nix box (raw sockets are needed). Just type `sudo pip install gping`

## License and Credits ##

The python-ping project was started by Matthew Dixon Cowles.

    - copyleft 1989-2011 by the python-ping team, see AUTHORS for more details.
    - license: GNU GPL v2, see LICENSE for more details.

I have left the license and authors information intact, but this project seems to have a long history or forks and such
so I am probably somehow pissing someone off or violating some license. Let me know if this is the case and I will be better.
