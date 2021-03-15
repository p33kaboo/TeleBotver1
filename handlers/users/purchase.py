import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.utils import callback_data

from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.choice_buttons import choice, pear_keyboard, apples_keyboard
from loader import dp, bot


@dp.message_handler(Command("items"))
async def show_items(message: Message):
    await message.answer(text="На продажу у нас есть 2 товаров: 5 Яблок и 1 Груша. \n"
                              "Если вам ничего не нужно - нажмите отмену",
                         reply_markup=choice)


@dp.callback_query_handler(buy_callback.filter(item_name="apple"))
async def buying_apples(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"call={callback_data}")
    quantity = callback_data.get("quantity")
    await call.message.answer(f"Вы выбрали купить яблоки. Яблок всего {quantity}. Спасибо.",
                              reply_markup=apples_keyboard)


@dp.callback_query_handler(text_contains="pear")
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=50)
    calback_data = call.data
    logging.info(f"call={callback_data}")

    await call.message.answer("Вы выбрали купить грушу. Груша всего одна. Спасибо.",
                              reply_markup=pear_keyboard)


@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
    await call.answer("Вы отменили покупку!", show_alert=True)
    await call.message.edit_reply_markup(reply_markup=None)