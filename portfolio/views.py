from django.shortcuts import render
import datetime


def home_page_view(request):
    agora = datetime.datetime.now()
    local = 'Lisboa'
    topicos = ['HTML', 'CSS', 'Python', 'Django', 'JavaScript']

    context = {
        'hora': agora.hour,
        'local': local,
        'topicos': topicos,
    }

    return render(request, 'portfolio/home.html', context)


def layout(request):
    return render(request, 'portfolio/templates/portfolio/layout.html')


#def quizz(request):
#   if request.method == 'POST'
#      n = request.POST['nome']
#      p = pontuacao_quizz(request)
#      r = PontuacaoQuizz(nome=n, pontuacao=p)
#      r.save()


