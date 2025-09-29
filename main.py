from pyscript import display, document
def form_message(e):
    name = document.getElementById('input1').value
    age = document.getElementById('input2').value
    school = document.getElementById('input3').value

    message = f'''Student Profile:\n
    Name:{name}\n 
        Age:{age}\n
            School:{school}\n
            
            information:\n
            {name}\'s is {age} years old who studies at {school}.
'''
    display(message, target="output")
    
