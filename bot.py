import logging


from aiogram import Bot, Dispatcher, executor, types


from main import get_image
from config import BOT_TOKEN


# Configure logging
logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)







@dp.message_handler(commands=['image'])
async def send_and_image(message: types.Message):
    await message.reply("Ожидаем ответа...")
    request = message.text.split()[1:]
    image = get_image(request)


    await message.answer(image)


# def get_image(text:str, count:int=1, size="1024x1024"):
#     return openai.Image.create(prompt=text, n=count, size=size)





@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
