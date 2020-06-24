from django.http import HttpResponse as httpR
from django.shortcuts import render
import operator

def home(Request):
    return render(Request,'home.html')

def count(Request):
    Full_text  = Request.GET['FullText']
    FullText_List = Full_text.split()
    Dictionory = {}
    for word in FullText_List:
        if word in Dictionory:
            Dictionory[word]+=1
        else:
            Dictionory[word] = 1

    SortedList = sorted(Dictionory.items() , key=operator.itemgetter(1), reverse=True)
    return render(Request,'count.html',{'FullText':Full_text , 'Count':len(FullText_List),'Dictionary':SortedList})

def about(Request):
    return render(Request,'about.html')