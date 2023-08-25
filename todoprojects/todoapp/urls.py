from django.urls import path
from . import views
app_name='todoapp'

urlpatterns = [

    path('', views.add, name='add'),
    # path('details',views.details,name='details')
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('classhome/',views.TaskListView.as_view(),name='classhome'),
    path('classdetail/<int:pk>/', views.TaskDetailView.as_view(), name='classdetail'),
    path('classupdate/<int:pk>/', views.TaskUpdateView.as_view(), name='classupdate'),
    path('classdelete/<int:pk>/', views.TaskDeleteView.as_view(), name='classdelete'),

]