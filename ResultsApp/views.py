from django.shortcuts import render
from StudentsApp.models import StudentPerformance, StudentPerfomranceInDemarcateQuizes
from .forms import StudentSearchForm
from django.db.models import Min

from django.db.models import Sum, F, DecimalField

from QuestionsApp.models import QuestionGroupModel

def ViewGetQuestionnaire(request):
    context = {}

    # Step 1: Find QuestionGroupModel instances created by the current logged-in user
    current_user = request.user
    question_groups_created_by_user = QuestionGroupModel.objects.filter(Creators_Information=current_user)

    # Step 2: Use those QuestionGroupModel instances to filter and get the earliest StudentPerformance objects
    earliest_student_performances = StudentPerformance.objects.filter(
        Question_Group_Information__in=question_groups_created_by_user
    ).values('Question_Group_Information').annotate(
        earliest_completed_at=Min('Completed_At')
    ).values('earliest_completed_at', 'Question_Group_Information')

    # Step 3: Fetch the corresponding StudentPerformance objects
    student_performances = StudentPerformance.objects.filter(
        Question_Group_Information__in=earliest_student_performances.values('Question_Group_Information'),
        Completed_At__in=earliest_student_performances.values('earliest_completed_at')
    )

# For Demarcate Questions Results

        # Step 2: Use those QuestionGroupModel instances to filter and get the earliest StudentPerformance objects
    earliest_student_performances = StudentPerfomranceInDemarcateQuizes.objects.filter(
        Question_Group_Information__in=question_groups_created_by_user
    ).values('Question_Group_Information').annotate(
        earliest_completed_at=Min('Completed_At')
    ).values('earliest_completed_at', 'Question_Group_Information')

    # Step 3: Fetch the corresponding StudentPerformance objects
    student_performances_demarcate = StudentPerfomranceInDemarcateQuizes.objects.filter(
        Question_Group_Information__in=earliest_student_performances.values('Question_Group_Information'),
        Completed_At__in=earliest_student_performances.values('earliest_completed_at')
    )

    context['student_performances_demarcate'] = student_performances_demarcate


    context['student_performances'] = student_performances

    return render(request, 'ResultsApp/Get_Questionnaire.html', context)






def ViewGetStudentDemarcateDoneQuestionnaire(request, pk):
    context = {}

    # Retrieve the QuestionGroupModel instance based on pk
    question_group = QuestionGroupModel.objects.get(pk=pk)

    # Get the names of students who attempted questions from the specified QuestionGroup
    student_names = StudentPerfomranceInDemarcateQuizes.objects.filter(
        Question_Group_Information=question_group
    ).values_list('Student_Information__username', flat=True).distinct()

    context['student_names'] = student_names
    context['question_group'] = question_group
    return render(request, 'ResultsApp/StudentDemarcateDoneQuestionnaire.html', context)



def ViewGetStudentDoneQuestionnaire(request, pk):
    context = {}

    # Retrieve the QuestionGroupModel instance based on pk
    question_group = QuestionGroupModel.objects.get(pk=pk)

    # Get the names of students who attempted questions from the specified QuestionGroup
    student_names = StudentPerformance.objects.filter(
        Question_Group_Information=question_group
    ).values_list('Student_Information__username', flat=True).distinct()

    context['student_names'] = student_names
    context['question_group'] = question_group

    return render(request, 'ResultsApp/StudentDoneQuestionnaire.html', context)

def ViewSearchStudentPerformance(request, pk):
    form = StudentSearchForm(request.GET)
    grouped_results = None
    total_score = None
    demarcate_grouped_results = None
    D_total_score = None

    username = pk

    student_performances = StudentPerformance.objects.filter(Student_Information__username=username)
    student_performances_D = StudentPerfomranceInDemarcateQuizes.objects.filter(Student_Information__username=username)

    # Annotate the total score for regular performances
    grouped_results = student_performances.values('Question_Group_Information__Name_Of_Group').annotate(
        total_score=Sum(F('Score_Per_Question'), output_field=DecimalField())
    )

    # Annotate the total score for demarcate performances
    demarcate_grouped_results = student_performances_D.values('Question_Group_Information__Name_Of_Group').annotate(
        total_score=Sum(F('Score_Per_Question'), output_field=DecimalField())
    )

    # Calculate the total scores for regular and demarcate performances
    total_score = sum(group['total_score'] for group in grouped_results)
    D_total_score = sum(D_group['total_score'] for D_group in demarcate_grouped_results)
    context = {
        'form': form,
        'Group_Information': grouped_results,
        'Total_Score': total_score,
        'Group_Information_Demarcate': demarcate_grouped_results,
        'Total_D_Score': D_total_score
        }

    return render(request, 'ResultsApp/search_student_performance.html', context)


def ViewStudentResults(request):
    student_performances = StudentPerformance.objects.filter(Student_Information=request.user)
    student_performances_D = StudentPerfomranceInDemarcateQuizes.objects.filter(Student_Information=request.user)

    # Annotate the total score for regular performances
    grouped_results = student_performances.values('Question_Group_Information__Name_Of_Group').annotate(
        total_score=Sum(F('Score_Per_Question'), output_field=DecimalField())
    )

    # Annotate the total score for demarcate performances
    demarcate_grouped_results = student_performances_D.values('Question_Group_Information__Name_Of_Group').annotate(
        total_score=Sum(F('Score_Per_Question'), output_field=DecimalField())
    )

    # Calculate the total scores for regular and demarcate performances
    total_score = sum(group['total_score'] for group in grouped_results)
    D_total_score = sum(D_group['total_score'] for D_group in demarcate_grouped_results)

    context = {
        'Group_Information': grouped_results,
        'Total_Score': total_score,
        'Group_Information_Demarcate': demarcate_grouped_results,
        'Total_D_Score': D_total_score
    }
    return render(request, 'ResultsApp/index.html', context)
