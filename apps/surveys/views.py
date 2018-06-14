from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited

def index(request):
    return render(request, 'surveys/index.html')

def process(request):
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        return redirect('/result')

def result(request):
    #context = {
        #'name': request.session['name'],
        #'location': request.session['location'],
        #'language': request.session['language'],
        #'comment': request.session['comment'],
    #}
    return render(request, 'surveys/result.html')

# Create your views here.
