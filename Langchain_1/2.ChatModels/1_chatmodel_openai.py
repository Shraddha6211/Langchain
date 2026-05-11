from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini', temperature = 1.5, max_completion_tokens=500)

result = model.invoke("Suggest me fun activity to do in office on Friday.")

print(result.content)