oTree-game
=================

##Server Setup

If you just do local tests, after installed _oTree_, just execute `otree runserver` from terminal.

If you do a real experiment, you need to run production level server of oTree. To do so, besides oTree, you need to install [redis](http://redis.io/),
and start redis server from terminal by executing `redis-server`. When your redis server is active, go into the folder `oTree-game` from terminal,
then execute

```shell
export OTREE_PRODUCTION=1
otree runprodserver
```

__Notice__: the first command is to disable debug information, so when you want to get the debug information back, just execute `export OTREE_PRODUCTION=0`
from the same terminal.
