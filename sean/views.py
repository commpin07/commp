from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Item
from django.views.generic.detail import DetailView
from .forms import ItemAnswerForm, SuggestionForm
from django.db.models import F
import string
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.core.paginator import Paginator
from collections import Counter


# Create your views here.


def index(request):
    item_list = Item.objects.all().order_by('-id')
    p = Paginator(item_list, 9)
    page = request.GET.get('page')
    item_list = p.get_page(page)
    user = request.user
    context= {
		'item_list':item_list,
		'user': user,
	}
    return render(request, 'sean/index.html', context)

# class ContentDetail(DetailView):
#        model = Item
#        template_name = 'sean/detail.html'

@login_required
def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemAnswerForm(request.POST, instance=item)
    item.item_answercount = F('item_answercount') + 1
    item.save()
    
    if form.is_valid():
        form.save()
        return redirect('sean:feedback', id=item.id)     
    return render(request, 'sean/answer_form.html', {'form':form, 'item':item}) 


def feedback(request,id):
    itemli = Item.objects.get(id=id)
    item = Item.objects.values_list('item_answer').get(id=id)
    
    with open('sean/read.txt', 'w') as f:
        
        item_list = str(item)
       
        f.write(item_list)

    text = open('sean/read.txt').read() 
    lower_case = text.lower()   
    cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
    
    
    tokenized_words = cleaned_text.split()
    

    stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "or", "because", "as",
              "of", "at", "by", "for", "with", "about", "against", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "here", "there", "any", "both", "each",
              "few", "other", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "s", "t", "can", "will", "just", "don"]

    final_words = []
    for word in tokenized_words:
        if word not in stop_words:
            final_words.append(word)

    
    emotion_list = {}
    with open('sean/emotions.txt', 'r') as f:
        for line in f:
            clear_line = line.replace("\n",'').replace(",",'').replace("'",'').strip()
            word, emotion = clear_line.split(':')
            d = {word:emotion}

            if word in final_words:
                emotion_list.update(d)

    emotion_c1 = []
    with open('sean/emotions.txt', 'r') as file:
        for line in file:
            clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
            word, emotion = clear_line.split(':')
            
            if word in final_words:
                emotion_c1.append(emotion)


    w = Counter(emotion_c1)
    
    
    zjs2 = str(w)
    str_g = str(zjs2)[9: -2]
   

    zjs = str(emotion_list).replace(',',' ... ')
    str_q = str(zjs)[1 : -1]

    if (len(emotion_list) == 0):
        return render(request, 'sean/sorry.html',{'itemli':itemli})  
    else:
        return render(request, 'sean/feedback.html',{'itemli':itemli, 'str_q':str_q, 'str_g':str_g})      
    
    # return render(request, 'sean/feedback.html',{'itemli':itemli, 'emotion_list':emotion_list})      

def suggestions(request):
    
    form = SuggestionForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('sean:index')
    return render(request, 'sean/suggestion_form.html', {'form':form})     