from django.shortcuts import render
from staff.form import add_a_question
from staff.form_testcase import add_a_testcase 
from pages.models import question_list, testcase
from django.contrib.auth.decorators import permission_required

# Create your views here.
@permission_required ('pages.add_question_list', raise_exception=True)
def add_question(request):
   user = request.user
   form = add_a_question(request.POST)
   if request.method == 'POST':
      if form.is_valid():
         name = form.cleaned_data['question_name']
         statement = form.cleaned_data['question_statement']
         level = form.cleaned_data['difficulty']
         question_list.objects.create(
            question_name = name,
            question_statement = statement,
            difficulty = level
         )
         return render(request, 'add_question.html', {'user':user, 'form':form})
   
   
   return render(request, 'add_question.html', {'user':user, 'form':form})

@permission_required('pages.add_testcase', raise_exception=True)   
def add_testcase(request):
   user = request.user
   form = add_a_testcase(request.POST)
   if request.method == 'POST':
      if form.is_valid():
         question_id = form.cleaned_data['question_id']
         inputs = form.cleaned_data['tc_input']
         outputs = form.cleaned_data['tc_output']
         input_list = [input.strip() for input in inputs.split('|')]
         output_list = [output.strip() for output in outputs.split('|')]
         if len(input_list)!=len(output_list):
            print('ERROR')
         else:
            for i in range (0, len(input_list), 1):
               testcase.objects.create(
                  question_id = question_id,
                  tc_input = input_list[i],
                  tc_output = output_list[i],
               )
               
      
      
   return render(request, 'add_testcase.html', {'user':user, 'form':form})