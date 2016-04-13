# Fake CSV server
A web server serving nonsense CSV files of specified size. Can be useful in some integration tests.

Can send multiple files in parallel and do it much faster than it would be possible to read them from a disk (unless from some crazy SSDs).
Works with Python 3 and 2.

Can be deployed to Cloud Foundry.

##Usage
```
$ pip install -r requirements.txt
$ PORT=9099 python fake_csv_server/app.py &
$ curl localhost:9099/fake-csv/3
```

In response you'll get a three kilobyte (plus the size of the header line) CSV file.

