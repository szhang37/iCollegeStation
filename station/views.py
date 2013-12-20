from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from models import School
from models import Category
from models import Course
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import Comment
from models import Catcnt
import random,string


def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('station/index.html', context_dict, context)

def courses(request):
    context = RequestContext(request)
    
    catid = request.GET.get('catid')
    sid = request.GET.get('sid')
    isSchool = None
    isCat = None
    if sid:
        course_list = Course.objects.filter(s_id=sid)
        isSchool = School.objects.filter(s_id=sid)
    elif catid:
        course_list = Course.objects.filter(cat_id=catid)
        isCat = Category.objects.filter(cat_id=catid)
    else:    
        course_list = Course.objects.all()
    paginator = Paginator(course_list, 30) # Show 25 contacts per page
    
#     for course in course_list:
#         for i in range(0, 15):
#             com = Comment(name = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(6)), content = ''.join(random.choice(string.ascii_lowercase) for x in range(random.randrange(0, 50))), c_id = course.c_id)
#             com.save()
    page = request.GET.get('page')
    
    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        courses = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        courses = paginator.page(paginator.num_pages)

    return render_to_response('station/course_list.html', {"courses": courses, "isschool": isSchool, "iscat": isCat})

def course(request):
    context = RequestContext(request)
    cid = request.GET.get('cid')
    if request.method == 'POST': # If the form has been submitted...
        na = request.POST.get('name')
        con = request.POST.get('content')
        print "content:"+con
        if na or con:
            com = Comment(name =na, content =con, c_id = cid)
            com.save()

    course = Course.objects.filter(c_id = cid)
    comments  = Comment.objects.filter(c_id = cid)

    return render_to_response('station/course.html', {"course": course, "comments":comments}, context)

def school(request):
    context = RequestContext(request)
    sch = []
    lastsch =[]
    schools = School.objects.all()
    l = School.objects.count()/3
    for i in range(0, l+1):
        if i<l:
            sch.append([schools[3*i],schools[3*i+1],schools[3*i+2]])
        else:
            if School.objects.count()%3==1:
                lastsch.append(schools[3*i])
            elif School.objects.count()%3==2: 
                lastsch.append(schools[3*i],schools[3*i+1])
    
    print sch, lastsch
    context_dict = {'schools': sch, 'lastsch':lastsch}
    return render_to_response('station/school.html', context_dict, context)


def category(request):
    context = RequestContext(request)
    alphabet = []
    letters = []
    context_dict = {}
    
    for c in range(65,90):
        cats = Category.objects.filter(catname__istartswith=str(chr(c)))
        alphabet.append(cats)
        letters.append(str(chr(c)))
#         for cat in cats:
#             print cat.catname
    catcnt = Catcnt.objects.all()
        
    context_dict["alph"] =  alphabet
    context_dict["letter"] =  letters
    context_dict["cnt"] =  catcnt
    return render_to_response('station/category.html', context_dict, context)

def about(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('station/about.html', context_dict, context)

