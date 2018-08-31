# About

This is a demo for channels_redis not closing connections when used together with async_to_sync.

# Requirements

- redis installed and running
- reporting open handles needs access to `/proc/self/fd`

# Steps

Setup project and run server:

```
virtualenv env
source env/bin/activate
pip install -r requirements.txt

cd project
./manage.py runserver &
```

Run the sync test command
`./manage.py test_send_sync`

It will show the number of open handles, which includes TCP connections:

```
number of open handles 10
number of open handles 11
number of open handles 12
number of open handles 13
number of open handles 14
number of open handles 15
number of open handles 16
number of open handles 17
number of open handles 18
number of open handles 19
number of open handles 20
number of open handles 21
number of open handles 22
...
```

In contrast, try out async sending:

`./manage.py test_send_async`

```
number of open handles 10
number of open handles 10
number of open handles 10
number of open handles 10
number of open handles 10
number of open handles 10
...
```

You can open http://localhost:8000/app/ in a browser and watch the websocket messages coming in.