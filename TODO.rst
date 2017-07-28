**********
gping todo
**********

Tasks
=====
- [x] Add entrypoint ``gping`` and argument parsing
- [o] Add reading from stdin
- [o] Add collectd metrics gathering: https://pythonhosted.org/collectd/

Upstream changes
================
- [x] Add "Make it possible to ping without root access.": https://github.com/markotibold/gping/commit/b75fa2d41ec10073f894676fc3f3ec6b46693c05
- [o] Add "Allow binding to an interface": https://github.com/danharvey/pyping/commit/cb8489762d3171fb0b69c0fb9aaa8968d5e439b4
- [o] Add statsd support: https://github.com/ChristianKniep/python-ping/commit/a3653526e5857f346e2a244988df3849574ba385
- [o] Check "fix packet numbering bug": https://github.com/matesito/gping/commit/498c93500e35c8f5ad9c682df1e6c66fb5c5998a
- [o] Check improvements from Vijayananda Reddy: https://github.com/VijayanandaReddy/gping/commit/25ac7c8efb6cf394b6c36ed2ed5b6712116b6c53
- [o] Check "For some reason, die was not working": https://github.com/biplav/gping/commit/377f0f4e85535fd3b6f812eb29d49ad8bf9a24fa
- [o] Check "Changes to harden gping.py for usecases like die, ping of devices, timeouts": https://github.com/biplav/gping/commit/6fb9008d4ae63f954f6d59cfbf4bb445964c1351
- [o] Check features of leading non-gevent repositories (IPv6, etc.):

    - https://github.com/l4m3rx/python-ping
    - https://github.com/tomwilkie/pyping

