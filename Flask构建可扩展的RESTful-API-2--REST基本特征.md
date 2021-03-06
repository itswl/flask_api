# 2\. REST基本特征

### 1.REST的最基本特征

我们把服务器提供的服务统一称为资源。 我们可以使用URL来定位资源，如/v1/book/user/1 来定位一个用户 定位到资源以后，可以使用HTPP动词来操作资源，类似使用DDL操作数据库。



![image](http://upload-images.jianshu.io/upload_images/14597179-a994cb294ad609e5?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240) 


对于视图函数的URL，尽量不应该包含动词，因为URL是用来定位资源的，例如我们之前的试图函数，应该这样改写
```

# from flask import Blueprint

# user = Blueprint('user',__name__)

# @user.route('/v1/user/get')
# def get_user():
#     return 'imwl'

from app.libs.redprint import Redprint

api = Redprint('user')
#@api.route('/get')  URL中不应该包含动词
@api.route('',methods = ['GET'])
def get_user():
    return 'get_user'

@api.route('',methods = ['PUT'])
def update_user():
    return 'update_user'

@api.route('',methods = ['DELETE'])
def delete_user():
    return 'deletete_user'

@api.route('',methods = ['POST'])
def create_user():
    return 'create_user'
```
### 2.为什么标准的REST不适合内部开发

REST的使用场景有两个：内部开发API，开放API。 标准的REST比较适合开放性的API。只负责提供数据，不负责业务逻辑

1.  由于内部的开发，业务逻辑非常复杂，想用简单的四个接口来标示所有的业务逻辑，基本上是不可能的
2.  REST的接口粒度比较粗（返回的资源属性比较多；服务器不会负责处理数据），这样前端的开发是不太方便的
3.  标准的REST会造成HTTP请求的数量大幅度的增加

### 3.建议

*   尽量遵从REST的设计风格规范
*   要灵活一些，如果前端要考虑业务逻辑的话，我们就不要遵从资源的限制了，应该让API具有业务逻辑的性质
*   如果前端需要几个资源合并在一起的数据，那么我们就为前端定制一个合并数据的接口
