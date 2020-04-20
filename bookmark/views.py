from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .models import Bookmark

class BookmarkListView(ListView):
    model = Bookmark #이 뷰 만들때 사용하는 모델은 bookmark이다
    paginate_by = 5 #한 페이지에 몇개의 리스트를 보일것인가

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url'] #이 두개의 값을 입력받겠다
    success_url = reverse_lazy('list') #북마크를 추가한 후에 어느 페이지로 이동할 것인가를 나타냄/url에서 name이 list인 곳으로 이동
    template_name_suffix = '_create' #해당 리스트 뷰로 이동하여 해당 html파일이 bookmark_create로 찾아감

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'
    #models.py에서 업데이트 이후 어디로 가야할지 지정해줌

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')
