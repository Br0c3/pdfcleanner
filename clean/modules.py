from pypdf import PdfReader, PdfWriter # module utiliser pour travailler le pdf
from django.conf import settings
from io import BytesIO

def uploadFile(f, file_name:str):
    """
    peut etre utiliser pour stocker le fichier directement sur le disque cote server
    mais n'est pas utilser ici par soucie de transparance

    Args:
        f (objet file): objet fichier avec le contenue du fichier upload
        file_name (str): le nom du fichier 

    """
    with open(settings.BASE_DIR / file_name , "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def clean(file_name, title):
    """
    la fonction qui supprime le text dans un fichier fichier pdf 

    Args:
        file_name (objet file): objet file contenant le fichier uploader
        title (str): nom du fichier 
    """
    reader = PdfReader(file_name) # creer le reader du pdf upload
    writer = PdfWriter(file_name) # creer le writer du pdf upload
    writer.clone_document_from_reader(reader) # cLoner le reader dans le writer 
    writer.remove_text() # supprimer le texte du writer
    out = BytesIO() # creer l'objet ByteIO pour eviter de stocker le fichier( impossible de retourner un objet writer)
    writer.write(out) # ecrire le writer dans le ByteIO
    return out.getbuffer() # retourner le buffer du ByteIO
    