from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Item
from django.views.generic.detail import DetailView
from .forms import ItemAnswerForm, SuggestionForm
from django.db.models import F
import string
import csv
from django.shortcuts import render_to_response
from collections import Counter

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer



# import matplotlib.pyplot as plt



# Create your views here.


def index(request):
    item_list = Item.objects.all()
    return render(request, 'sean/index.html', {'item_list':item_list})

class ContentDetail(DetailView):
       model = Item
       template_name = 'sean/detail.html'

def update_item(request,id):
    item = Item.objects.get(pk=id)
    form = ItemAnswerForm(request.POST, instance=item)
    item.item_answercount = F('item_answercount') + 1
    item.save()
    
    if form.is_valid():
        form.save()
        return redirect('sean:detail', pk=item.id)     
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
    
    
    # tokenized_words = cleaned_text.split()
    tokenized_words = word_tokenize(cleaned_text, "english")
    # print(tokenized_words)

    # stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
    #           "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
    #           "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
    #           "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
    #           "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
    #           "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
    #           "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
    #           "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
    #           "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
    #           "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

    # final_words = []
    # for word in tokenized_words:
    #     if word not in stop_words:
    #         final_words.append(word)

         

    final_words = []
    for word in tokenized_words:
        if word not in stopwords.words('english'):
            final_words.append(word)

    # lemma_words = []
    # for word in final_words:
    #     word = WordNetLemmatizer().lemmatize(word)
    #     lemma_words.append(word)
        
    
    # emotion_list = {}
    # with open('sean/emotions.txt', 'r') as f:
    #     for line in f:
    #         clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
    #         word, emotion = clear_line.split(':')
    #         d = {word:emotion}
            
    #         if word in final_words:
    #             emotion_list.update(d)

    

    # emotion_list = {}
    # with open('sean/emotions.txt', 'r') as file:
    #     for line in file:
    #         clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
    #         word, emotion = clear_line.split(':')
    #         d = {word:emotion}
    #         if word in lemma_words:
    #             emotion_list.update(d)


    # with open('sean/test.txt', 'w') as f:
        
    #     item_lis = str(emotion_list)
       
    #     f.write(item_lis)

    # f = open('sean/test.txt', 'r')
    # file_contents = f.read()
    # f.close()    

    

    # print(emotion_list)

    # if (len(emotion_list) == 0):
    #     return render(request, 'sean/sorry.html',{'itemli':itemli})  
    # else:
    #     return render(request, 'sean/feedback.html',{'itemli':itemli, 'file_contents':file_contents})      
    
    
    
    # return render(request, 'sean/feedback.html',{'itemli':itemli, 'file_contents':file_contents})  
    return render(request, 'sean/feedback.html',{'itemli':itemli, 'final_Words':final_words})  

    
def suggestions(request):
    
    form = SuggestionForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('dtt:index')
    return render(request, 'dtt/suggestion_form.html', {'form':form})     