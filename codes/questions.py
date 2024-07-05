import random
import re

folder_path = 'aimentor/'
vertices_path = folder_path + 'knowledge_vertices.py'
graph_path = folder_path + 'knowledge_graph.py'
output_path = folder_path + 'questions.txt'
template_path = folder_path + 'template.txt'


def process_template(template, actual_info):
    placeholder_pattern = r'\[(.*?)\]'
    
    def replace_match(match):
        placeholder = match.group(1).strip()
        if placeholder in actual_info:
            return actual_info[placeholder]
        else:
            return match.group(0) 
    
    processed_template = re.sub(placeholder_pattern, replace_match, template)
    
    store_pattern = r'\((.*?)\)'
    
    stored_parts = re.findall(store_pattern, template)

    print(processed_template, stored_parts)

    right_answer = actual_info[stored_parts[0]]
    wrong_answers = random.sample(knowledge_vertices[stored_parts[0]], 3)

    print(right_answer, wrong_answers)
    with open(output_path, 'a', encoding='utf-8') as file:
        file.write(f'{processed_template}\n')
        file.write(f'Right answer: {right_answer}\n')
        file.write(f'Wrong answers: {wrong_answers}\n')
        file.write('\n')

# Example knowledge graph
knowledge_vertices = {}

with open(vertices_path, 'r', encoding='utf-8') as file:
    exec(file.read())

# Example knowledge graph with tuple keys
knowledge_graph = {}
with open(graph_path, 'r', encoding='utf-8') as file:
    exec(file.read())

with open(template_path, 'r', encoding='utf-8') as file:
    for line in file:
        edge, question = line.split(':')
        edge = edge.strip()[1:-1]
        info = edge.split(',')
        print(info)
        info = [x.strip() for x in info]
        info = [
            x.strip()[1:-1] if (x.startswith("'") and x.endswith("'")) or (x.startswith('"') and x.endswith('"')) 
            else x.strip()[1:] if x.startswith("'") or x.startswith('"') 
            else x.strip()[:-1] if x.endswith("'") or x.endswith('"') 
            else x.strip() 
            for x in info
        ]
        print(info)
        # Convert info list to a tuple for dictionary key
        info_tuple = tuple(info)

        # Randomly select a key from the graph
        selected_key = random.choice(list(knowledge_graph[info_tuple].keys()))

        # Collect actual info
        actual_info = {}
        actual_info[info[0]] = selected_key
        for i, value in enumerate(knowledge_graph[info_tuple][selected_key]):
            actual_info[info[i + 1]] = value
        
        print('acutal_info: ', actual_info)
        print('question: ', question)
        process_template(question, actual_info)

