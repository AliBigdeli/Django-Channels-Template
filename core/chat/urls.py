from django.urls import path
from . import views

app_name = "chat"

urlpatterns = [
    path('create', views.ChatroomCreateView.as_view(), name='create-chatroom'),
    path('<str:room_name>', views.ChatroomGroupChatView.as_view(), name='group-chat-room'),
]