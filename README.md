
Urlcf URL Shortener
======

Tested under Python 2.7 on Ubuntu 14.04.

Runs on 80 with index on /.

* Install.

```bash

apt-get install python-flask python-sqlalchemy

wget -O urlcf.zip https://codeload.github.com/alkorgun/urlcf/zip/master

unzip urlcf.zip

rm urlcf.zip

cd urlcf-master

python setup.py install

```

* Test on **8080**.

```bash

urlcf-run8080

```

* Run as service.

```bash

service urlcf start

```

* Run on startup.

```bash

update-rc.d urlcf defaults

```

* Build **DEB**.

```bash

apt-get install python-stdeb

cd urlcf-master

./build_deb.sh

```
