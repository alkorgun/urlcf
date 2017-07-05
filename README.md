
Urlcf URL Shortener
======

Tested under Python 2.7 on Ubuntu 14.04.

Runs on 80 with index on /.

* Install.

```bash

apt-get install python-flask python-sqlalchemy

tar fx urlcf.tar

cd urlcf

python setup.py install

```

* Run.

```bash

service urlcf start

```

* Run on startup.

```bash

update-rc.d urlcf defaults

```
