from django.shortcuts import render, HttpResponse

from .models import Category, Candidate
from .forms import Submit


def submit_form(request):
    if request.method == 'POST':
        form = Submit(request.POST)

        if form.is_valid():
            category = form.cleaned_data.get('category').lower()
            candidate = form.cleaned_data.get('candidate').lower()

            if Category.objects.filter(type=category).exists():
                existed_cat = Category.objects.get(type=category)
                new_entry_count = existed_cat.entry_count + 1
                existed_cat.entry_count = new_entry_count
                existed_cat.save()

                if Candidate.objects.filter(name=candidate).exists():
                    existed_can = Candidate.objects.get(name=candidate)
                    new_vote_count = existed_can.vote_count + 1
                    existed_can.vote_count = new_vote_count
                    existed_can.save()
                else:
                    data_2 = Candidate(name=candidate, vote_count=1, category=existed_cat)
                    data_2.save()
            else:
                data_1 = Category(type=category, entry_count=1)
                data_1.save()

                data_2 = Candidate(name=candidate, vote_count=1, category=Category.objects.get(type=category))
                data_2.save()

            return HttpResponse('We registered your form. Category for: {} and your candidate is: {}'
                                .format(category, candidate))
    else:
        form = Submit()

    return render(request, 'poll/formpage.html', {'form': form})
