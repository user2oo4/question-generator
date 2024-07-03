import openai
import random

# OpenAI API details
OPENAI_API_KEY = 'sk-proj-WrQEyGR97nSKE9f1gCh4T3BlbkFJYq53eFWa0i8ewJ7HYKTP'  # Make sure to replace with your actual OpenAI API key
OPENAI_MODEL_ENDPOINT = 'gpt-4o'  # Chat model
folder_path = 'banking/'
vertices_path = folder_path + 'knowledge_vertices.py'
graph_path = folder_path + 'knowledge_graph.py'
output_path = folder_path + '4o.txt'

def openai_chat_completion(prompt, **kwargs):
    max_tokens = kwargs.get('max_tokens', 500)
    temperature = kwargs.get('temperature', 0.6)
    api_key = kwargs.get('api_key', OPENAI_API_KEY)
    model_endpoint = kwargs.get('model_endpoint', OPENAI_MODEL_ENDPOINT)

    openai.api_key = api_key

    response = openai.ChatCompletion.create(
        model=model_endpoint,
        messages=[
            {"role": "system", "content": "Bạn là một trợ lý hữu ích. Hãy trả lời bằng tiếng Việt."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens,
        temperature=temperature
    )

    return response['choices'][0]['message']['content'].replace('\'', '\"').encode('utf-8')

# Example knowledge graph
knowledge_vertices = {}

with open(vertices_path, 'r', encoding='utf-8') as file:
    exec(file.read())
# Example knowledge graph with tuple keys
knowledge_graph = {}
with open(graph_path, 'r', encoding='utf-8') as file:
     exec(file.read())

with open(output_path, 'w', encoding='utf-8') as output_file:
    # Randomly select a number of feature tuples and their corresponding card types
    for selected_edge in list(knowledge_graph.keys()):
        print(selected_edge)
        output_file.write(f'Selected edge: {selected_edge}\n')
        # generate template
        question_prompt = (
            f'Giả sử có những loại thông tin như sau: {selected_edge}. Hãy tạo ra một vài mẫu câu hỏi làm câu hỏi trả lời ngắn hỏi về {selected_edge[0]}.'
            f'Ví dụ, nếu các loại thông tin là Tên thẻ, Tính năng nổi bật, Chi tiết tính năng và hỏi về tên thẻ, mẫu câu hỏi có thể là: '
            f'Tính năng [Tính năng nổi bật] là của thẻ (tên thẻ) nào sau đây?'
            f'Nếu hỏi về Chi tiết tính năng, mẫu câu hỏi có thể là:'
            f'Hãy nêu (Chi tiết tính năng) của [Tính năng nổi bật] của [Tên thẻ].'
            f'Thông tin trong ngoặc [] được cho cụ thể, thông tin trong ngoặc () là thông tin được hỏi.'
            f'Ví dụ với mẫu câu hỏi: thẻ [Tên thẻ] có (Tính năng nổi bật) nào?, câu hỏi cụ thể có thể là: Thẻ tín dụng A có tính năng nổi bật nào?'
            f'Mỗi câu hỏi cần có ít nhất hai loại thông tin được cung cấp, nhưng chỉ hỏi về một loại thông tin (sử dụng ngoặc ()). Thêm ngoặc [] và () như trên.'
            f'Chỉ sử dụng các loại thông tin được cung cấp và không cần thêm thông tin cụ thể nào. Với các mẫu câu hỏi khác nhau, hãy chọn những tổ hợp thông tin khác nhau.'
            f'Mỗi tổ hợp thông tin chỉ cần một mẫu câu hỏi. Có thể loại đi những câu hỏi không hợp lý.'
        )
        question_template = openai_chat_completion(question_prompt)
        output_file.write(f'Question template: {question_template.decode()}\n\n')

exit(0)
selected_key = random.choice(list(knowledge_graph[selected_edge].keys()))
while selected_key == 'nan' or len(selected_edge) > 3:
    selected_edge = random.choice(list(knowledge_graph.keys()))
    selected_key = random.choice(list(knowledge_graph[selected_edge].keys()))
choices = list(knowledge_vertices[selected_edge[0]])
print('selected_edge: ', selected_edge)
print('selected_key: ', selected_key)
selected_features = knowledge_graph[selected_edge][selected_key]

selected_string = selected_key
for feature in selected_features:
    if feature != 'nan':
        selected_string += ',' + str(feature)

selected_hint = f"Biết rằng {selected_key} là {selected_edge[0]}"
for i in range(len(selected_features)):
    if selected_features[i] == 'nan':
        continue
    selected_hint += f", {selected_features[i]} là {selected_edge[i + 1]}"

# Generate the relationship prompt
relationship_prompt = (
    f"{selected_string} và mối quan hệ của chúng với nhau. "
    f"Hãy sử dụng một câu ngắn và đơn giản để giải thích mối quan hệ. "
    f"Bạn không cần cung cấp thêm thông tin. "
    f"{selected_hint}. "
    f"Nhấn mạnh những thông tin này."
)

print(relationship_prompt)
print()

template_text = openai_chat_completion(relationship_prompt)
print('template: ', template_text.decode())
print()
question_prompt = (
    f"Dựa trên câu này: {template_text}."
    f"Bạn có thể viết một câu hỏi dựa trên câu này và giấu đi thông tin về {selected_key}. Tạo các lựa chọn để biến nó thành câu hỏi trắc nghiệm với đáp án đúng là {selected_key}. Chọn 3 đáp án sai từ {choices}"
)
question = openai_chat_completion(question_prompt)
print("Generated question:", question.decode('utf-8'))
