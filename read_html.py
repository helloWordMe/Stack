import re
from stack import Stack
def count_html_tags(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    

    tags = re.findall(r'[<>/]', content)
    
    print(tags)

    tag_count = len(tags)
    return tags

def push_stack(tags : list):
    stack = Stack[str]()
    for i in tags :
        print(i)
        stack.push(i)


file_path = 'Stack\my_file.html' 
#print("Total number of HTML tags:", count_html_tags(file_path))

tags = count_html_tags(file_path)
push_stack(tags=tags)


































