from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm

# Create your views here.
def index(request):

    lottos = GuessNumbers.objects.all()
    # {"Lottos" : Lottos} < context
    return render(request, 'lotto/default.html', {"lottos":lottos})

def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")

def post(request):

    if request.method == 'POST':

        form = PostForm(request.POST)

        if form.is_valid():
            lotto = form.save(commit = False)
            lotto.generate()

            return redirect('index')


        # user_name = request.POST['name']
        # user_text = request.POST['text']
        # row = GuessNumbers(name=user_name, text=user_test)
        # row.generate() # self.save()

        # print('\n\n\n===========================\n\n\n')
        # print(request.POST['csrfmiddlewaretoken'])
        # print(request.POST['name'])
        # print(request.POST['text'])
        # print('\n\n\n===========================\n\n\n')

    else:
        form = PostForm()
        return render(request, 'lotto/form.html', {'form':form})


def detail(rewquest, lottokey):
    lotto = GuessNumbers.objects.get(pk=lottokey)

    return render(rewquest, 'lotto/detail.html', {'lotto':lotto})

# # Create your views here.
# def index(request):
#
#     row = GuessNumbers(name=request.POST['name'], text=request.POST['text'])
#
#     row.lottos = ""
#     origin = list(range(1,46))
#
#     for _ in range(0, row.num_lotto):
#         random.shuffle(origin)
#         guess = origin[:6]
#         guess.sort()
#         row.lottos += str(guess) +'\n' # 로또 번호 str에 6개 번호 set 추가
#
#     row.update_date = timezone.now()
#     row.save() # commit
#
#     return HttpResponse('<h1>Hello, world!</h1>')
