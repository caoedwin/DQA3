from django.shortcuts import render, redirect
from django.conf import settings

# Create your views here.
from django.http import HttpResponse
from django.db import models
from .models import TestLog, UserInfo
# from .forms import UserForm,testplanForm
import datetime


def login(request):
    # return HttpResponse("hello world")
    context = {}
    context['hello'] = '登錄'
    # 2 form
    # if request.method == "POST":
    #
    #     login_form = UserForm(request.POST)
    #     message = "请检查填写的内容！"
    #     print (login_form.is_valid())
    #     if login_form.is_valid():
    #         Account = login_form.cleaned_data['Accountf']
    #         # print (Account)
    #         Password = login_form.cleaned_data['Passwordf']
    #         # print(Password)
    #         try:
    #             # print(Password)
    #             user = UserInfo.objects.get(Account=Account)
    #             # print (user.Password)
    #             if user.Password == Password:
    #                 return redirect('/index/')
    #             else:
    #                 message = "密码不正确！"
    #         except:
    #             message = "用户不存在！"
    #     return render(request, 'login/login.html', locals())
    #
    # login_form = UserForm()
    # return render(request, 'login/login.html', locals())
    # 1
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #
    #     if username and password:  # 确保用户名和密码都不为空
    #         username = username.strip()
    #         # 用户名字符合法性验证
    #         # 密码长度验证
    #         # 更多的其它验证.....
    #         try:
    #             user = UserInfo.objects.get(Account=username)
    #             print (user.Password)
    #             if user.Password == password:
    #                 return redirect('/index/')
    #             else:
    #                 message = "密码不正确！"
    #         except:
    #             message = "用户名不存在！"
    #         return render(request, 'login/login.html', {"message": message})
    # return render(request, 'login/login.html')
    # 3 session
    # 不允许重复登录
    if request.session.get('is_login', None):
        return redirect('/login/')
    # print(request.method)
    # print('test')
    if request.method == "POST":
        # login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        # if login_form.is_valid():
        Account = request.POST.get('inputEmail')
        Password = request.POST.get('inputPassword')
        # print (Account)
        # print (Password)
        try:
            user = UserInfo.objects.get(Account=Account)
            if user.Password == Password:
                # 往session字典内写入用户状态和数据,你完全可以往里面写任何数据，不仅仅限于用户相关！
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.Username
                return redirect('/index/')
            else:
                message = "密码不正确！"
        except:
            message = "用户不存在！"
        return render(request, 'test.html', locals())


    return render(request, 'test.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")
    #flush()方法是比较安全的一种做法，而且一次性将session中的所有内容全部清空，确保不留后患。但也有不好的地方，那就是如果你在session中夹带了一点‘私货’，会被一并删除，这一点一定要注意
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/index/")


def index(request):
    # 跳轉頁面
    context = {}
    context['hello'] = '主界面'
    if not request.session.get('is_login', None):
        return redirect('/login/')
    # print('2')
    # if request.session.get('is_login', None):
    #     return redirect('/index')

    # Test_form = testplanForm(request.POST)
    actstatus = ""
    actstatus_end = ""
    # Comments = ""
    message=''
    messagep=''
    End_time = "first"
    print('12')
    print (request.method)
    print (request.POST)
    # print (request.GET)

    if request.method == "POST":
        # print('11')
        # Test_form = testplanForm(request.POST)
        # Project_Unit = Test_form.cleaned_data['Unit']
        # Project = Project_Unit[:5]
        # Unit = Project_Unit[5:]
        # Phase = Test_form.cleaned_data['Phase']
        # Testitem = Test_form.cleaned_data['Item']
        # Comments = Test_form.cleaned_data['Comment']
        # dic = {'Project': Project, 'Unit': Unit, 'Phase': Phase, 'Testitem': Testitem}
        # test_log = TestLog()
        # update = TestLog.objects.filter(**dic)
        # print ('1')
        # if not update.End_time:
        #     actstatus = "disabled"
        #     print('2')
        # print (request.POST.get('Start'))
        print(request.POST)
        if 'start' in request.POST:
            print('4')
            # Test_form = testplanForm(request.POST)
            # if Test_form.is_valid():  # 必须要先验证否则提示object错误没有attribute 'cleaned_data'
            Project_Unit = request.POST.get('Units')
            if len(Project_Unit)==10:
                print('t')
                Project = Project_Unit[:5]
                Unit = Project_Unit[5:]
                print(Project)
                print(Unit)
                Phase = request.POST.get('Phase')
                print(Phase)
                if len(Phase)<=10:
                    Testitem = request.POST.get('Item')
                    Comments = request.POST.get('Comments')
                    dic = {'Project': Project, 'Unit': Unit, 'Phase': Phase, 'Testitem': Testitem, 'End_time': ""}
                    # print (dic)
                    check = TestLog.objects.filter(**dic)
                    for e in check:
                        End_time = e.End_time
                        # print(e.End_time)
                    # if End_time=="first":
                    #     test_log = TestLog()
                    #     test_log.Project = Project
                    #     test_log.Unit = Unit
                    #     test_log.Phase = Phase
                    #     test_log.Testitem = Testitem
                    #     test_log.Tester_id = request.session.get('user_name')
                    #     test_log.Comments = Comments
                    #     test_log.Start_time = datetime.datetime.now()
                    #     # test_log.End_time = End_time
                    #     test_log.save()
                    if not End_time:
                        actstatus = r'disabled="disabled"'
                        print(actstatus)
                    else:
                        test_log = TestLog()
                        test_log.Project = Project
                        test_log.Unit = Unit
                        test_log.Phase = Phase
                        test_log.Testitem = Testitem
                        test_log.Tester_id = request.session.get('user_name')
                        test_log.Comments = Comments
                        test_log.Start_time = datetime.datetime.now()
                        # test_log.End_time = End_time
                        test_log.save()
                    return render(request, 'index.html', locals())
                else:
                    messagep="Please choose Phase"
                    return render(request, 'index.html', locals())
            else:
                message="len of Units is not 10"
                return render(request, 'index.html', locals())

        if 'end' in request.POST:
            print('3')
            # Test_form = testplanForm(request.POST)
            # if Test_form.is_valid():  # 必须要先验证否则提示object错误没有attribute 'cleaned_data'
            Project_Unit = request.POST.get('Units')
            if len(Project_Unit) == 10:
                Project = Project_Unit[:5]
                Unit = Project_Unit[5:]
                Phase = request.POST.get('Phase')
                if len(Phase)<=10:
                    Testitem = request.POST.get('Item')
                    Comments = request.POST.get('Comments')
                    dic = {'Project': Project, 'Unit': Unit, 'Phase': Phase, 'Testitem': Testitem, 'End_time': ""}
                    update = TestLog.objects.filter(**dic)
                    for e in update:
                        End_time = e.End_time
                        print (End_time)
                    if not End_time:
                        print('t')
                        update.update(End_time=datetime.datetime.now())
                        # for e in update:
                        #     e.End_time= datetime.datetime.now()
                    else:
                        actstatus_end = r'disabled="disabled"'
                    return render(request, 'index.html', locals())
                else:
                    messagep="Please choose Phase"
                    return render(request, 'index.html', locals())

            else:
                message = "len of Units is not 10"
                return render(request, 'index.html', locals())

    # Test_form = testplanForm()
    return render(request, 'index.html', locals())


def DashboardProject(request):
    # 跳轉頁面
    context = {}
    context['hello'] = '主界面'
    return render(request, 'DashboardProject.html', context)


def DashboardUnits(request):
    # 跳轉頁面
    context = {}
    context['hello'] = '主界面'
    return render(request, 'DashboardUnits.html', context)
