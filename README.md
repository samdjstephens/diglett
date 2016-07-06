# diglett - SSH tunnel manager

![diglett](http://cdn.bulbagarden.net/upload/thumb/3/31/050Diglett.png/250px-050Diglett.png)

> to have a way of naming, opening and closing SSH tunnels without using `ps aux | grep ssh` —> `kill`

-- samjdstephens, founding author of diglett

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
