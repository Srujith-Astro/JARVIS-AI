import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "you are a personal assistant"
    },
    {
      "role": "user",
      "content": "hey give me a short essay on AI"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)

'''
{
  "id": "chatcmpl-7knuHxyacfjjozCCmO8MHuI99bClz",
  "object": "chat.completion",
  "created": 1691389285,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Title: Artificial Intelligence: Revolutionizing the Future\n\nIntroduction:\n\nArtificial Intelligence (AI) refers to the intelligence displayed by machines, aiming to mimic human cognitive functions. With advancements in technology, AI has emerged as a powerful tool, revolutionizing various aspects of our lives. This essay will explore the significance of AI, its applications, benefits, and potential concerns.\n\nBody:\n\n1. Applications of AI:\n\nAI has found applications in numerous fields, enhancing efficiency and accuracy. In healthcare, AI systems analyze vast amounts of medical data to aid in diagnosis and treatment plans. Industries such as finance, manufacturing, transportation, and agriculture also benefit from AI by automating processes, reducing costs, and improving overall productivity. Additionally, AI powers virtual personal assistants like Siri and Alexa, transforming the way we interact with technology.\n\n2. Benefits of AI:\n\nAI offers countless benefits to individuals and society as a whole. It enables robots to perform repetitive and dangerous tasks, minimizing human involvement and risks. AI-powered algorithms can rapidly process vast amounts of data, leading to quicker insights and informed decision-making. Additionally, AI enhances personalization, enabling tailored experiences in areas such as e-commerce, entertainment, and marketing. Overall, AI has the potential to improve quality of life, drive economic growth, and address complex societal"
      },
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 24,
    "completion_tokens": 256,
    "total_tokens": 280
  }
}
'''