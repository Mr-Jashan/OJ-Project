from django.shortcuts import render , get_object_or_404
from pages.models import question_list
from compiler.form import codesubmissionform
from compiler.views import run_code
from pages.models import code_check, code_record, testcase
from account.models import profile
from django.contrib.auth.decorators import permission_required, login_required

def homepage(request):
   
   return render(request, 'homepage.html')

def list (request):
   questions = question_list.objects.all()
   return render(request, "question_list.html", {"questions" : questions}) 

@login_required
def leaderbord (request):
   leaderbord = profile.objects.all().order_by('-points')
   return render(request, 'lederbord.html', {'leaderbord':leaderbord})

@login_required
def submissions(request):
    user = request.user
    submissions = code_record.objects.filter(username=user)
    return render(request, 'submissions.html', {'submissions': submissions, 'buttom_check': True})

@login_required
def  q_solve(request, question_id):
   question = get_object_or_404(question_list, question_id=question_id)
   form = codesubmissionform(request.POST)
   user = request.user
   if(request.method =='POST'):
      
         if form.is_valid ():
            language = form.cleaned_data['language']
            code = form.cleaned_data['code']
            
            if 'action' in request.POST:
               if request.POST['action'] == 'run':
                  input = form.cleaned_data['input_data']
                  output = run_code(language, code, input)
                  return render(request, 'solve_question.html', {'output':output, 'form':form, 'question':question, 'run':True}) 

               elif request.POST['action'] == 'submit':
                  testcases = testcase.objects.filter(question_id = question_id)
                  tc_passed = True
                  output=""
                  err_input=""
                  exp_output=""
                  for input in testcases:
                     output = run_code(language, code, input.tc_input)
                     if output.strip() != input.tc_output.strip():
                        tc_passed = False
                        err_input = input.tc_input.strip()
                        exp_output=input.tc_output.strip()
                        break
                  wronge_code={
                     'output' : output,
                     'err_input':err_input,
                     'exp_output':exp_output
                  }
                  record = code_record.objects.create(
                     username = user,
                     language = language,
                     code = code
                  )
                  # print(record.created_at)
                  user_check = code_check.objects.filter(username = user, question_id=question).exists()
                  if tc_passed:
                     if not user_check :
                        user_profile = profile.objects.get(user=user)  
                        if question.difficulty == 'easy':
                           sum_added = 1
                        elif question.difficulty == 'mediam':   
                           sum_added = 2
                        else:
                           sum_added = 3
                        user_profile.points += sum_added
                        user_profile.save()
                        
                        code_check.objects.create(
                           username = user,
                           question_id = question, 
                           is_accepted = True
                        )
                        return render(request, 'solve_question.html', {'question': question, 'form':form, 'status':True})
                     else:
                        return render(request, 'solve_question.html', {'question': question, 'form':form, 'status':True})
                  else:
                     if not user_check:
                        user_profile = profile.objects.get(user=user)
                        user_profile.points -= 0.001
                        user_profile.save()
                     return render(request, 'solve_question.html', {'question': question, 'form':form, 'status':False, 'wronge_code':wronge_code})
               return render(request, 'solve_question.html', {'question': question, 'form': form})
              
         else:
            return render(request, 'solve_question.html', {'question': question, 'form': form, 'errors': form.errors})         
            
   else:   
      form = codesubmissionform()
      return render(request, 'solve_question.html', {'question': question, 'form':form})
   
