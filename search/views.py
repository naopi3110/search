from django.shortcuts import render
from .forms import playerForm
from . import forms
import pandas as pd


def form(request):
    form = playerForm()
    return render(request,'search/form.html',{'form': form,}) 

def form1(request):
    form = playerForm()
    return render(request,'search/form1.html',{'form': form,}) 

def form2(request):
    form = playerForm()
    return render(request,'search/form2.html',{'form': form,})

def form3(request):
    form = playerForm()
    return render(request,'search/form3.html',{'form': form,})

def form4(request):
    form = playerForm()
    return render(request,'search/form4.html',{'form': form,})

def form5(request):
    form = playerForm()
    return render(request,'search/form5.html',{'form': form,}) 

def form6(request):
    form = playerForm()
    return render(request,'search/form6.html',{'form': form,}) 

def form7(request):
    form = playerForm()
    return render(request,'search/form7.html',{'form': form,}) 



def serch(enter, df):
    N = []
    Q = []
    A = []
    for i in range(len(df.index)):
        question = str(df.iloc[i,0])
        n = len(enter)
        question_n = question[0:n]
        if question_n == enter:
            number = i + 2
            q = df.iloc[i,0]
            a = df.iloc[i,1]
            N.append(number)
            Q.append(q)
            A.append(a)
            
            if len(question) < n:
                m = len(question)
                enter_m = enter[0:m]
                if question == enter_m:

                    number = i + 2
                    q = df.iloc[i,0]
                    a = df.iloc[i,1]
                    N.append(number)
                    Q.append(q)
                    A.append(a)

    list = {'number':N, 'question':Q, 'answer':A}
    return list




def index(request):
    form = forms.playerForm(request.GET or None)
    df = pd.read_excel('search/web_test.xlsx', sheet_name='玉手箱（非言語・空欄補助）')
    if form.is_valid():
        word = {
            'word': request.GET.get('word'),
        }
        enter = word["word"]
        list = serch(enter, df)
        print(list)
    
    return render(request, 'search/index.html',list)

def index1(request):
    form = forms.playerForm(request.GET or None)
    df = pd.read_excel('search/web_test.xlsx', sheet_name='玉手箱（非言語・図表読み取り）')
    if form.is_valid():
        word = {
            'word': request.GET.get('word'),
        }
        enter = word["word"]
        list = serch(enter, df)
        print(list)
    
    return render(request, 'search/index1.html',list)

def index2(request):
    form = forms.playerForm(request.GET or None)
    df = pd.read_excel('search/web_test.xlsx', sheet_name='玉手箱（言語） ')
    if form.is_valid():
        word = {
            'word': request.GET.get('word'),
        }
        enter = word["word"]
        list = serch(enter, df)
        print(list)
    
    return render(request, 'search/index2.html',list)

def index3(request):
    form = forms.playerForm(request.GET or None)
    df = pd.read_excel('search/web_test.xlsx', sheet_name='玉手箱（英語）')
    if form.is_valid():
        word = {
            'word': request.GET.get('word'),
        }
        enter = word["word"]
        list = serch(enter, df)
        print(list)
    
    return render(request, 'search/index3.html',list)

def index4(request):
    form = forms.playerForm(request.GET or None)
    df = pd.read_excel('search/web_test.xlsx', sheet_name='TG-WEB（言語）')
    if form.is_valid():
        word = {
            'word': request.GET.get('word'),
        }
        enter = word["word"]
        list = serch(enter, df)
        print(list)
    
    return render(request, 'search/index4.html',list)

def index5(request):
    form = forms.playerForm(request.GET or None)
    df = pd.read_excel('search/web_test.xlsx', sheet_name='TG-WEB(数学)')
    if form.is_valid():
        word = {
            'word': request.GET.get('word'),
        }
        enter = word["word"]
        list = serch(enter, df)
        print(list)
    
    return render(request, 'search/index5.html',list)

def index6(request):
    form = forms.playerForm(request.GET or None)
    df = pd.read_excel('search/web_test.xlsx', sheet_name='GAB（言語・テレ朝系）')
    if form.is_valid():
        word = {
            'word': request.GET.get('word'),
        }
        enter = word["word"]
        list = serch(enter, df)
        print(list)
    
    return render(request, 'search/index6.html',list)

def index7(request):
    form = forms.playerForm(request.GET or None)
    df = pd.read_excel('search/web_test.xlsx', sheet_name='GAB（英語）')
    if form.is_valid():
        word = {
            'word': request.GET.get('word'),
        }
        enter = word["word"]
        list = serch(enter, df)
        print(list)
    
    return render(request, 'search/index7.html',list)



