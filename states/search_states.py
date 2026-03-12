from telebot.handler_backends import State, StatesGroup

class SearchStates(StatesGroup):
    waiting_for_movie_name = State()
    waiting_for_rating = State()
    waiting_for_budget_min = State()
    waiting_for_budget_max = State()
    waiting_for_year = State()
