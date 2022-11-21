from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram_dialog import Window, Dialog, DialogRegistry
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const
from core.core import dispatcher


registry = DialogRegistry(dispatcher)


class KeyboardStates(StatesGroup):
    sender = State()    # teachers
    receiver = State()  # students


teacher_window = Window(
    Const("Hello, teacher"),
    Button(Const("Useless button"), id="teacher_btn"),
    state=KeyboardStates.sender,
)


student_window = Window(
    Const("Hello, student"),
    Button(Const("Useless button"), id="student_btn"),
    state=KeyboardStates.receiver,
)


dialog_student = Dialog(student_window)
registry.register(dialog_student)
