from django.http import JsonResponse

class Http_Code(object):
    ok = 200
    paramerror = 400
    noauth = 401
    servererror = 500
    blocked = 405

def result(code=200, message="", data=None, kwargs=None):
    json_dict = {"code":code, "message":message, "data":[data]}

    if kwargs and isinstance(kwargs,dict) and kwargs.keys():
        json_dict.update(kwargs)

    return JsonResponse(json_dict)

def ok(message="", data=None, kwargs=None):
    return result(message=message, data=data, kwargs=kwargs)

def paramerror(message="", data=None, kwargs=None):
    return result(code=Http_Code.paramerror, message=message, data=data, kwargs=kwargs)

def noauth(message="", data=None, kwargs=None):
    return result(code=Http_Code.noauth, message=message, data=data, kwargs=kwargs)

def servererror(message="", data=None, kwargs=None):
    return result(code=Http_Code.servererror, message=message, data=data, kwargs=kwargs)

def blocked(message="", data=None, kwargs=None):
    return result(code=Http_Code.blocked, message=message, data=data, kwargs=kwargs)