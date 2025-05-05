from django.shortcuts import render
from django.http import HttpResponse
import pandas
import json
# Create your views here.
def home(request):
    return render(request,"home.html")



def read_file(request):
  
    if request.method=="POST":
        request.session.flush()
        # file=request.POST["file"];
        my_uploaded_file = request.FILES['file']
        if  "csv"  in my_uploaded_file.name   :
           data= pandas.read_csv(my_uploaded_file)
           request.session["data"]=data.to_json()
           len_=len(data)

        elif  "xlsx" in my_uploaded_file.name :    
           data= pandas.read_excel(my_uploaded_file)
           len_=len(data)

           request.session["data"]=data.to_json()

     
        request.session["len"]=len_

        temp= pandas.read_json(request.session.get("data")).head(10)     
    
       

    if request.method=="GET":
       
        
        columns=request.GET.getlist('columns')
       
        request.session["columns"]=json.dumps(columns)
        print("fff",request.session.get("columns"))

        temp=pandas.read_json(request.session.get("data"))[list(columns)].head(10)
     
    return render(request,"table.html",{"data":temp,"columns":pandas.read_json(request.session.get("data")).columns,"range":range(1,10)})#.to_html() 



    # forloop.counter
    # forloop.counter0
    # forloop.first
    # forloop.last
    # forloop.parentloop
    # forloop.revcounter
    # forloop.revcounter0

def pagination(request):

    page=int(request.GET.get("page"))
    limit=int(request.GET.get("limit"))

    a=(page-1)*limit
    b=a+(limit-1)
    data2=pandas.read_json(request.session.get("data")).copy()
    temp=data2.loc[a:b,eval(request.session.get("columns"))]
    print(str(page),str(limit),str(a),str(b))
    # len_=int(request.session.get("len"))
 
    return render(request,"table.html",{"data":temp,"columns":pandas.read_json(request.session.get("data")).columns,"range":range(1,10)})#.to_html() "range":range(1,len_,10)

# def read_file_by_columns (request):
#        if request.method=="POST":
#         # file=request.POST["file"];
#         my_uploaded_file = request.FILES['file']
#         if  "csv"  in my_uploaded_file.name   :
#             data= pandas.read_csv(my_uploaded_file).head(10) 
#         elif  "xlsx" in my_uploaded_file.name :    
#             data= pandas.read_excel(my_uploaded_file).head(10) 
            
#         # print(my_uploaded_file.name)




#     return render(request,"table.html",{"data":data})#.to_html()


# file = request.FILES['filename']
# file.name           # Gives name
# file.content_type   # Gives Content type text/html etc
# file.size           # Gives file's size in byte
# file.read()         # Reads file

# print(request.FILES.items())
# for filename, file in request.FILES.items():
#     print(filename, file)

# for filename, file in request.FILES.iteritems():
#     name = request.FILES[filename].name