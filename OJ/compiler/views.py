from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from compiler.form import codesubmissionform
from django.conf import settings
import os
import tempfile
import subprocess
from django.contrib.auth.models import User

@login_required
def home_page(request):
    context = {
        'user': request.user,
        'users': User.objects.all()
    }
    return render(request, 'home.html', context)

def submit(request):
    
    if(request.method =='POST'):
        form = codesubmissionform(request.POST)
        if form.is_valid ():
            language = form.cleaned_data['language']
            code = form.cleaned_data['code']
            input = form.cleaned_data['input_data']
            
            output = run_code(language, code,input)
            context = {
                'language': language,
                'code' : code,
                'input' : input,
                'output':output,
            }
            return render(request, 'index.html', {'form':form, 'context':context})
     
    else:
        form = codesubmissionform() 
        return render(request, 'index.html',{"form" : form})
    
def run_code(language, code, input):
    
    cleaned_input_data = '\n'.join(line for line in input.splitlines() if line.strip())

    output_data = ""

    if language == 'py':
        process = subprocess.Popen(
            ["python", "-c", code],
            stdin=subprocess.PIPE, 
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,  
            text=True                
        )
        output, errors = process.communicate(input=cleaned_input_data)

        output_data = output + errors
        # output_data =  errors if errors else output
        # print(cleaned_input_data)
        # print(output_data)
        
    elif language=='cpp':
        with tempfile.NamedTemporaryFile(delete=False, suffix='.cpp') as code_file:
            code_file.write(code.encode())
            code_file_name = code_file.name
            
        executable_path = code_file_name.rsplit('.',1)[0]
        compile_code = subprocess.run(
            ["g++", code_file_name, "-o", executable_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE  
        )
        
        if compile_code.returncode == 0:
            process = subprocess.Popen(
                [executable_path],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            output, errors = process.communicate(input=cleaned_input_data)
            output_data = output + errors
            os.remove(f"{executable_path}.exe")
        else:
            output_data = compile_code.stderr.decode()
        
        os.remove(code_file_name)
        print(f"Input -> {cleaned_input_data}")
        print(f"Output -> {output_data}")
    
    return output_data 