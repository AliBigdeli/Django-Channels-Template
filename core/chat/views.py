from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import *

class ChatroomCreateView(FormView):
    template_name = "chat/chatroom-create.html"
    form_class = ChatCreateForm
    
    def form_valid(self, form):
        chat_room_name = form.cleaned_data.get("chat_room_name")
        display_name = form.cleaned_data.get("display_name")
        self.request.session.update({"display_name":display_name})
        return HttpResponseRedirect(reverse_lazy("chat:group-chat-room",kwargs={"room_name":chat_room_name}))
    
    
    def form_invalid(self, form):
        return super().form_invalid(form)
        
    
    
class ChatroomGroupChatView(TemplateView):
    template_name = "chat/chatroom-group-chat.html"
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["room_name"] = kwargs.get("room_name")
        context["display_name"] = self.request.session.get("display_name","Undefined User")
        return context
