from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Well, Wellbore


class WellView(LoginRequiredMixin, View):

    def get(self, request):

        title = 'Скважины'
        header = 'Список скважин'

        object_list = Well.objects.filter()
        paginator = Paginator(object_list, 10)
        page = request.GET.get('page')
        try:
            wells = paginator.page(page)
        except PageNotAnInteger:
            wells = paginator.page(1)
        except EmptyPage:
            wells = paginator.page(paginator.num_pages)
        return render(request, 'well/index.html', {'page': page, 'wells': wells, 'title': title, 'header': header})


class WellDetailView(LoginRequiredMixin, View):
    def get(self, request, well):
        well = get_object_or_404(Well, uid=well)
        wellbores = Wellbore.objects.filter(nameWell=well.id)
        #print(wellbores[1].uid)
        #print(Wellbore.get_absolute_url(wellbores[1]))
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

        #equipments = rig.equipments.all()
        return render(request, 'well/detail.html', {'well': well, 'welbores':wellbores})


class WellboreDetailView(LoginRequiredMixin, View):
    def get(self, request, wellbore):
        wellbore = get_object_or_404(Wellbore, uid=wellbore)


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

        #equipments = rig.equipments.all()
        return render(request, 'wellbore/detail.html', {'wellbore': wellbore})
