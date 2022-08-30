from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from .models import Rig


class RigView(View):

    def get(self, request):

        title = 'Буровые установки'
        header = 'Список буровых установок'

        object_list = Rig.objects.filter()
        paginator = Paginator(object_list, 10)
        page = request.GET.get('page')
        try:
            rigs = paginator.page(page)
        except PageNotAnInteger:
            rigs = paginator.page(1)
        except EmptyPage:
            rigs = paginator.page(paginator.num_pages)
        return render(request, 'rig/index.html', {'page': page, 'rigs': rigs, 'title': title, 'header': header})


class RigDetailView(View):
    def get(self, request, rig):
        rig = get_object_or_404(Rig, uid=rig)
        #print(rig.equipments.all())
        #equipments = []
        #for i in rig.equipments.all():
        #    element=[]
        #    print(type(i))
        #    element.append(i.name)
        #    element.append(i.uid)
        #    if i.banner == "":
        #        element.append('<img src="/media/equipment_banners/default_equipment.jpg">')
        #    else:
        #        element.append('<img src=/media/'+str(i.banner)+'>')
            #element.append(i.id)
        #    equipments.append(element)
        #print(equipments)

        equipments = rig.equipments.all()
        return render(request, 'rig/detail.html', {'rig': rig, 'equipments': equipments})
