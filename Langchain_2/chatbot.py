from dotenv import load_dotenv
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-4.1-nano")

chat_history = [SystemMessage(content= 'Your are a helpful assistant'),]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content= user_input))
    if user_input == 'bye':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ", result.content)

print(chat_history)