# diglett - SSH tunnel manager

![diglett](http://cdn.bulbagarden.net/upload/thumb/3/31/050Diglett.png/250px-050Diglett.png)

# Install
```
pip install git+git://github.com/samdjstephens/diglett.git
```

# Use

1. Configure a new tunnel:
  ```
  diglett add myTunnel sam myServer 8080
  ```
2. Connect:
  ```
  diglett tunnel myTunnel
  ```
3. Close:
  ```
  diglett close myTunnel
  ```
4. List open tunnels:
  ```
  diglett ls
  ```
5. Help: `diglett --help`
