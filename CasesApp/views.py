from django.shortcuts import render, redirect
from .forms import CasesForm
from .models import CasesModel
from django.db.models import Q

def ViewUploadFile(request):
    form = CasesForm()
    results = CasesModel.objects.all()
    if request.method == 'POST':
        if "btnSubmit" in request.POST:
            form = CasesForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
        elif "btnSearch" in request.POST:
            print("button search clicked")
            if request.method == 'POST':
                if "btnSearch" in "POST":
                    CaseStudyNumber = request.POST.get('CaseStudyNumber')
                    CaseStudyFileName = request.POST.get('CaseStudyFileName')
                    results = CasesModel.objects.filter(Q(CaseStudyFileName__icontains=CaseStudyFileName) | Q(CaseStudyNumber__icontains=CaseStudyNumber))
                    
    else:
        form = CasesForm()
    
    return render(request, 'CasesApp/casos.html', {'form': form,'result':results})
