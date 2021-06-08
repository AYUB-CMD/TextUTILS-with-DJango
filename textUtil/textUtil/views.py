from django.http import HttpResponse
from django.shortcuts import render

def index(request):
  
  return render(request,'index.html')
    

def analyze(request):
  #get the text
  djtext=request.POST.get('text','default')

  # checkbox value
  removepunc=request.POST.get('removepunc','off')
  fulcap=request.POST.get('fulcap','off')
  newlineremover=request.POST.get('newlineremover','off')
  spaceremover=request.POST.get('spaceremover','off')
  # charcount=request.POST.get('charcount','off')

  #removepunctuation
  if removepunc == "on":
    punctuations=''' ()-[]{};:"'\,<>?!@`~#$%^^&* '''
    # analyzed=djtext
    analyzed=""
    for char in djtext:
     if char not in punctuations:
      analyzed=analyzed+char
    params={'purpose':'Removed Punctuation','analyzed_text':analyzed}
    djtext=analyzed
    
    # return render(request, 'analyze.html',params) 

  #Capitalize 
  if(fulcap=='on'):
    analyzed=""
    for char in djtext:
      analyzed=analyzed+char.upper()
      params={'purpose':'Changed to Capitalize','analyzed_text':analyzed}
      djtext=analyzed
    # return render(request, 'analyze.html',params) 

  # new line remover
  if(newlineremover=='on'):  
      analyzed=""
      for char in djtext:
        if char != '\n' and char != '\r':
          analyzed=analyzed+char
        params={'purpose':'Changed to Newline Removed','analyzed_text':analyzed}
        djtext=analyzed
      # return render(request, 'analyze.html',params) 

  # extra space remover
  if(spaceremover=='on'):
    analyzed=""
    for index,char in enumerate(djtext):
      if not (djtext[index] ==" " and djtext[index+1] == " "):
         analyzed=analyzed+char
         params={'purpose':'Changed to Extra Space Removed','analyzed_text':analyzed}
         djtext=analyzed
    # return render(request, 'analyze.html',params) 
  

  if(removepunc!='on'and fulcap!='on'and newlineremover !='on' and spaceremover !='on' and charcount !='on' ):
    return HttpResponse("ERROR! PLEASE SELECT ANY OPERATION AND TRY AGAIN") 
 
  return render(request, 'analyze.html',params) 

  
  

  
  

  
  



# def cap(request):
#   return HttpResponse("capfirst")   

# def newlineremove(request):
#   return HttpResponse("newline")   

# def spaceremove(request):
#   return HttpResponse("space")   

# def charcount(request):
#   return HttpResponse("charcount")     
   



# exercise 1 personal nav
# def per(request):
  # return HttpResponse('''<h1><a href="https://github.com/AYUB-CMD">personal nav</a></h1>''')    