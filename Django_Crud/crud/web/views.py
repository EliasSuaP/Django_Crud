from django.shortcuts import render
from .models import Album, Artist, Track

# Create your views here.

# OPCION CON lookup (__in)
def index(request):
    """ 
    Instancia de todos los artistas para entregarlos al template en el select.
    Al seleccionar un artista mediante el envío de formulario se recoge el valor del id
    envido en el value del select se filtran los albums por el id del artista,
    y se filtran las canciones utilizando un lookup __in para recorrer cada album y encontrar sus canciones.
    Entrega todas las bandas, albums y canciones al template.
    """
    bandas = Artist.objects.all()

    if request.method == 'POST':
        artist = request.POST['banda_id']
        albums = Album.objects.filter(artistid=artist)
        canciones = Track.objects.filter(albumid__in=albums)

        return render(request, 'index.html', {'bandas': bandas, 'albums': albums, 'canciones': canciones})
    
    else:

        return render(request, 'index.html', {'bandas': bandas})


# OPCION CON .extend()
# def index(request):
#     bandas = Artist.objects.all()

#     if request.method == 'POST':
#         artist= request.POST.get('banda_id')
#         albums = Album.objects.filter(artistid=artist)
#         canciones = []
#         for album in albums:
#             canciones.extend(Track.objects.filter(albumid=album))

#             # canciones = Track.objects.filter(albumid=album)

#         return render(request, 'index.html', {'bandas': bandas, 'albums': albums, 'canciones': canciones})
    
#     else:

#         return render(request, 'index.html', {'bandas': bandas})
    
# OPCION CON .append()
# def index(request):
#     bandas = Artist.objects.all()

#     if request.method == 'POST':
#         artist_id = request.POST.get('banda_id')
#         albums = Album.objects.filter(artistid=artist_id)
        
#         canciones = []  # Lista para almacenar todas las canciones

#         for album in albums:
#             # Obtener todas las canciones del álbum actual y agregarlas a la lista
#             canciones_album = Track.objects.filter(albumid=album)
#             for cancion in canciones_album:
#                 canciones.append(cancion)

#         return render(request, 'index.html', {'bandas': bandas, 'albums': albums, 'canciones': canciones})
    
#     else:
#         return render(request, 'index.html', {'bandas': bandas})
    



def artistas(request):
    """ 
    Instancia de todos los artistas para entregarlo al template donde se renderiza una tabla 
    con todos los artistas.
    """
    artistas = Artist.objects.all()
    return render(request, 'artistas.html', {'artistas': artistas})
