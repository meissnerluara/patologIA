from django.urls import reverse
from django.shortcuts import render, redirect
from ImagesApp.models import ImageModel
from .forms import SelectImageForm, CreateDemarcateQuestionsForm,GetQuestionnaireListForm
from .models import DemarcateQuestion,DemarcateQuestionsModel
from QuestionsApp.models import QuestionGroupModel
from QuestionsApp.models import QuestionsModel
from django.http import HttpResponse
from StudentsApp.models import StudentPerformance, StudentPerfomranceInDemarcateQuizes
from AccountsApp.models import CustomUserModel

"""Questão de demarcação do lado do professor"""

"""Método Criando formulário de demarcação"""
def ViewCreateDemarcateQuestion(request):
    form = CreateDemarcateQuestionsForm()
    if request.method == 'POST':
        form = CreateDemarcateQuestionsForm(request.POST or None)
        form.save()
        return redirect('DemarcateApp:SelectImageView')
    context = {'form':form}
    return render(request, 'DemarcateApp/CreateQuestion.html', context)

"""Recebe a demarcação da Imagem através do método Post"""
def ViewSelectImage(request):
    form = SelectImageForm()
    if request.method == 'POST':
        form = SelectImageForm(request.POST or None)
        form.save(commit=False)
        Image_Number = request.POST.get('Question_Image')
        return redirect('DemarcateApp:CreateDemarcateAreaView', pk = Image_Number)
    context = {'form':form}
    return render(request, 'DemarcateApp/SelectImagePage.html', context)

# Demarcação de Area do lado do Professor
def ViewCreateDemarcateArea(request, pk):
    Image_Instance = ImageModel.objects.get(Id_Image = pk)
    Get_Questions = DemarcateQuestionsModel.objects.all()
    context = {'instance': Image_Instance, 'List_of_Questions': Get_Questions}

    """O método POST tras para o django os valores definidos no javascript e canvas"""
    if request.method == "POST":
        Width_Of_Marked_Area = request.POST.get('width')
        Height_Of_Marked_Area = request.POST.get('height')
        StartX_Of_Marked_Area = request.POST.get('startX')
        StartY_Of_Marked_Area = request.POST.get('startY')

        Total_Area = abs(int(Width_Of_Marked_Area) * int(Height_Of_Marked_Area))

        Question_ID = request.POST.get("Question_List")
        Question_Instance = DemarcateQuestionsModel.objects.get(Id_Question=str(Question_ID))

        Create_Object = DemarcateQuestion(StartX = StartX_Of_Marked_Area,StartY = StartY_Of_Marked_Area,Width = Width_Of_Marked_Area ,Height = Height_Of_Marked_Area, Area = Total_Area, Question_Image = Image_Instance, Related_Question = Question_Instance)
        Create_Object.save()

        return redirect('DemarcateApp:CreateDemarcateQuestionView')

    return render(request, 'DemarcateApp/TeacherDemarcate.html', context)

"""Questão de Demarcação Lado do Aluno"""

def ViewGetDemarcateQuestionnaireList(request):
    form = GetQuestionnaireListForm()
    if request.method == 'POST':
        form = GetQuestionnaireListForm(request.POST or None)
        Get_Name = request.POST.get('Name_Of_Group')
        return redirect(reverse('DemarcateApp:AnswerDemarcateQuestionView', kwargs={'pk': str(Get_Name)} ))
    context = {'form': form}
    return render(request, 'DemarcateApp/StudentSelectQuestionnaire.html', context)

# View para Pergunta sobre Demarcação de Imagem
def ViewAnswerDemarcateQuestion(request, pk):
    List_of_Question = list(DemarcateQuestion.objects.filter(Related_Question__Group_Name_Of_Quesitons=pk))
    Get_Student_Information = CustomUserModel.objects.get(Id_User=request.user.Id_User)
    Get_Question_Information = None
    Get_Group_Information = QuestionGroupModel.objects.get(Id_QuestionGroup=pk)

    X_Range = False
    Y_Range = False
    Width_Range = False
    Height_Range = False
    is_wrong = None
    Score_Per_Question = 0.00

    # A plataforma fornece duas tentativas ao estudante para uma demarcação correta
    # Define DTries "Tentativas" como 2 "Tentativas" se não existir na sessão
    if 'DIndex' not in request.session or 'DTries' not in request.session:
        request.session['DIndex'] = 0
        request.session['DTries'] = 2

    # Initialize Total_Score_Per_Questionnaire if it doesn't exist in the session
    if 'Total_Score_Per_Questionnaire' not in request.session:
        request.session['Total_Score_Per_Questionnaire'] = 0.0

    Total_Score_Per_Questionnaire = request.session['Total_Score_Per_Questionnaire']

    get_index = int(request.session.get('DIndex'))
    Get_Question_Information = List_of_Question[get_index]

    get_tries = request.session.get('DTries')

    # Informações sobre o total de notas de uma questão específica
    Question_Total_Marks = Get_Question_Information.Related_Question.Question_Marks

    print(Question_Total_Marks)
    if request.method == 'POST':
        if get_index < len(List_of_Question):
    # Precisa mudar esta parte para uma função diferente
    # ---------------------------------------------------
            StartX_Of_Marked_Area = int(request.POST.get('startX'))
            StartY_Of_Marked_Area = int(request.POST.get('startY'))
            Width_Of_Marked_Area = int(request.POST.get('width'))
            Height_Of_Marked_Area =int(request.POST.get('height'))
            # Area = abs(int(Width_Of_Marked_Area) * int(Height_Of_Marked_Area))
            Threshold = 10  # Temp
            if get_index < len(List_of_Question):
                """Intervalo Positivo""" """range(start[inclusivo], stop[exclusivo], step)"""
                """                 start                               stop                                             step"""
                X_P_Range = range((List_of_Question[get_index].StartX), (List_of_Question[get_index].StartX  + Threshold), 1)
                Y_P_Range = range((List_of_Question[get_index].StartY),
                                  (List_of_Question[get_index].StartY + Threshold), 1)
                Width_P_Range = range((List_of_Question[get_index].Width),
                                      (List_of_Question[get_index].Width + Threshold), 1)
                Height_P_Range = range((List_of_Question[get_index].Height),
                                       (List_of_Question[get_index].Height + Threshold), 1)
                # Area_P_Range = range((List_of_Question[get_index].Area),
                #                      (List_of_Question[get_index].Area + Threshold), 1)

                """Intervalo Negativo"""
                X_N_Range = range((List_of_Question[get_index].StartX - Threshold),
                                  (List_of_Question[get_index].StartX), 1)
                Y_N_Range = range((List_of_Question[get_index].StartY - Threshold),
                                  (List_of_Question[get_index].StartY), 1)
                Width_N_Range = range((List_of_Question[get_index].Width - Threshold),
                                      (List_of_Question[get_index].Width), 1)
                Height_N_Range = range((List_of_Question[get_index].Height - Threshold),
                                       (List_of_Question[get_index].Height), 1)
               # -------------------------------------------------------------------------------------------------------------------
                # Verifique as condições e atualize as variáveis
                # Verifica se o ponto x e y do estudante está entre os pontos x e y do professor + o limite de 10%
                # Início de X Positivo na área demarcarda e Início de X Negativo na área demarcarda
                if (StartX_Of_Marked_Area in list(X_P_Range)) or (StartX_Of_Marked_Area in list(X_N_Range)):
                    X_Range = True
                    print("X no Intervalo")
                # Início de Y Positivo na área demarcarda e Início de Y Negativo na área demarcarda
                if (StartY_Of_Marked_Area in list(Y_P_Range)) or (StartY_Of_Marked_Area in list(Y_N_Range)):
                    Y_Range = True
                    print("Y no Intervalo")
                    # Início da Largura Positiva na área demarcarda e Início da Largura Negativa na área demarcarda
                if (Width_Of_Marked_Area in list(Width_P_Range)) or (Width_Of_Marked_Area in list(Width_N_Range)):
                    Width_Range = True
                    print("Largura no Intervalo")
                    # Início da Altura Positiva na área demarcarda e Início da Altura Negativa na área demarcarda
                if (Height_Of_Marked_Area in list(Height_P_Range)) or (Height_Of_Marked_Area in list(Height_N_Range)):
                    Height_Range = True
                    print("Altura no Intervalo")
                # Verifique se todas as condições foram atendidas
                # Faixa de área removida
                if all([X_Range, Y_Range, Width_Range, Height_Range]):
                    is_wrong = False
                    print("Sua resposta está correta")
                    Score_Per_Question += float(Question_Total_Marks) if get_tries == 2 else float(Question_Total_Marks) / 2


                    Total_Score_Per_Questionnaire += Score_Per_Question
                    request.session['Total_Score_Per_Questionnaire'] = Total_Score_Per_Questionnaire
                    save_performance = StudentPerfomranceInDemarcateQuizes(
                        Student_Information=Get_Student_Information,
                        Question_Information=Get_Question_Information.Related_Question,
                        Question_Group_Information=Get_Group_Information,
                        Score_Per_Question=Score_Per_Question)
                    save_performance.save()
                    get_index += 1
                    request.session['DIndex'] = get_index
                    request.session['DTries'] = 2
                    if get_index >= len(List_of_Question):
                        return redirect('StudentsApp:CurrentDemarcateQuestionnaireResultView', pk)
                else:
                    print("Your Answer is wrong")
                    is_wrong = True
                    if get_tries is None:
                        get_tries = request.session.get('DTries')
                        get_tries = 2
                    get_tries -= 1
                    request.session['DTries'] = get_tries
                    if get_tries == 0:
                        Score_Per_Question = 0
                        save_performance = StudentPerfomranceInDemarcateQuizes(
                        Student_Information=Get_Student_Information,
                        Question_Information=Get_Question_Information.Related_Question,
                        Question_Group_Information=Get_Group_Information,
                        Score_Per_Question=Score_Per_Question)
                        save_performance.save()

                        get_index += 1
                        request.session['DIndex'] = get_index
                        request.session['DTries'] = 2



                        if get_index >= len(List_of_Question):
                            return redirect('StudentsApp:CurrentDemarcateQuestionnaireResultView', pk)
                            return redirect('DemarcateApp:ResultView')

        if get_index >= len(List_of_Question):
            request.session['DIndex'] = 0
            request.session['DTries'] = 2
            return redirect('StudentsApp:CurrentDemarcateQuestionnaireResultView', pk)
        else:
            question = List_of_Question[get_index]
            context = {'Demarcate_Question_List': question, 'is_wrong': is_wrong, 'Total_Score': Total_Score_Per_Questionnaire, 'Total_Questions': str(len(List_of_Question)), 'current_question':get_index}
            return render(request, 'DemarcateApp/StudentDemarcate.html', context)

    context = {'Demarcate_Question_List': List_of_Question[get_index], 'is_wrong': is_wrong, 'Total_Questions': str(len(List_of_Question)), 'current_question':get_index}
    return render(request, 'DemarcateApp/StudentDemarcate.html', context)


def ViewResult(request):
    if 'DIndex' in request.session or 'DTries' in request.session or 'Total_Score_Per_Questionnaire':
        del request.session['DIndex']
        del request.session['DTries']
        del request.session['Total_Score_Per_Questionnaire']
    return render(request,'DemarcateApp/Result.html')