from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode
from core.core import dispatcher
from keyboard import KeyboardStates


@dispatcher.message_handler(commands=["start"])
async def start(m: Message, dialog_manager: DialogManager):
    await dialog_manager.start(KeyboardStates.receiver, mode=StartMode.RESET_STACK)
