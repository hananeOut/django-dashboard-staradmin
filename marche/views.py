from django.shortcuts import render,redirect
from .models import Consultation, Soumission
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views.generic.edit import UpdateView

def consultationCreate(request):
    if request.method == 'POST' and request.FILES['Fich_Tech_valid'] and request.FILES['PV_Eval'] and request.FILES['PV_Ouvert'] :
        Fich_Tech_valid = request.FILES['Fich_Tech_valid']
        PV_Eval = request.FILES['PV_Eval']
        PV_Ouvert = request.FILES['PV_Ouvert']
        fs = FileSystemStorage()
        filename1 = fs.save(Fich_Tech_valid.name, Fich_Tech_valid)
        filename2 = fs.save(PV_Eval.name, PV_Eval)
        filename3 = fs.save(PV_Ouvert.name, PV_Ouvert)
        url1 = fs.url(filename1)
        url2 = fs.url(filename2)
        url3 = fs.url(filename3)
        consultation = Consultation(
            Nouvelle_Relance=request.POST['Nouvelle_Relance'],
            N_Dossier=request.POST['N_Dossier'],
            A_N_Dossier=request.POST['A_N_Dossier'],
            Designation=request.POST['Designation'],
            Type_Operation=request.POST['Type_Operation'],
            Nom_Agent_Tech=request.POST['Nom_Agent_Tech'],
            date_Fich_Tech=request.POST['date_Fich_Tech'],
            Fich_Tech_valid=url1,
            date_Lance=request.POST['date_Lance'],
            date_Ouvert=request.POST['date_Ouvert'],
            PV_Eval=url2,
            PV_Ouvert=url3,
            System_Eval=request.POST['System_Eval'],
            Created_by = request.user,
        )
        consultation.save()
    return render(request, 'Create.html')

def consultationShow(request):
    consultation = Consultation.objects.all()
    return render(request, 'FonCon.html', {'consultation': consultation})

def consultationEdit(request, id):
    consultation = Consultation.objects.get(id=id)
    if request.method == 'POST' :
        consultation.N_Dossier = request.POST['N_Dossier']
        consultation.A_N_Dossier = request.POST['A_N_Dossier']
        consultation.Nom_Agent_Tech = request.POST['Nom_Agent_Tech']
        consultation.save()
        return redirect('/marche/list')
    return render(request, 'Edit.html',{'consultation': consultation})

def consultationDelete(request,id):
    consultation = Consultation.objects.get(id=id)
    consultation.delete()
    return redirect('/marche/list')
    return render(request, 'FonCon.html')

class SoumissionUpdate(UpdateView):
    model = Soumission
    fields = ['Iden_Ope']
    template_name = 'CreateSoum.html"'
    success_url="/marche/soum/<int:id>"

def SoumissionCreate(request, id):
    if request.method == 'POST':
        soumissionnaire = Soumission(
            Iden_Ope = request.POST['Iden_Ope'],
            Raison_Soci = request.POST['Raison_Soci'],
            Statut_Juri = request.POST['Statut_Juri'],
            N_Tele = request.POST['N_Tele'],
            N_Fax = request.POST['N_Fax'],
            Email = request.POST['Email'],
            Created_by = request.user,
            Con_id=Consultation.objects.get(id=id),
        )
        soumissionnaire.save()
    else:
        ls_soumissionnaire = Soumission.objects.filter(Con_id = Consultation.objects.get(id=id))
        return render(request, "CreateSoum.html", {'ls_soumissionnaire': ls_soumissionnaire})

def SoumissionUpdate(request, id):
    soumissionnaire = Soumission.objects.get(pk=id)
    if request.method == 'POST':
        soumissionnaire.Iden_Ope = request.POST['Iden_Ope']
        soumissionnaire.Raison_Soci = request.POST['Raison_Soci']
        soumissionnaire.Statut_Juri = request.POST['Statut_Juri']

    return  render(request, "UpdateSoum.html")

