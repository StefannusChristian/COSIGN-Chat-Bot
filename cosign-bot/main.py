from telegram.ext import *
from random import choice
import keys

# Global Variables
greetings = [
    'hey',
    'hola',
    'hi',
    'halo',
    'hai'
    ]

kos_terdekat = [
    'kos terdekat',
    'saya ingin mencari kos terdekat',
    'apakah ada kos terdekat dekat CIT',
    'cari kos'
    ,'kos'
]

list_kos_terdekat = ['Kost Pak Mulyono', 'Kost Putri ', 'Kost Bu Yanti',
       'Kost Apik Kranti 6B Tipe A', 'Kost pak Ncang',
       'Kost Kelinci Bunder 5 Tipe A ', 'Kost 157 Tipe A',
       'Kost Putri Bu Aan', 'Tabhita Kos', 'Kost XXI ', 'Crystal Kost',
       'Rukita Green 21']

apartement_terdekat = [
    'apartemen terdekat',
    'saya ingin mencari apartemen terdekat',
    'apakah ada apartemen dekat CIT',
    'cari apartemen',
    'apartment terdekat',
    'saya ingin mencari apartment terdekat',
    'apakah ada apartment dekat CIT',
    'cari apartment',
    'apartment',
    'apartemen'
    ]

print('Starting up bot...')

# Lets us use the /start command
def start_command(update, context): update.message.reply_text('Hello there! I\'m a bot. What\'s up?')

# Lets us use the /help command
def help_command(update, context):
    reply_text_string = '''
    Hi there!\nSepertinya kamu butuh bantuan.
    \nBerikut merupakan text-text yang kalian dapat tanyakan ke chat-bot kami!\n
    '''
    reply_text_string += ', '.join(greetings)
    reply_text_string = reply_text_string[:-1]
    
    update.message.reply_text(reply_text_string)


def handle_response(text):
    # Greetings
    greetings_responds = ['Hey there!','Hi There','Halo','Shalom!','Ada yang bisa dibantu?','Wassup!']
    for greet in greetings:
        if greet.strip() in text: return choice(greetings_responds)

    # Cari Kos
    kos_response = 'Berikut merupakan kos terdekat dari CIT berdasarkan riset kami:\n'
    for i in range(len(list_kos_terdekat)):
        curr_str = f'{i+1}. {list_kos_terdekat[i]}\n'
        kos_response+=curr_str
    
    for kos in kos_terdekat:
        if kos.strip() in text: return kos_response
    
    
    # Cari Apartemen
    apartement_responds = ''
    for apartement in apartement_terdekat:
        if apartement.strip() in text: return apartement_responds
    
    # Unknown Text
    unknown_response_list = ['Maaf, saya tidak bisa mengerti!',"I Don't Understand!","???","What?","Kamu Nanya?"]
    unknown_response_suffix = ' Ketik /help untuk menampilkan command yang mungkin bisa membantu'
    unknown_response = choice(unknown_response_list) + unknown_response_suffix
    
    return unknown_response


def handle_message(update, context):
    # Get basic info of the incoming message
    message_type = update.message.chat.type
    text = str(update.message.text).lower()
    response = ''

    # Print a log for debugging
    # print(f'User ({update.message.chat.id}) says: "{text}" in: {message_type}')

    # React to group messages only if users mention the bot directly
    if message_type == 'group':
        # Replace with your bot username
        if '@co_sign_bot' in text:
            new_text = text.replace('@co_sign_bot', '').strip()
            response = handle_response(new_text)
    else:
        response = handle_response(text)

    # Reply normal if the message is in private
    update.message.reply_text(response)


# Log errors
def error(update, context):
    print(f'Update {update} caused error {context.error}')


# Run the program
if __name__ == '__main__':
    updater = Updater(keys.token, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))

    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(1.0)
    updater.idle()