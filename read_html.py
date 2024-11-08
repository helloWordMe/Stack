import re
from stack import Stack

file_path = 'my_file.html'

def count_html_tags(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    tags = re.findall(r'[<>/]', content)

    tag_count = len(tags)
    return tags

def push_stack(tags : list):
    tags = tags[::-1]
    stack = Stack[str]()
    for i in tags :
        stack.push(i)
    return stack    

def compile_html_file(stack: Stack):
    num_open = 0
    num_close = 0 
    open_tag = Stack[str]()
    close_tag = Stack[str]()  # پشته جدید برای نگهداری تگ‌های باز
    while True:
        ele_one = stack.pop()
        ele_two = ''
        ele_three = ''
        if ele_one == '>':
            raise Exception('*') 

        elif ele_one == '<':
            ele_two = stack.pop()
            
            if ele_two == '>':
                num_open += 1
                open_tag.push('<>')
            
            elif ele_two == '/':
                ele_three = stack.pop()
            
                if ele_three == '>':
                    num_close += 1
                    close_tag.push('</>')
            
                else:
                    raise Exception('missing >')
           
            else:
                raise Exception('Wrong syntax...')        

        
        else:
            raise Exception('Wrang syntax ...')
        
        if stack.empty()==True:
            break
    if num_close == num_open :
        print("your code is Right")
    else:
        raise Exception('Wrang syntax ...')




tags = count_html_tags(file_path)
stack = push_stack(tags=tags)

compile_html_file(stack)




































