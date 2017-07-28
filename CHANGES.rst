***************
gping changelog
***************

In progress
===========

2016-11-21 0.2
==============
- Be graceful to hostname resolution failures
- Record all failures (hostname resolution and timeouts) in ``self.failures``
- Improve console output formatting
- Add shell command entrypoint ``gping`` to ``setup.py``
- Add argument parsing for interactive use, e.g. ``--hostnames=www.example.net,mail.example.net``
- Incorporate "Make it possible to ping without root access" using ``socket.SOCK_DGRAM`` instead of ``socket.SOCK_RAW``
  by Marko Tibold: https://github.com/markotibold/gping/commit/b75fa2d4
- Incorporate  "Allow binding to an interface", e.g. ``--bind=192.168.111.2``
  by Dan Harvey: https://github.com/danharvey/pyping/commit/cb848976
- Non-interactive mode: Record all results in ``self.results``
- Non-interactive mode: Make verbose output optional

2012-08-21 0.1
==============
- Fix setup.py deps
- Add install instructions to README
- Tag release ``gping-0.1``

2012-07-17 0.0
==============
- Add main gping.py

2012-07-12 0.0
==============
- Change __main__ action. Fix id overflow issue.

2012-07-10 0.0
==============
- First commit. Clean out stuff. Fix setup.py.
- Add README.md
