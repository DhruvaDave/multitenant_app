from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Client
from django.urls import reverse_lazy
from django.db import connection

# Create your views here.


class ClientListView(ListView):
    model = Client
    template_name = 'client_list.html'
    context_object_name = 'clients'
    # paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ClientListView, self).get_context_data(**kwargs)
        print("------here--------")
        with connection.cursor() as cursor:
            cursor.execute("SELECT privilege_type FROM information_schema.role_table_grants where table_name::text = %s and grantee=%s",["sales_client","29"])

            # cursor.execute("SELECT privilege_type FROM information_schema.role_table_grants where table_name::text = %s and grantee=%s",["sales_client","29"])
            temp = cursor.fetchall()
        
        clients = None
        print("------temp------",temp)
        for all_data in temp:
            if 'SELECT' in all_data:
                clients = self.get_queryset().filter(salesperson=29)
                print("-------clinets---------",clients)
            # else:
            #     clients = None
            #     print("-------else--------")
        # clients = self.get_queryset()
        # page = self.request.GET.get('page')
       
        context['clients'] = clients
        return context

class ClientDetailView(DetailView):
    model = Client
    template_name = 'client_detail.html'

class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'client_update.html'
    context_object_name = 'client'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        with connection.cursor() as cursor:
            cursor.execute("SELECT privilege_type FROM information_schema.role_table_grants where table_name::text = %s and grantee=%s",["sales_client","29"])
            temp = cursor.fetchall()
        
        client = None
        print("------temp------",temp)
        for all_data in temp:
            if 'UPDATE' in all_data:
                client = self.get_queryset().filter(salesperson=29)
                print("-------clinets---------",client)
                context['title'] = 'Update'
                context['client'] = client
                return context
            else:
                print("_______you can't update_______")

        return None
        # context['title'] = 'Update'
        # context['client'] = client
        # return context

    def get_success_url(self):
        return reverse_lazy('client_detail', kwargs={'pk': self.object.id})