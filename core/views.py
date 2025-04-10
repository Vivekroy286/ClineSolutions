from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm


@login_required
def home_view(request):
    questions = Question.objects.all().order_by('-created_at')
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('home')
    else:
        form = QuestionForm()
    return render(request, 'core/home.html', {'questions': questions, 'form': form })

@login_required
def question_detail_view(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    answers = question.answers.all()
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            return redirect('question_detail', question_id= question.id)
    else:
        form = AnswerForm()
    return render(request, 'core/question_detail.html', {'question' : question , 'answers' : answers, 'form': form})


@login_required
def like_answer_view(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    if request.user in answer.likes.all():
        answer.likes.remove(request.user)
    else:
        answer.likes.add(request.user)
    return redirect('question_detail', question_id=answer.question.id)
    
    
