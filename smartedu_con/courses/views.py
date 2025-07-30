from django.shortcuts import render
from . models import Category, Course

def course_list(request):
    courses = Course.objects.all().order_by('-date')
    categories = Category.objects.all()
    context = {
        'courses': courses,
        'categories': categories
    }

    return render(request, 'courses.html', context)

def course_detail(request, category_slug, course_id):
    course = Course.objects.get(category__slug=category_slug, id=course_id)
    context = {
        'course': course
    }
    return render(request, 'course.html', context)

    #category__slug iki __ yazma sebebi, category alanının slug alanına göre filtreleme yapıyoruz.
    #context ile course_detail.html dosyasına course değişkenini gönderiyoruz.

def category_detail(request, category_slug):
    courses = Course.objects.all().filter(category__slug=category_slug)
    categories = Category.objects.all()
    context = {
        'courses': courses,
        'categories': categories
    }
    return render(request, 'courses.html', context)