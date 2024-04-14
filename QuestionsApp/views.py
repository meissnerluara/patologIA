from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import SelectQuestionTypeForm,CreateQuestionGroupForm,CreateQuestionsForm,EditQuestionsForm, CreateOptionForm,EditOptionForm
from .models import QuestionTypesModel,QuestionGroupModel, QuestionsModel,MCQModel
from ImagesApp.models import ImageModel
from AccountsApp.models import RoleModel
from django.http import HttpResponse


def teacher_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.Role == RoleModel.objects.get(Role_Type='estudante'):
            return redirect("HomeApp:HomePageView")
        return view_func(request, *args, **kwargs)
    return wrapper


@teacher_required
def ViewSelectQuestionType(request):
    form = SelectQuestionTypeForm()
    if request.method == 'POST':
        form = SelectQuestionTypeForm(request.POST or None)
        selected_option = form['Category'].value()
        
        try:
            question_type = QuestionTypesModel.objects.get(Id_Type_Question=selected_option)
        except QuestionTypesModel.DoesNotExist:
            return HttpResponse("Tipo de Questão inválida")

        if question_type.Category == "Questões de Demarcação de Imagens":
            return redirect('QuestionsApp:CreateQuestionGroupView')
        elif question_type.Category == "Questões de múltipla escolha":
            return redirect("QuestionsApp:CreateQuestionGroupView")
        else:
            return HttpResponse("Seleção errada")
    
    context = {'form': form}
    return render(request, 'QuestionsApp/SelectQuestionType.html', context)




@teacher_required
def ViewCreateQuestionGroup(request):
    Questionnaire_Objects = QuestionGroupModel.objects.filter(Creators_Information = request.user)

    form = CreateQuestionGroupForm()
    if request.method == 'POST':
        form = CreateQuestionGroupForm(request.POST or None)
        if form.is_valid():
            ins = form.save(commit=False)

            Is_Demarcate = request.POST.get('Is_Demarcate')
            ins.Is_Demarcate = Is_Demarcate
            
            Status = request.POST.get('status')
            ins.Online_Status = Status

            Creator = request.user
            ins.Creators_Information = Creator

            ins.save()
            if Is_Demarcate == 'True':
                return redirect('DemarcateApp:CreateDemarcateQuestionView')
            elif Is_Demarcate == 'False':
                return redirect('QuestionsApp:CreateQuestionView')
        else:
            print(form.errors)
    context = {'form':form, 'Questionnaire_Information': Questionnaire_Objects}
    return render(request, 'QuestionsApp/CreateQuestionsGroup.html', context)
@teacher_required
def ViewEditQuestionGroup(request, pk):
    question_obj = QuestionGroupModel.objects.get(Id_QuestionGroup = pk)
    form = CreateQuestionGroupForm(instance=question_obj)
    if request.method == 'POST':
        form = CreateQuestionGroupForm(request.POST, instance=question_obj)
        if form.is_valid():
            ins = form.save(commit=False)
            
            Status = request.POST.get('status')
            ins.Online_Status = Status

            Creator = request.user
            ins.Creators_Information = Creator

            ins.save()
            return redirect('QuestionsApp:CreateQuestionGroupView')
    context = {'form':form, 'Online_Status':str(question_obj.Online_Status)}
    return render(request, 'QuestionsApp/CreateQuestionsGroup.html', context)
@teacher_required
def ViewDeleteQuestionGroup(request, pk):
    question_obj = QuestionGroupModel.objects.get(Id_QuestionGroup = pk)
    question_obj.delete()
    return redirect('QuestionsApp:CreateQuestionGroupView')

@teacher_required
def ViewCreateQuestion(request):
    form = CreateQuestionsForm()
    editForm = EditQuestionsForm()
    if request.method == 'POST':
        if 'editButton' in request.POST:
            editForm = EditQuestionsForm(request.POST or None)
            get_question_number = request.POST.get('Question_Number')
            return redirect(reverse('QuestionsApp:EditQuestionView', kwargs={'question_number': str(get_question_number)} ))
        elif 'deleteButton' in request.POST:
            editForm = EditQuestionsForm(request.POST or None)
            get_question_number = request.POST.get('Question_Number')
            return redirect(reverse('QuestionsApp:DeleteQuestionView', kwargs={'question_number': str(get_question_number)} ))
        else:
            form = CreateQuestionsForm(request.POST or None)
            if form.is_valid():
                form.save()
                return redirect('QuestionsApp:CreateOptionView')
    context = {'form':form, 'eidtform':editForm}
    return render(request, 'QuestionsApp/CreateQuestion.html', context)

@teacher_required
def ViewEditQuestion(request,question_number):
    question_obj = QuestionsModel.objects.get(Question_Number = question_number)
    form = CreateQuestionsForm(instance=question_obj)
    if request.method == 'POST':
        form = CreateQuestionsForm(request.POST or None, instance=question_obj)
        if form.is_valid():
            form.save()
            return redirect('QuestionsApp:CreateQuestionView')
    context={'form':form}
    return render(request,'QuestionsApp/CreateQuestion.html', context)

@teacher_required
def ViewDeleteQuestion(request, question_number):
    question_to_delete = QuestionsModel.objects.get(Question_Number = question_number)
    question_to_delete.delete()
    return redirect('QuestionsApp:CreateQuestionView')

@teacher_required
def ViewImagesGrid(request):
    all_images = ImageModel.objects.all()
    context = {'list_of_images':all_images}
    return render(request, 'QuestionsApp/referencestemplates/ImagesGrid.html', context)

@teacher_required
def ViewCreateOption(request):
    form = CreateOptionForm()

    editForm = EditOptionForm()
    if request.method == 'POST':
        if 'btnCreateAnother' in request.POST:
            form = CreateOptionForm(request.POST or None)
            if form.is_valid():
                instance = form.save(commit = False)
                is_right = request.POST.get('status')
                instance.Is_Right = is_right
                instance.save()
                return redirect('QuestionsApp:CreateOptionView')
            else:
                print(form.errors)
        elif 'btnFinish' in request.POST:
            form = CreateOptionForm(request.POST or None)
            if form.is_valid():
                instance = form.save(commit = False)
                is_right = request.POST.get('status')
                instance.Is_Right = is_right
                instance.save()
                return redirect('QuestionsApp:CreateQuestionView')
            else:
                print(form.errors)
        elif 'btnEdit' in request.POST:
            editForm = EditOptionForm(request.POST or None)
            if editForm.is_valid():
                info = request.POST.get('Related_Question')
                return redirect(reverse('QuestionsApp:EditOptionView', kwargs={'pk': info}))
    context = {'form':form,'editForm':editForm}
    return render(request, 'QuestionsApp/CreateOption.html', context)

@teacher_required
def ViewEditOption(request, pk):
    get_option_value = MCQModel.objects.filter(Related_Question__Id_Question = pk).order_by('Option')
    if request.method == 'POST':
        for option in get_option_value:
            option_text = request.POST.get(str(option.Id_MCQs))
            option_selection = request.POST.get(option.Option)
            option.Is_Right = option_selection
            option.Option_Text = option_text
            option.save()
        return redirect('QuestionsApp:CreateOptionView')
    context = {'options':get_option_value}
    return render(request, 'QuestionsApp/EditOption.html', context)

@teacher_required
def ViewDeleteOption(request, pk):
    get_option = MCQModel.objects.get(Id_MCQs = pk)
    get_option.delete()
    return redirect('QuestionsApp:CreateOptionView')