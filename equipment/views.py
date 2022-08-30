from django.shortcuts import render

from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from .models import Equipment


class EquipmentView(View):

    def get(self, request):

        title = 'Оборудование'
        header = 'Список оборудования'

        #object_list = Article.published.all()
        object_list = Equipment.objects.filter()
        #return render(request, 'equipment/index.html', {'equipments': equipments})
        paginator = Paginator(object_list, 10)
        page = request.GET.get('page')
        try:
            equipments = paginator.page(page)
        except PageNotAnInteger:
            equipments = paginator.page(1)
        except EmptyPage:
            equipments = paginator.page(paginator.num_pages)
        return render(request, 'equipment/index.html', {'page': page, 'equipments': equipments, 'title': title, 'header': header})


class EquipmentDetailView(View):
    def get(self, request, equipment):
        equipment = get_object_or_404(Equipment, uid=equipment)
        return render(request, 'equipment/detail.html', {'equipment': equipment})