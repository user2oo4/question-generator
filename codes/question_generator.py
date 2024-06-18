import openai
import random

# OpenAI API details
OPENAI_API_KEY = 'sk-proj-WrQEyGR97nSKE9f1gCh4T3BlbkFJYq53eFWa0i8ewJ7HYKTP'  # Make sure to replace with your actual OpenAI API key
OPENAI_MODEL_ENDPOINT = 'gpt-3.5-turbo'  # Chat model

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
knowledge_vertices = {
    'Tính năng thẻ': ['Tích lũy điểm thưởng', 'Mua hàng trả góp', 
                      'Tặng đặc quyền miễn phí', 'Dịch vụ hỗ trợ khách hàng 24-7',
                      'Dịch vụ tin nhắn BSMS'],
    'Loại thẻ': ['Thẻ Mastercard Discovery', 'Thẻ JCB Credit Ultimate',
                 'Thẻ tín dụng cá nhân các hạng', 'Thẻ ghi nợ và tín dụng doanh nghiệp']
}

knowledge_graph = {
    ('Tính năng thẻ', 'Loại thẻ'): {
        'Tích lũy điểm thưởng': ['Thẻ Mastercard Discovery', 'Thẻ JCB Credit Ultimate'],
        'Mua hàng trả góp': ['Thẻ tín dụng cá nhân các hạng'],
        'Tặng đặc quyền miễn phí': ['Thẻ JCB Credit Ultimate'],
        'Dịch vụ hỗ trợ khách hàng 24-7': ['Thẻ ghi nợ và tín dụng doanh nghiệp'],
        'Dịch vụ tin nhắn BSMS': ['Thẻ ghi nợ và tín dụng doanh nghiệp']
    }
}

knowledge_graph_2 = {
    ('Tính năng thẻ', 'Loại thẻ'): {
        ('Tích lũy điểm thưởng', ['Thẻ Mastercard Discovery', 'Thẻ JCB Credit Ultimate']),
        ('Mua hàng trả góp', ['Thẻ tín dụng cá nhân các hạng']),
        ('Tặng đặc quyền miễn phí', ['Thẻ JCB Credit Ultimate']),
        ('Dịch vụ hỗ trợ khách hàng 24-7', ['Thẻ ghi nợ và tín dụng doanh nghiệp']),
        ('Dịch vụ tin nhắn BSMS', ['Thẻ ghi nợ và tín dụng doanh nghiệp'])
    }
}

# Randomly select an entity and its corresponding relationship
entity_type = random.choice(list(knowledge_graph.keys()))
entities = list(knowledge_graph[entity_type].keys())

entity = entities[0]
entity_key = knowledge_graph[entity_type][entity]
entity_name = entity_type[0]
entity_key_name = entity_type[1]
print('entities: ', entities)
print('entity: ', entity)
print('entityKey: ', entity_key)
print('entity name', entity_name)
print('entityKey name', entity_key_name)
choices = knowledge_vertices[entity_key_name]
# Generate the relationship prompt based on the selected entity
relationship_prompt = f"{entity} và mối quan hệ của nó với {entity_key}. Hãy sử dụng một câu ngắn và đơn giản để giải thích mối quan hệ. Bạn không cần cung cấp thêm thông tin. Gợi ý {entity} là {entity_name} và {entity_key} là {entity_key_name}."

# Call openai_chat_completion function with appropriate parameters
bruh = {
    'max_tokens': 500,
    'temperature': 0.6,
    'api_key': OPENAI_API_KEY,
    'model_endpoint': OPENAI_MODEL_ENDPOINT
}
template = openai_chat_completion(relationship_prompt)
template_text = template.decode('utf-8')
print("Generated template:", template_text)

question_prompt = f"Dựa trên câu này: {template_text}.Biết rằng hai thành phần chính của câu là {entity} và {entity_key}, bạn có thể viết một câu hỏi dựa trên câu này (ví dụ nếu câu là A có B. Câu hỏi có thể là A có cái gì? Bạn cần giấu thông tin về B). Và tạo các lựa chọn để biến nó thành câu hỏi trắc nghiệm. Nêu rõ những đáp án đúng. Chọn các đáp án sai từ {choices}"

question = openai_chat_completion(question_prompt)
print("Generated question:", question.decode('utf-8'))
