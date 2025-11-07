from django import forms
from . import models
from django.shortcuts import render, redirect

# def student_form(request, forms.modelForm):
#     if request.method == 'POST':
#         form = forms.modelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('student_list')
#     else:
#         form = forms.modelForm()
#     return render(request, 'student_form.html', {'form': form})
