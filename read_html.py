import re
from stack import Stack

file_path = 'my_file.html'

def count_html_tags(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    tags = re.findall(r'[<>/]', content)

    return tags

def push_stack(tags : list):
    tags = tags[::-1]
    stack = Stack[str]()
    for i in tags :
        stack.push(i)
    return stack    

def compile_html_file(stack: Stack):

    open_tag = Stack[str]() 
    while stack.empty() == False:
        ele_one = stack.pop()
        ele_two = ''
        ele_three = ''
        if ele_one == '>':
            raise Exception('*') 

        elif ele_one == '<':
            ele_two = stack.pop()
            
            if ele_two == '>':

                open_tag.push('<>')
            
            elif ele_two == '/':
                ele_three = stack.pop()
            
                if ele_three == '>':

                    tag = open_tag.pop()
                    if tag != '<>':
                        raise Exception('Missing open tag <>')
            
                else:
                    raise Exception('missing >')
           
            else:
                raise Exception('Wrong syntax...')        

        
        else:
            raise Exception('Wrang syntax ...')
        
    if open_tag.empty() == True:
        print('your code is right')
    else:
        raise Exception('Wrong syntax...')   


tags = count_html_tags(file_path)
stack = push_stack(tags=tags)

compile_html_file(stack)




































