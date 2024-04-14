from django.shortcuts import render, redirect
from QuestionsApp.models import QuestionTypesModel,QuestionsModel, QuestionGroupModel,MCQModel
from QuestionsApp.forms import SelectQuestionTypeForm
from StudentsApp.models import StudentPerformance, StudentPerfomranceInDemarcateQuizes
from AccountsApp.models import CustomUserModel
from .forms import GetQuestionnaireListForm

from django.urls import reverse
from django.http import HttpResponse
from django.db.models import Min, Sum

def ViewSelectQuestionType(request):
    form = SelectQuestionTypeForm()
    if request.method == 'POST':
        form = SelectQuestionTypeForm(request.POST or None)
        selected_option = form['Category'].value()

        try:
            question_type = QuestionTypesModel.objects.get(Id_Type_Question=selected_option)
        except QuestionTypesModel.DoesNotExist:
            return HttpResponse("Invalid question type")

        if question_type.Category == "Questões de Demarcação de Imagens":
            return redirect('DemarcateApp:GetDemarcateQuestionnaireListView')
        elif question_type.Category == "Questões de múltipla escolha":
            return redirect("StudentsApp:GetQuestionnaireListView")
        else:
            return HttpResponse("Wrong Selection")

    context = {'form': form}
    return render(request, 'QuestionsApp/SelectQuestionType.html', context)



def ViewGetQuestionnaireList(request):
    form = GetQuestionnaireListForm()
    if request.method == 'POST':
        get_questionnaire_id = request.POST.get('Name_Of_Group')
        return redirect(reverse('StudentsApp:GetQuestionsListView', kwargs = {'pk':str(get_questionnaire_id)}))
    context = {'form':form}
    return render(request, 'StudentsApp/GetQuestionnaireList.html', context)

def ViewGetQuestionsList(request, pk):
    Get_Student_Information = CustomUserModel.objects.get(Id_User = request.user.Id_User)
    Get_Group_Information = QuestionGroupModel.objects.get(Id_QuestionGroup = pk)
    Get_Question_Information = None
    List_Of_Questions = list(QuestionsModel.objects.filter(Group_Name_Of_Quesitons=pk))
    List_Of_Options = {}
    context = {}
    wrong_answer = False
    total_marks = 0
    score = 0
    final_marks = 0


    if 'index' not in request.session or 'tries' not in request.session:
        request.session['index'] = 0
        request.session['tries'] = 2

    get_index = int(request.session['index'])
    Get_Question_Information = List_Of_Questions[get_index]

    if str(Get_Question_Information.Type_Of_Question) == "Demarcate":
        print("It is a Demarcate Question")

    tries = request.session.get('tries')

    if request.method == 'POST':
        selected_option = request.POST.get('Question_Option')
        question_marks = List_Of_Questions[get_index].Question_Marks

        if selected_option == "True":
            wrong_answer = False
            score += question_marks if tries == 2 else question_marks/2
            print('1: '+str(score))
            # Add Model here
            save_performance =StudentPerformance(Student_Information = Get_Student_Information, Question_Information = Get_Question_Information, Question_Group_Information = Get_Group_Information, Score_Per_Question = score)
            save_performance.save()
        if selected_option == "False":
            if tries is None:
                tries = request.session.get('tries')
                tries = 2
            tries -= 1
            request.session['tries'] = tries
            if tries == 0:
                get_index += 1
                request.session['index'] = get_index
                request.session['tries'] = 2
                if get_index >= len(List_Of_Questions):
                    save_performance =StudentPerformance(Student_Information = Get_Student_Information, Question_Information = Get_Question_Information, Question_Group_Information = Get_Group_Information, Score_Per_Question = score)
                    save_performance.save()

                    return redirect('StudentsApp:CurrentQuestionnaireResultView', pk)
                    return redirect('StudentsApp:ResultView')
                    return HttpResponse(f'You have got {score} out of {total_marks}')
                else:
                    List_Of_Options = MCQModel.objects.filter(Related_Question__Id_Question = List_Of_Questions[get_index].Id_Question)
                    print('2: '+str(score))
                    # Add Model Here
                    save_performance =StudentPerformance(Student_Information = Get_Student_Information, Question_Information = Get_Question_Information, Question_Group_Information = Get_Group_Information, Score_Per_Question = score)
                    save_performance.save()
                    final_marks += score
                    context = {'Question':List_Of_Questions[get_index], 'Options':List_Of_Options, 'wrong_answer':wrong_answer, 'tries': request.session.get('tries'), 'current_score':score, 'Questionnaire_Name': Get_Group_Information, 'Total_Questions': str(len(List_Of_Questions)), 'current_question':get_index, 'Total_marks':final_marks}
                    return render(request, 'StudentsApp/GetQuestionsList.html', context)
            else:
                List_Of_Options = MCQModel.objects.filter(Related_Question__Id_Question = List_Of_Questions[get_index].Id_Question)
                wrong_answer = True
                score += question_marks if tries == 2 else question_marks/2
                print('3: '+str(score))
                final_marks += score
                context = {'Question':List_Of_Questions[get_index], 'Options':List_Of_Options, 'wrong_answer':wrong_answer, 'tries': tries, 'current_score':score, 'Questionnaire_Name': Get_Group_Information, 'Total_Questions': str(len(List_Of_Questions)), 'current_question':get_index, 'Total_marks':final_marks}
                return render(request, 'StudentsApp/GetQuestionsList.html', context)


        total_marks += question_marks
        get_index += 1
        request.session['index'] = get_index
        request.session['tries'] = 2

        if get_index >= len(List_Of_Questions):
            request.session['index'] = 0
            request.session['tries'] = 2
            return redirect('StudentsApp:CurrentQuestionnaireResultView', pk)

            return redirect('StudentsApp:ResultView')
            return HttpResponse(f'Não existem mais questões para exibir')

    if get_index >= len(List_Of_Questions):
        request.session['index'] = 0
        request.session['tries'] = 2
        final_marks += score
        context = {'score': score, 'total_marks': total_marks}
        return redirect('StudentsApp:CurrentQuestionnaireResultView', pk)
        #return render(request, 'StudentsApp/Result.html', context)
    else:
        List_Of_Options = MCQModel.objects.filter(Related_Question__Id_Question = List_Of_Questions[get_index].Id_Question)
        question = List_Of_Questions[get_index]
        if str(Get_Question_Information.Type_Of_Question) == "Demarcate":
            print("It is a Demarcate Question")

        total_marks = question.Question_Marks
        final_marks += score
        context = {'Question':question, 'Options':List_Of_Options, 'wrong_answer':wrong_answer, 'tries': request.session.get('tries'), 'current_score':score,  'Questionnaire_Name': Get_Group_Information, 'Total_Questions': str(len(List_Of_Questions)), 'current_question': str(get_index), 'Total_marks':final_marks}
        return render(request, 'StudentsApp/GetQuestionsList.html', context)

# Generate PDF

def ViewCurrentQuestionnaireResult(request, pk):
    # Get the earliest completed student performance for each question
    total_marks = 0
    get_result = StudentPerformance.objects.filter(
        Question_Group_Information=pk
    ).values(
        'Question_Information'
    ).annotate(
        earliest_completion=Min('Completed_At'),
        total_marks=Sum('Score_Per_Question')
    ).values(
        'earliest_completion', 'Question_Information', 'total_marks'
    ).order_by('earliest_completion')

    # Fetch the corresponding StudentPerformance objects and calculate total marks

    earliest_performances = [
        StudentPerformance.objects.filter(
            Question_Group_Information=pk,
            Question_Information=result['Question_Information'],
            Completed_At=result['earliest_completion']
        ).first()
        for result in get_result
    ]

    # Calculate the total marks only for the selected objects
    total_marks = sum(result['total_marks'] for result in get_result)

    context = {'Temp_Result': earliest_performances, 'Total_Marks': total_marks}
    return render(request, 'StudentsApp/CurrentQuestionnaireResult.html', context)



def ViewCurrentDemarcateQuestionnaireResult(request, pk):
    # Get the earliest completed student performance for each question
    total_marks = 0
    get_result = StudentPerfomranceInDemarcateQuizes.objects.filter(
        Question_Group_Information=pk
    ).values(
        'Question_Information'
    ).annotate(
        earliest_completion=Min('Completed_At'),
        total_marks=Sum('Score_Per_Question')
    ).values(
        'earliest_completion', 'Question_Information', 'total_marks'
    ).order_by('earliest_completion')

    # Fetch the corresponding StudentPerformance objects and calculate total marks

    earliest_performances = [
        StudentPerfomranceInDemarcateQuizes.objects.filter(
            Question_Group_Information=pk,
            Question_Information=result['Question_Information'],
            Completed_At=result['earliest_completion']
        ).first()
        for result in get_result
    ]

    # Calculate the total marks only for the selected objects
    total_marks = sum(result['total_marks'] for result in get_result)

    context = {'Temp_Result': earliest_performances, 'Total_Marks': total_marks}
    return render(request, 'StudentsApp/CurrentDemarcateQuestionnaireResult.html', context)

def ViewResult(request):
    if 'index' in request.session or 'tries' in request.session:
        del request.session['index']
        del request.session['tries']
    return render(request,'StudentsApp/Result.html')