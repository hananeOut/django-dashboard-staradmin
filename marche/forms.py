from .models import Consultation

class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ["Nouvelle_Relance","N_Dossier","A_N_Dossier","Designation",
                  "Type_Operation","Nom_Agent_Tech","PV_Eval","PV_Ouvert","System_Eval",
                  "date_Fich_Tech","Fich_Tech_valid","date_Ouvert"]