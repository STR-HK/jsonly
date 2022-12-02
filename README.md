# jsonly
[<img src="https://img.shields.io/pypi/v/jsonly.svg">](https://pypi.python.org/pypi/jsonly)<br>
json을 이용하여 DB 시스템을 사용하시는 분들께 바칩니다.
## **Install**
```
pip install jsonly
```
## **Example**
### **DATA(data.json)**
```json
{
    "기본" : {
        "사과" : "애플"
    },
    "하나" : "일",
    "둘" : "이"
}
```

### **GET**
데이터를 불러올때 쓰이는 코드
```py
from jsonly import Connect

connect = Connect(path="data.json")
print(connect.get(path="기본/사과"))
```
```
>>> 애플
```

### **SET**(저장 성공시)
데이터를 덮어씌울때 쓰이는 코드
```py
from jsonly import Connect

connect = Connect(path="data.json")

data = {"기본중에" : "기본"}
print(connect.set(data=data))
```
```
>>> True
```

### **UPDATE**(저장 성공시)
데이터를 추가할때 쓰이는 코드
```py
from jsonly import Connect

connect = Connect(path="data.json")

data = {"기본중에" : "기본"}
print(connect.update(data=data))
```
```
>>> True
```
