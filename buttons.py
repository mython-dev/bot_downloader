from telebot import types



social_network = types.InlineKeyboardMarkup(row_width=2)
instagram = types.InlineKeyboardButton (text= 'Instagram', callback_data='INS')
youtube = types.InlineKeyboardButton (text= 'YouTube', callback_data='YT')

social_network.add(youtube,instagram)
