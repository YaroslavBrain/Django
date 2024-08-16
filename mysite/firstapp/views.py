from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

def index(request):
    t = render_to_string("firstapp/index.html")
    return HttpResponse(t)


def about(request):
    return render(request, "firstapp/about.html")

def categories(request):
    return render(request, 'firstapp/categories.html')

def categories_certain(request, cat_id: int = 0):
    match cat_id:
        case 1:
            resp = """Category 1    
        <ul>
            <li>Article 1.1
            <li>Article 1.2
            <li>Article 1.3
            <li>Article 1.4
        </ul>"""
        case 2:
            resp = """Category 2    
        <ul>
            <li>Article 2.1
            <li>Article 2.2
            <li>Article 2.3
            <li>Article 2.4
        </ul>"""
        case _:
            return redirect('cats', permanent=True)

    return HttpResponse(f"""<h1>Articles by category</h1> 
    {resp}
    """)

def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)

    return HttpResponse(f"<h1>Categories by slug</h1><p>{cat_slug}</p>")



def archive(request, year):
    if year >= 2025 or year <= 2020:
        raise Http404()
    return HttpResponse(f"<h1>Archive by year</h1><p>{year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Where did you get this url?</h2>")