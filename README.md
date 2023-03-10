# jsonly

[<img src="https://img.shields.io/pypi/v/jsonly.svg">](https://pypi.python.org/pypi/jsonly)<br>
json을 이용하여 DB 시스템을 사용하시는 분들께 바칩니다.

## **Install**

```
pip install jsonly
```

## **Example**

### **DATA**

```json
# data.json (default)
{
  "기본": {
    "사과": "애플"
  },
  "하나": "일",
  "둘": "이"
}
```

### **GET**

데이터를 불러올 때 사용하는 메소드

```py
# get.py
from jsonly import Connect

connect = Connect(path="data.json")
print(connect.get(path="기본/사과"))
```

```
# result
>>> 애플
```

### **SET**

데이터를 덮어씌울 때 사용하는 메소드

```py
# set.py
from jsonly import Connect

connect = Connect(path="data.json")

data = {"기본중에" : "기본"}
print(connect.set(data=data))
```

```
# result
>>> True
```

```json
# data.json (modified from default)
{
    "기본중에": "기본"
}
```

### **UPDATE**

데이터를 루트 경로에 추가할 때 사용하는 메소드

```py
# update.py
from jsonly import Connect

connect = Connect(path="data.json")

data = {"새로운" : "데이터"}
print(connect.update(data=data))
```

```
# result
>>> True
```

```json
# data.json (modified from default)
{
    "기본": {
        "사과": "애플"
    },
    "하나": "일",
    "둘": "이",
    "새로운": "데이터"
}
```

### **INSERT**

데이터를 특정 경로에 추가할 때 사용하는 메소드

```py
# insert.py
from jsonly import Connect

connect = Connect(path="data.json")

data = {"데이터" : "삽입"}
print(connect.insert(data=data, path='기본'))
```

```
# result
>>> True
```

```json
# data.json (modified from default)
{
    "기본": {
        "데이터": "삽입"
    },
    "하나": "일",
    "둘": "이",
}
```
