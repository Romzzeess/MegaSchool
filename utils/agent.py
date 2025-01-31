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

async def async_get_answer(query: str, context: str) -> tuple[int, str]:
    """Function to get answer from model"""
    
    if "\n" in query:
        prompt = f"""Вопрос: В каком рейтинге (по состоянию на 2021 год) ИТМО впервые вошёл в топ-400 мировых университетов?
        \n1. ARWU (Shanghai Ranking)\n2. Times Higher Education (THE) World University Rankings
        \n3. QS World University Rankings\n4. U.S. News & World Report Best Global Universities
        Ответ должен содержать только номер правильного ответа. Ответ:
        2
        Ответь на вопрос опираясь на данную информацию: {context}. Вопрос: {query}. Ответ должен содержать только номер правильного ответа. Ответ:"""
        answer = await async_request_to_gigachat(prompt)
        answer = int("".join([symbol for symbol in answer if symbol.isdigit()]))
        reasoning = "Из информации на основании источников"
        
    else:
        prompt = f"Ответь на вопрос опираясь на данную информацию: {context}. Вопрос: {query}"
        answer = -1
        reasoning = await async_request_to_gigachat(prompt)
        
    return answer, reasoning