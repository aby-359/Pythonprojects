
from django.urls import path
from .import views
urlpatterns = [

    path('',views.todo,name='todo'),
    path('delete/<int:Taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cdn/', views.Todolistview.as_view(), name='cdn'),
    path('cde/<int:pk>/', views.Tododetail.as_view(), name='cde'),
    path('cup/<int:pk>/', views.TodoUpdate.as_view(), name='cup'),
    path('del/<int:pk>/', views.TodoDelete.as_view(), name='del')
]
