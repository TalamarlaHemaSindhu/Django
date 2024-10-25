from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def csearch(request,pid):
    chiru=[{'id':1,'name':"indra",'dialogue':"mokke kadha ani pikesthe peeka kostha"},
    {'id':2,'name':"shankardada",'dialogue':"In front there is crocodile fesival"},
    {'id':3,'name':"gangleader",'dialogue':"cheyyi chusava entha rough ga undho raffadistha"},
    {'id':4,'name':"brucelee",'dialogue':"just time gap anthe timing lo gap vundadhu"},
    ]

    
    result=None
    for item in chiru:
        if item.get('id')==pid:
            result=item
            break
    if result is not None:
        return HttpResponse(f"<p>name:{result.get('name')}<br>dialogue:{result.get('dialogue')}</p>")
    else:
        return HttpResponse("enti ah cinema cheyaledha")
def bsearch(request,pid):
    balayya=[{'id':1,'name':"legend",'dialogue':"flute jinka mundhu udhu simham mundhu kaadhu"},
    {'id':2,'name':"narasimhareddy",'dialogue':"katthulatho kaadhura kanti chuputho champestha"},
    {'id':3,'name':"simha",'dialogue':"kodithe medical test lu chepinchukovataniki mee asthulu ammina saripovu"},
    {'id':4,'name':"veerasimhareddy",'dialogue':"go neeku government order naaku gods ordder"},
    ]

    
    result=None
    for item in balayya:
        if item.get('id')==pid:
            result=item
            break
    if result is not None:
        return HttpResponse(f"<p>name:{result.get('name')}<br>dialogue:{result.get('dialogue')}</p>")
    else:
        return HttpResponse("Sar sarle chala movies chesam adhi okati cheyakapothe emanna avuthundha enti")


def psearch(request,pid):
    pk=[{'id':1,'name':"attarintikidaredhi",'dialogue':"naakoncham tikkundhi, kaani daniko lekkundhi"},
    {'id':2,'name':"gabbarsingh",'dialogue':"nenu cheppina okate naa fans cheppina okate"},
    {'id':3,'name':"gopalagopala",'dialogue':"nenu time ki ravadam kaadhu mithrama nenu vachake time vasthundhi"},
    
    {'id':4,'name':"rambabu",'dialogue':"nuvu pm ayithe enti cm ayithe enti"},
    ]

    
    result=None
    for item in pk:
        if item.get('id')==pid:
            result=item
            break
    if result is not None:
        return HttpResponse(f"<p>name:{result.get('name')}<br>dialogue:{result.get('dialogue')}</p>")
    else:
        return HttpResponse("nuvvu cheppindhi correct ayithe ah dialogue a chupisthundhi")

# Create your views here.
