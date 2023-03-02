from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import News, Category
from django.views.generic import TemplateView, ListView
from .forms import ContactForm


def news_list(request):
    news_list = News.published.all()

    context = {
        "news_list":news_list
    }
    return render(request, 'news/news_list.html', context)


def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)

    context = {
        'news': news,
    }
    return render(request, 'news/news_detail.html', context)



def homepage(request):
    categories = Category.objects.all()
    news_list = News.published.all().order_by('-publish_time')[:5]

    local_news = News.published.all().filter(category__name="Local").order_by('-publish_time')[:5]
    sport_news = News.published.all().filter(category__name="Sport").order_by('-publish_time')[:5]
    business_news = News.published.all().filter(category__name="Business").order_by('-publish_time')[:5]
    technology_news = News.published.all().filter(category__name="Technology").order_by('-publish_time')[:5]


    context = {
        'news_list': news_list,
        'categories': categories, 
        'local_news': local_news,
        'sport_news': sport_news,
        'technology_news': technology_news,
        'business_news': business_news
    }
    return render(request, 'home.html', context)

# class HomePageView(ListView):
    model = News
    template_name = 'home.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] = News.published.all().order_by('-publish_time')[:10]
        context['local_one'] = News.published.all().filter(category__name="Local").order_by('-publish_time')[:1]
        context['local_news'] = News.published.all().filter(category__name="Local").order_by('-publish_time')[1:6]
        return context


class LocalNewsView(ListView):
    model = News
    template_name = "news/local.html"
    context_object_name = "local_news"

    def get_queryset(self):
        news = News.published.all().filter(category__name="Local")
        return news



class SportNewsView(ListView):
    model = News
    template_name = "news/sport.html"
    context_object_name = "sport_news"

    def get_queryset(self):
        news = News.published.all().filter(category__name="Sport")
        return news



class TechnologyNewsView(ListView):
    model = News
    template_name = "news/technology.html"
    context_object_name = "technology_news"

    def get_queryset(self):
        news = News.published.all().filter(category__name="Technology")
        return news



class BusinessNewsView(ListView):
    model = News
    template_name = "news/business.html"
    context_object_name = "business_news"

    def get_queryset(self):
        news = News.published.all().filter(category__name="Business")
        return news


def contact_us(request):
    form = ContactForm(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return HttpResponse('<h2> Biz bilan bog\'langaningiz uchun tashakkur! </h2>')
    context = {
        'form': form
    }
    return render(request, 'additional/contact.html', context)


# class ContactPageView(TemplateView):
    template_name = 'contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'contact.html', context)
    
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid() and request.method == 'POST':
            form.save()
            return HttpResponse('<h2> Biz bilan bog\'langaningizdan minnatdormiz! </h2>')
        context = {
            'form': form
        }
        return render(request, 'contact.html', context)


def error_404(request):
    context = { }
    return render(request, 'additional/404.html', context)


def about_us(request):
    pass
    return render(request, 'additional/about.html')



# class NewsListview(ListView):
#     model = News
#     template_name = "news/news_list.html"
#     context_object_name = 'news_list'

# class NewsDetailView(DetailView):
    model = News
    template_name = "news/news_detail.html"
    context_object_name = "news"