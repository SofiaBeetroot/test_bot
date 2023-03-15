import Token
from config import bot
from aiogram import types

PRICE = types.LabeledPrice(label='Підписка на 1 місяць', amount=20000)  # це == 20000 / 100 = 200 грн


async def buy(message: types.Message):
    if Token.PAYMENTS_TOKEN.split(':')[1] == 'TEST':
        await bot.send_message(message.chat.id, "Тестовий платіж")

    await bot.send_invoice(message.chat.id,
                           title="Підписка на бота",
                           description="Активація функціонала бота на 1 місяць",
                           provider_token=Token.PAYMENTS_TOKEN,
                           currency='uah',
                           photo_url='https://blog-assets.lightspeedhq.com/img/2021/06/6f6649f3-payments-101.png',
                           photo_width=416,
                           photo_height=234,
                           photo_size=416,
                           is_flexible=False,
                           prices=[PRICE],
                           start_parameter="one-month-subscription",
                           payload="test-invoice-payload")


async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)


async def successful_payment(message: types.Message):
    print("SUCCESSFUL PAYMENT:")
    payment_info = message.successful_payment.to_python()
    for key, values in payment_info.items():
        print(f'{key} = {values}')

    await bot.send_message(message.chat.id,
                           f"Оплата на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} пройшла успішно")
