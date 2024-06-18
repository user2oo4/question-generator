from gradio_client import Client

client = Client("KingNish/OpenGPT-4o")
result = client.predict(
		user_prompt={"text":"","files":[]},
		model_selector="idefics2-8b-chatty",
		decoding_strategy="Top P Sampling",
		temperature=0.5,
		max_new_tokens=4096,
		repetition_penalty=1,
		top_p=0.9,
		web_search=True,
		api_name="/chat"
)
print(result)