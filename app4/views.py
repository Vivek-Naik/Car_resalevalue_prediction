# app4/views.py

from django.shortcuts import render
from app4.forms import WordForm

def permute(word):

    if len(word) <= 1:
        return {word}
    smaller_permutations = permute(word[1:])
    char = word[0]
    result = set()
    for perm in smaller_permutations:
        for i in range(len(perm) + 1):
            result.add(perm[:i] + char + perm[i:])
    return result

def home(request):
    form = WordForm(request.POST or None)
    permutations = None
    
    if form.is_valid():
        word = form.cleaned_data['word']
        permutations = sorted(permute(word))  # Sort to ensure a consistent order
    
    return render(request, 'app4/index.html', {'form': form, 'permutations': permutations})