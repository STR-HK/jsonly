# jsonly

[<img src="https://img.shields.io/pypi/v/jsonly.svg">](https://pypi.python.org/pypi/jsonly)<br>
Dedicated to those who use DB systems with json.

## **Install**

```
pip install jsonly
```

## **Example**

### **DATA**

```json
# data.json (default)
{
  "default": {
    "a": "apple"
  },
  "one": "first",
  "two": "second"
}
```

### **GET**

Method to use when fetching data

```py
# get.py
from jsonly import Connect

connect = Connect(path="data.json")
print(connect.get(path="default/a"))
```

```
# result
>>> apple
```

### **SET**

Method to use when overwriting data

```py
# set.py
from jsonly import Connect

connect = Connect(path="data.json")

data = {"this" : "default"}
print(connect.set(data=data))
```

```
# result
>>> True
```

```json
# data.json (modified from default)
{
    "this": "default"
}
```

### **UPDATE**

Method to use when adding data to the root path

```py
# update.py
from jsonly import Connect

connect = Connect(path="data.json")

data = {"new" : "data"}
print(connect.update(data=data))
```

```
# result
>>> True
```

```json
# data.json (modified from default)
{
    "default": {
        "a": "apple"
    },
    "one": "first",
    "two": "second",
    "new": "data"
}
```

### **INSERT**

Method to use when adding data to a specific path

```py
# insert.py
from jsonly import Connect

connect = Connect(path="data.json")

data = {"data" : "insert"}
print(connect.insert(data=data, path='default'))
```

```
# result
>>> True
```

```json
# data.json (modified from default)
{
    "default": {
        "data": "insert"
    },
    "one": "first",
    "two": "second",
}
```
