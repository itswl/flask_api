
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
    return 'delete_user'

@api.route('',methods = ['POST'])
def create_user():
    '''
    name,password 数据，第三方，自己的产品，APP，小程序，用户
    人，
    客户端 client
    种类很多
    注册形式很多  短信 邮件 QQ 微信

    '''
    pass