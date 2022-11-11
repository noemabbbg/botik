
from operator import mod
from subprocess import call
from tracemalloc import start
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
 


uploader = InlineKeyboardMarkup(row_width=1)
upload_button = InlineKeyboardButton(text = "Загрузить", callback_data="uploader")
uploader.insert(upload_button)


main_menu = InlineKeyboardMarkup(row_width=2)
start_chapter = InlineKeyboardButton(text = "начать с начала", callback_data="start_read")
modify_chapter = InlineKeyboardButton(text = 'найти главу🔎', callback_data='start_modify_read')
back_to_titles_list = InlineKeyboardButton(text = 'к тайтлам', callback_data='back_to_titles_list')
main_menu.insert(start_chapter)
main_menu.insert(modify_chapter)
main_menu.insert(back_to_titles_list)

next_chapterKB = InlineKeyboardMarkup(row_width=2)
next_chapter = InlineKeyboardButton(text = '➡️', callback_data='next_chapter')
search_chapters = InlineKeyboardButton(text = 'найти главу🔎',callback_data='start_modify_read' )

next_chapterKB.insert(search_chapters) 
next_chapterKB.insert(next_chapter)
next_chapterKB.insert(back_to_titles_list) 



adm_panel = InlineKeyboardMarkup(row_width=1)
add_title = InlineKeyboardButton(text = 'Добавить новый тайтл', callback_data='addtitle')
add_chapters = InlineKeyboardButton(text = 'Добавить новые главы', callback_data='addchap')
adm_panel.insert(add_title)
adm_panel.insert(add_chapters)