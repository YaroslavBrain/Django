from django.http import HttpResponse


def index(request):
    return HttpResponse("FirstApp`s page")


def categories(request, cat_id: int = 0):
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
            resp = """<ul type="square">
        <li>Category 1    
        <ul>
            <li>Article 1.1
            <li>Article 1.2
            <li>Article 1.3
            <li>Article 1.4
        </ul>
        <li>Category 2    
        <ul>
            <li>Article 2.1
            <li>Article 2.2
            <li>Article 2.3
            <li>Article 2.4
        </ul>
    </ul>"""

    return HttpResponse(f"""<h1>Articles by category</h1> 
    {resp}
    """)
