from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    res = 'hi, friend! where a u from?'
    from_source = request.session.get('from_source', 'unkown')
    res = 'hi, friend! u come from %s' %from_source
    return HttpResponse(res)
