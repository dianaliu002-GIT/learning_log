# learning_logs/urls.py
from django.urls import path
from . import views  # 导入当前应用的视图模块（views.py）


app_name = 'learning_logs'  # 必须定义应用命名空间（否则反向解析可能报错）
# 定义该应用的 URL 路由列表
urlpatterns = [
    # 路径：访问 /learning_logs/ 时，调用 views.index 视图函数
    path('', views.index, name='index'),  
    # 说明：
    # - 第一个参数 '' 是相对路径（结合主配置的 'learning_logs/'，完整路径为 /learning_logs/）
    # - views.index 是处理该路径的视图函数（需要在 views.py 中定义）
    # - name='index' 给这个路由起个名字，方便在模板中引用
    
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    
    path('new_topics/', views.new_topic, name='new_topic'),
    path('topics/<int:topic_id>/new_entry/', views.new_entry, name='new_entry'),
    
    path('entries/<int:entry_id>/edit/', views.edit_entry, name='edit_entry'),
    
]

