from django.contrib.auth import REDIRECT_FIELD_NAME, login, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from blog.forms import (
    CommentForm,
    ArticleForm,
    ProfileForm
)
from blog.models import (
    Article,
    Profile,
    Comment
)


class IndexView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'articles_list'
    paginate_by = 3
    ordering = ['-pub_date']


class NewArticle(LoginRequiredMixin, CreateView):
    form_class = ArticleForm
    template_name = 'new_article.html'
    login_url = reverse_lazy('blog:login')
    redirect_field_name = REDIRECT_FIELD_NAME

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NewArticle, self).form_valid(form)


class ArticleView(DetailView):
    model = Article
    template_name = 'article.html'


class NewComment(LoginRequiredMixin, CreateView):
    form_class = CommentForm
    template_name = 'new_comment_form.html'
    login_url = reverse_lazy('blog:login')
    redirect_field_name = REDIRECT_FIELD_NAME

    def form_valid(self, form):
        form.instance.article = get_object_or_404(Article, pk=self.kwargs['pk'])
        if 'comment_key' in self.kwargs:
            form.instance.parent_comment = get_object_or_404(Comment, pk=self.kwargs['comment_key'])
        form.instance.user = self.request.user
        return super(NewComment, self).form_valid(form)


class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        res = super(SignUp, self).form_valid(form)
        login(self.request, self.object)
        return res


class PersonView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'person.html'
    context_object_name = 'person'

    # login_url = reverse_lazy('blog:login')
    # redirect_field_name = REDIRECT_FIELD_NAME


class PersonEditView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'person_edit.html'

    login_url = reverse_lazy('blog:login')
    redirect_field_name = REDIRECT_FIELD_NAME

    def get_success_url(self):
        return reverse('blog:person', kwargs=self.kwargs)

    def dispatch(self, *args, **kwargs):
        if self.kwargs['pk'] != self.request.user.pk:
            raise PermissionDenied
        return super(PersonEditView, self).dispatch(*args, **kwargs)
