from django import forms


"""
    ici il y aura les formulaires de tout le projet
    pour le moment il n'y a que le formulaire d'upload du pdf a netoter 
    mais il pourrais em avoir plus ;)
"""
class UploadFileForm(forms.Form):
    #recuperer le nom du fichier dans un champ de teste de 50 caractere maxi
    file_name = forms.CharField(max_length=50)
    #recuperer le fichier a proprement parler dans un champ file
    file = forms.FileField()