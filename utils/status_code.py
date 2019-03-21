
class code():

    success = {'code': 200, 'msg': '请求成功！', 'data': ''}

    # user_form 表单验证 json
    user_form_required = {'code': 1001, 'msg': '请将参数填写完整！', 'data': ''}

    user_form_mobile = {'code': 1002, 'msg': '手机号填写不正确！', 'data': ''}

    user_form_imagecode = {'code': 1003, 'msg': '随机验证码填写错误！', 'data': ''}

    user_form_phonecode = {'code': 1004, 'msg': '短信验证码填写错误！', 'data': ''}

    user_form_mobiled = {'code': 1005, 'msg': '手机号已注册！', 'data': ''}

    user_status_info = {'code': 1009, 'msg': '未登录！', 'data': ''}
    # login_from 表单验证

    login_form_required = {'code': 1011, 'msg': '请将参数填写完整！', 'data': ''}

    login_form_mobile = {'code': 1012, 'msg': '手机号填写不正确！', 'data': ''}

    login_form_password = {'code': 1013, 'msg': '手机号或者密码错误！', 'data': ''}


    # 实名认证

    auth_form_required = {'code': 1021, 'msg': '请将参数填写完整！', 'data': ''}

    auth_form_name = {'code': 1022, 'msg': '请填写正确的姓名！', 'data': ''}

    auth_form_card = {'code': 1023, 'msg': '请填写正确身份证号！', 'data': ''}


    # 房源
    is_house_auth = {'code': 1031, 'msg': '未完成认证！', 'data': ''}
    is_house_order_auth = {'code': 1032, 'msg': '不能对自己的房源提交订单！', 'data': ''}

    @staticmethod
    def set_data(status, data=''):
        status['data'] = data
        return status

    @staticmethod
    def set_err_name(status, error_name=''):
        status['error-name'] = error_name
        return status