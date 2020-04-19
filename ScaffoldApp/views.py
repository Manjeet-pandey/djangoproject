from django.shortcuts import render,redirect
from ScaffoldApp.models import *
from ScaffoldApp.forms import *


# Create your views here.
def index(request):
    return render(request,'ScaffoldApp/index.html')

def addProduct(request):
    form=addProductForm()
    if request.method=='POST':
      form =addProductForm(request.POST)
      if form.is_valid():
          form.save()
          return redirect('/home')
    return render(request,'ScaffoldApp/addProduct.html',
                  {
                      'form':form
                      }
                  )

def addProject(request):
    form=addProjectForm()
    if request.method=='POST':
      form=addProjectForm(request.POST)
      if form.is_valid():
          form.save()
          return redirect('/home')
    return render(request,'ScaffoldApp/addProject.html',
                  {
                      'addprojectform':form
                      }
                  )

def displayProject(request):
    project=AddProject.objects.all()
    return render(request,'ScaffoldApp/displayProject.html',
                  {
                      'project':project
                      }
                  )

def addSupplier(request):
    form=addSupplierForm()    
    if request.method=='POST':
        form=addSupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    return render(request,'ScaffoldApp/addSupplier.html',
           {
               'addSupplierform':form
               }
           )

def viewAll(request):
    return render(request,'ScaffoldApp/viewAll.html')

def approve(request):
    return render(request,'ScaffoldApp/approve.html')
 
def payment(request):
    return render(request,'ScaffoldApp/payment.html')