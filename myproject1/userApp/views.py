from django.shortcuts import render
from userApp import  models
from django.contrib import messages
from delete import *
# Create your views here.
def dl(req):
    if req.method == 'POST':
        us = req.POST.get("username")
        obj = models.User.objects.filter(username=us)
        if obj:
            return render(req, "index.html", )
        else:
            return render(req, "register.html", {"msg": "请先注册"})
    return render(req, 'login.html')
    # cookie存在客户端
    # session保存在服务器端均已键值对保存
    # 验证用户名和密码


def loginP(req):
    if req.method == "POST":
        # 1.获取form表单信息
        user = req.POST.get("username")
        psw = req.POST.get("password")
        # 2.查询数据库user表，验证用户名和密码是否正确
        obj = models.User.objects.filter(username=user, passworrd=psw)
        if obj:
            if ((user=="admin") and (psw=="admin")):
                req.session["user"] = obj  # 获取用户的所有信息
                req.session.set_expiry(30 * 60)  # 设置过期时间，单位是s
                messages.success(req, "登陆成功，欢迎")
                return render(req,"admin.html")
            # 信息正确，登陆成功http：无状态 每访问一个网页称为一个回话 会话管理：session或cookie
            # 保存用户登录状态，共多个页面获取与验证
            req.session["user"] = obj  # 获取用户的所有信息
            req.session.set_expiry(30 * 60)  # 设置过期时间，单位是s
            messages.success(req, "登陆成功，欢迎")
            return render(req, "index.html")
        else:
            messages.success(req, "用户名或密码输入错误")
            return render(req, "login.html")
    else:

        return render(req, "login.html")
def indexPage(request):
    return render(request,"index.html")
def zc(req):
    if req.method=='POST':
        us=req.POST.get("un")
        pa=req.POST.get("pwd")
        te=req.POST.get("tel")
        # d={k: list(v) for k, v in zip(us, zip(pa, te))}
        obj=models.User.objects.filter(username=us)
        if obj:
            messages.success(req, "用户名已存在")
            return render(req, "register.html")
        else:
            #models.User.objects.create(**d)
            twz=models.User.objects.create(username=us,passworrd=pa,telephone=te)
            twz.save()
            messages.success(req, "注册成功")
            return render(req, "login.html")
    else:
        return render(req,"register.html")
def tc(req):
    return  render(req,"login.html")

def Mes(req):
    if req.method == 'POST':
        n = req.POST.get("n")
        email = req.POST.get("email")
        message = req.POST.get("message")
        #d = {k: list(v) for k, v in zip(name, zip(email, message))}
        # models.User.objects.create(**d)
        twz = models.Message.objects.create(name=n, email=email, concent=message)
        twz.save()
        messages.success(req, "反馈成功")
        return render(req, "index.html")
    else:
        return render(req, "index.html")

def show_M(req):
    if req.session.get("user"):
        ms = models.Message.objects.all()
        return render(req, "message.html", locals())
    else:
        return render(req,"login.html")
def delete(req):
    c=req.GET.get("id")
    de(c)
    ms = models.Message.objects.all()
    messages.success(req, "删除成功！")
    return render(req,"message.html",locals())
def ad(req):
    return render(req,"admin.html")
