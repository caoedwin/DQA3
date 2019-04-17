# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.

from .models import TestLog,UserInfo

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('Account', 'Password', 'Username',)
        }),
    )
    list_display = ('Account', 'Password', 'Username', )
    # 列表里显示想要显示的字段
    list_per_page = 50
    # 满50条数据就自动分页
    ordering = ('-Account',)
    # 后台数据列表排序方式
    list_display_links = ('Account', )
#导入需要管理的数据库表
@admin.register(TestLog)
class TestLogAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields' : ('Project', 'Unit', 'Phase', 'Testitem',)
        }),
        ('Advanced options',{
            'classes': ('collapse',),
            'fields' : ('Tester','Comments')
        }),
    )
    list_display = ('Project', 'Unit', 'Phase', 'Testitem', 'Tester', 'Comments', 'Start_time', 'End_time')
    # 列表里显示想要显示的字段
    list_per_page = 50
    # 满50条数据就自动分页
    ordering = ('-Start_time',)
    #后台数据列表排序方式
    list_display_links = ('Unit', 'Testitem')
    # 设置哪些字段可以点击进入编辑界面
    # list_editable = ('Tester',)
