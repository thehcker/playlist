# from django.shortcuts import render, get_object_or_404
# from music.models import Album, Song

# # Create your views here.
# # '/music/'
# def home(request):
# 	all_albums = Album.objects.all()
# 	context = {'all_albums': all_albums}
# 	template = 'index.html'
# 	return render(request, template,context)

# # '/music/<album_id>/'
# def detail(request, album_id):
# 	album = get_object_or_404(Album, pk=album_id)
# 	return render(request, 'detail.html', {'album': album})

# def favorite(request, album_id):
# 	album = get_object_or_404(Album, pk=album_id)
# 	try:
# 		selected_song = album.song_set.get(pk=request.POST['song'])
# 	except(KeyError, Song.DoesNotExist):
# 		return render(request, 'detail.html', {
# 			'album':album,
# 			'error_message': 'You did not select a valid song',
# 			})
# 	else:
# 		selected_song.is_favorite = True
# 		selected_song.save()
# 		return render(request, 'detail.html', {'album': album})		

from django.views.generic import ListView, DetailView
from music.models import Album
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy

class IndexView(ListView):
	template_name = 'index.html'
	context_object_name = 'all_albums'

	def get_queryset(self):
		return Album.objects.all()

class DetailView(DetailView):
	model = Album
	template_name = 'detail.html'

class AlbumCreateView(CreateView):
	model = Album
	fields = ['artist', 'album_title', 'genre','album_logo']
	template_name = 'album_form.html'

class AlbumUpdate(UpdateView):
	model = Album
	fields = ['artist', 'album_title', 'genre','album_logo']
	# template_name = 'detail.html'
	success_url = reverse_lazy('index')

class AlbumDelete(DeleteView):
	model = Album
	success_url = reverse_lazy('index')	