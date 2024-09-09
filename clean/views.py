from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UploadFileForm
from .modules import * 



def index (request):
    """
    cette view s'occupe de recuperer le fichier upload et de renvoyer une
    reponce http contenant le template vide

    Args:
        request (undefined): la requette http

    """
    if request.method == "POST":
        #recupérer les données du formulaire
        form = UploadFileForm(request.POST, request.FILES)
        #vérifier la validiter du fomulaire
        if form.is_valid():
            #recupérer le nom du fichier entrer dans le formulaire
            file_name = request.POST['file_name']
            #uploadFile(request.FILES["file"], file_name)
            fName = clean(request.FILES["file"], file_name) #créer le template en appelant la fonction clean
            mine_type = "application/pdf" #determiner le type de fichier a envoyer dans la reponce
            response = HttpResponse(fName, content_type=mine_type) # construire la reponce http
            response['Content-Disposition'] = "attachement; filename= template_" + file_name + ".pdf" #customiser la reponce http en ajoutant le nom du fichier 
            return response
            
    else:
        form = UploadFileForm() #si il n'y a pas de requette post , renvoyer le formulaire vierge
    return render(request, "index.html", {"form": form}) # rendre le template index.html avec comme variable notre formulaire

