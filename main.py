import openai
import os


from config import OPNEAI_KEY



def get_image(text:str, count:int=1, size="1024x1024"):
    return openai.Image.create(prompt=text, n=count, size=size)









def get_open_ai(text:str, engine="text-davinci-003"):
    completion = openai.Completion.create(
            engine=engine,
            prompt=text,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
            )
    return completion.choices[0].text


if __name__ == '__main__':
    print(OPNEAI_KEY)
    openai.api_key = OPNEAI_KEY 
    com = openai.Completion.create(
            engine="text-davinci-003",
            prompt='Большие собаки',
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
            )
    print(com)
