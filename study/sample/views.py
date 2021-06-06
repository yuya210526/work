import json

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic.list import ListView

from sample.models import Company


class CompanyList(ListView):
    """事業者一覧"""
    template_name='sample/company_list.html'
    context_object_name='companies'
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        companies = Company.objects.all().order_by('id')
        self.object_list =companies
        context = self.get_context_data(object_list=self.object_list)
        return self.render_to_response(context)


class BalancingGroupList(ListView):
    """BG一覧"""
    template_name='sample/balancing_group_list.html'
    context_object_name='balancing_groups'
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        company = get_object_or_404(Company, pk=kwargs['company_id'])
        balancing_groups = company.balancing_groups.all().order_by('id')
        self.object_list = balancing_groups
        context = self.get_context_data(object_list=self.object_list, company=company)
        return self.render_to_response(context)


class CompanyNavigation(View):
    """事業者ナビゲーション"""
    template_name='sample/company_navigation.html'

    def get(self, request, *args, **kwargs):
        company_navigation = [];
        
        companies = Company.objects.all().order_by('id')
        for company in companies:
            company_node = dict();
            company_node['text'] = company.name
            company_node['nodes'] = []
            company_navigation.append(company_node)

            balancing_groups = company.balancing_groups.all().order_by('id')
            for balancing_group in balancing_groups:
                balancing_group_node = dict();
                balancing_group_node['text'] = balancing_group.name
                balancing_group_node['nodes'] = []
                company_node['nodes'].append(balancing_group_node)
        return render(request, self.template_name, {'company_navigation': json.dumps(company_navigation)})
