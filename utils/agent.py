from typing import Union
from gigachat import GigaChat
from utils.env import env

token = env.str("TOKEN")

model = GigaChat(
    credentials=token,
    scope="GIGACHAT_API_CORP",
    verify_ssl_certs=False,
    profanity_check=False,
)

async def async_request_to_gigachat(prompt: str) -> str:
    """Wrapper over the model class for easy use"""
    response = await model.achat(prompt)
    return response.choices[0].message.content

async def async_get_answer(query: str, context: str) -> tuple[Union[str, None], str]:
    """Function to get answer from model"""
    
    if "\n" in query:
        prompt = f"Ответь на вопрос опираясь на данную информацию: {context}. Вопрос: {query}. Ответ должен содержать только номер правильного ответа"
        answer = await async_request_to_gigachat(prompt)
        answer = "".join([symbol for symbol in answer if symbol.isdigit()])
        reasoning = "Из информации на сайте"
        
    else:
        prompt = f"Ответь на вопрос опираясь на данную информацию: {context}. Вопрос: {query}"
        answer = None
        reasoning = await async_request_to_gigachat(prompt)
        
    return answer, reasoning