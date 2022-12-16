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
]

list_kos_terdekat = ['Kost Pak Mulyono', 'Kost Putri ', 'Kost Bu Yanti',
       'Kost Apik Kranti 6B Tipe A', 'Kost pak Ncang',
       'Kost Kelinci Bunder 5 Tipe A ', 'Kost 157 Tipe A',
       'Kost Putri Bu Aan', 'Tabhita Kos', 'Kost XXI ', 'Crystal Kost',
       'Rukita Green 21']

fasilitas_kos_pak_mulyono = [
    'Listrik',
    'Kamar mandi dalam'
    ]

fasilitas_kos_putri = [
    'Listrik',
    'Kamar mandi dalam'
]
apartement_terdekat = [
    'apartemen terdekat',
    'saya ingin mencari apartemen terdekat',
    'apakah ada apartemen dekat CIT',
    'cari apartemen',
    'apartment terdekat',
    'saya ingin mencari apartment terdekat',
    'apakah ada apartment dekat CIT',
    'cari apartment',
    ]

fasilitas_kost_bu_yanti = [
    'Listrik',
    'Laundry',
    'Kamar mandi dalem kamar dibersihkan 1 minggu sekali '
    ]

fasilitas_kost_apik = [
    'Size kamar: 2 x 2,4 meter',
    'Kasur',
    'Lemari Baju',
    'Kipas Angin',
    'Bantal',
    'Ada Jendela',
    'Kloset jongkok',
    'Kamar Mandi Luar',
    'Wastafel']

add_kost_apik = [
    'Berjarak < 3km dari rumah makan', 
    'Dekat dari circle K', 
    'Dekat dari Masjid', 
    'Dekat dari BTN', 
    'Dekat dari STIE', 
    'Dekat dari RS Umum', 
    '< 1km dari halte statiun pasar senen', 
    'tidak ada AC'
    ]

fasilitas_Kost_pak_Ncang = [
    ' Listrik'
     'Air',
     'Air Panas',
     'Laundry',
     'Setrika',
     'Kamar mandi dalem',
     'Gas'
    ]

add_Kost_pak_Ncang = [
    'Laundry'
]

fasilitas_kost_kelinci = [
    "Wifi",
    "Penjaga Kos",
    "Ruang Tamu",
    "CCTV",
    "Parkir Mobil",
    "Parkir Motor",
    "Parkir Sepeda"
    ]

add_kost_kelinci = [
    "Berjarak < 3km dari rumah makan",
    "circle K",
    "Masjid AL Iman", 
    "BTN", 
    "STIE",
    "RS Umum PAD Gatot"
    ]

fasilitas_Kost_157_Tipe_A = [
 'AC',
 'Kasur',
 'Lemari Baju',
 'Cleaning Service',
 'Kloset Duduk',
 'Kamar Mandi Luar',
 'Wastafel',
 'Shower',
 'Air Panas'
 ]

add_Kost_157_Tipe_A = [
    "Berjarak < 3 km warteg bahari kemayoran", 
    "Dekat dari circle K", 
    "Dekat dari Masjid AL Iman", 
    "Dekat dari STIE Jakarta International College"
    ]


list_apart_terdekat = ['The Mansion Jasmine Tower', 'Springhill', 'Springhill Lain',
       'Grand Palace Kemayoran']

fasilitas_Kost_Putri_Bu_Aan = [
    "Listrik",
    "Laundry",
    "Kamar mandi luar",
    "Tidak ada AC"
]

fasilitas_kos_tabhita = ['Kasur', 'Lemari', 'AC', 'Kamar mandi dalam', 'Free Wifi', 'Dapur bersama', 'Parkir motor di dalam']

add_kos_tabhita = ['Harga belum termasuk listrik', 'Listrik 1300 W token']

fasilitas_kos_xxi = ['AC','Lemari Baju','Meja Makan','Kamar mandi dalam','Wifi','Dapur','Taman','Balcon','Gazebo','Parkir Motor']

fasilitas_kos_crystal = ['AC','Free Wifi','Kamar Mandi dalam','Dapur','Parkir Mobil dan Motor']

fasilitas_kos_rukita = ['AC', 'Kamar Mandi dalam', 'Meja', 'Kursi', 'Lemari Pakaian']

fasilitas_aprt_jasmine = ['Kitchen','Balkoni','Laundry','Kamar Mandi Dalam','AC','2 Bed Room']

fasilitas_aprt_springhill = ['3 Bed Room','Kamar Mandi Dalam','Balkoni']

fasilitas_aprt_springhill_lain = ['3 Bedroom','1 gudang','Kitchen','Balkoni','TV','Bathtub']

fasilitas_aprt_grand_palace = ['AC','Dapur','Kamar mandi luar maupun dalam','TV','Ruang tamu luas + sofa','Ada air hangat','Balkoni']

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
        if greet.strip() in text: 
            return choice(greetings_responds)

    # Cari Kos
    kos_response = 'Berikut merupakan kos terdekat dari CIT berdasarkan riset kami:\n'
    for i in range(len(list_kos_terdekat)):
        curr_str = f'{i+1}. {list_kos_terdekat[i]}\n'
        kos_response+=curr_str
    kos_response+='Klik nomor kos untuk mendapatkan detail mengenai kos tersebut. Contoh: kos-<nomor-kos>' 
    
    for kos in kos_terdekat:
        if kos.strip() in text: 
            return kos_response
    
    
    # Kos XXI --> kos-10
    kos_xxi = 'Kost XXI Details\n\n'
    harga = 'Harga: 1.6 juta / bulan\n\n'
    kos_xxi += harga
    kos_xxi += 'Fasilitas\n'
    for i in range(len(fasilitas_kos_xxi)):
        curr_str_xxi = f'{i+1}. {fasilitas_kos_xxi[i]}\n'
        kos_xxi+=curr_str_xxi
    kos_xxi+="\nJarak Dari CIT:\n"
    jarak_dari_cit = "3.4 km"
    kos_xxi+=jarak_dari_cit

    if text=='kos-10':
        return kos_xxi

    # Kos Crystal --> kos-11
    kos_crystal = 'Kost Crystal Details\n\n'
    harga = 'Harga: 2.3 juta / bulan\n\n'
    kos_crystal += harga
    kos_crystal += 'Fasilitas\n'
    for i in range(len(fasilitas_kos_crystal)):
        curr_str_crystal = f'{i+1}. {fasilitas_kos_crystal[i]}\n'
        kos_crystal+=curr_str_crystal
    kos_crystal+="\nJarak Dari CIT:\n"
    jarak_dari_cit = "1.3 km"
    kos_crystal+=jarak_dari_cit

    if text=='kos-11':
        return kos_crystal

    # Kos Rukita Green 21 --> kos-12
    kos_rukita = 'Kost Rukita Green 21 Details\n\n'
    harga = 'Harga: 1.8 juta / bulan\n\n'
    kos_rukita += harga
    kos_rukita += 'Fasilitas\n'
    for i in range(len(fasilitas_kos_rukita)):
        curr_str_rukita = f'{i+1}. {fasilitas_kos_rukita[i]}\n'
        kos_rukita+=curr_str_rukita
    kos_rukita+="\nJarak Dari CIT:\n"
    jarak_dari_cit = "3.5 km"
    kos_rukita+=jarak_dari_cit

    if text=='kos-12':
        return kos_rukita

    
    # Kos Pak Mulyono --> kos-1
    kos_pak_mulyono_response = 'Kost Pak Mulyono Details\n\n'
    harga = 'Harga: 2.4 juta / bulan\n\n'
    kos_pak_mulyono_response += harga
    kos_pak_mulyono_response += 'Fasilitas\n'
    for i in range(len(fasilitas_kos_pak_mulyono)):
        curr_str_pak_mulyono = f'{i+1}. {fasilitas_kos_pak_mulyono[i]}\n'
        kos_pak_mulyono_response+=curr_str_pak_mulyono
    kos_pak_mulyono_response+="\nJarak Dari CIT:\n"
    jarak_dari_cit = "5 - 10 menit jalan kaki"
    kos_pak_mulyono_response+=jarak_dari_cit

    if text=='kos-1': return kos_pak_mulyono_response

    # Kos Putri --> kos-2
    kos_putri = 'Kost Putri Details\n\n'
    harga = 'Harga: 1.2 juta / bulan\n\n'
    kos_putri += harga
    kos_putri += 'Fasilitas\n'
    for i in range(len(fasilitas_kos_putri)):
        curr_str_putri = f'{i+1}. {fasilitas_kos_putri[i]}\n'
        kos_putri+=curr_str_putri
    kos_putri+="\nJarak Dari CIT:\n"
    jarak_dari_cit = "5 - 10 menit jalan kaki"
    kos_putri+=jarak_dari_cit

    if text=='kos-2': return kos_putri

    # Kos Bu Yanti --> kos-3
    kost_bu_yanti = 'Kost Bu Yanti Details\n\n'
    harga = 'Harga: 2.5 juta / bulan\n\n'
    kost_bu_yanti += harga
    kost_bu_yanti += 'Fasilitas\n'
    for i in range(len(fasilitas_kost_bu_yanti)):
        curr_str_Bu_yanti = f'{i+1}. {fasilitas_kost_bu_yanti[i]}\n'
        kost_bu_yanti+=curr_str_Bu_yanti
    kost_bu_yanti+="\nJarak Dari CIT:\n"
    jarak_dari_cit = "5 - 10 menit jalan kaki"
    kost_bu_yanti+=jarak_dari_cit

    if text=='kos-3': return kost_bu_yanti

    # Kos Apik --> kos-4
    kost_apik = 'Kost Apik Details\n\n'
    harga = 'Harga: 765 ribu (termasuk listrik)  / bulan\n\n'
    kost_apik += harga
    kost_apik += 'Fasilitas\n'
    for i in range(len(fasilitas_kost_apik)):
        curr_str_kost_apik = f'{i+1}. {fasilitas_kost_apik[i]}\n'
        kost_apik+=curr_str_kost_apik
    kost_apik+="\nJarak Dari CIT:\n"
    jarak_dari_cit = "+= 1.8 km\n"
    kost_apik+=jarak_dari_cit
    kost_apik+="\nInformasi Tambahan:\n"
    for i in range(len(add_kost_apik)):
        curr_str_kost_apik = f'{i+1}. {add_kost_apik[i]}\n'
        kost_apik+=curr_str_kost_apik


    if text=='kos-4': return kost_apik
    
    #Kost_pak_Ncang --> kos-5
    Kost_pak_Ncang = 'Kost Pak Ncang Details\n\n'
    harga = 'Harga: 2.1 juta / bulan\n\n'
    Kost_pak_Ncang += harga
    Kost_pak_Ncang += 'Fasilitas\n'
    for i in range(len(fasilitas_Kost_pak_Ncang)):
        curr_str_Kost_pak_Ncang = f'{i+1}. {fasilitas_Kost_pak_Ncang[i]}\n'
        Kost_pak_Ncang+=curr_str_Kost_pak_Ncang
    Kost_pak_Ncang+="\nJarak Dari CIT:\n"
    jarak_dari_cit = "+= 1.8 km\n"
    Kost_pak_Ncang+=jarak_dari_cit
    Kost_pak_Ncang+="\nInformasi Tambahan:\n"
    for i in range(len(add_Kost_pak_Ncang)):
        curr_str_Kost_pak_Ncang = f'{i+1}. {add_Kost_pak_Ncang[i]}\n'
        Kost_pak_Ncang+=curr_str_Kost_pak_Ncang


    if text=='kos-5': return Kost_pak_Ncang

    #Kost Kelinci --> kos-6
    kost_kelinci = 'Kost Kelinci Bunder 5 Tipe A\n\n'
    harga = 'Harga: 1.7 juta / bulan\n\n'
    kost_kelinci += harga
    kost_kelinci += 'Fasilitas\n'
    for i in range(len(fasilitas_kost_kelinci)):
        curr_str_kost_kelinci = f'{i+1}. {fasilitas_kost_kelinci[i]}\n'
        kost_kelinci+=curr_str_kost_kelinci
    kost_kelinci+="\nJarak Dari CIT:\n"
    jarak_dari_cit = "+= 2.7 km\n"
    kost_kelinci+=jarak_dari_cit
    kost_kelinci+="\nInformasi Tambahan:\n"
    for i in range(len(add_kost_kelinci)):
        curr_str_kost_kelinci = f'{i+1}. {add_kost_kelinci[i]}\n'
        kost_kelinci+=curr_str_kost_kelinci


    if text=='kos-6': return kost_kelinci

    #Kost Kelinci --> kos-7
    Kost_157_Tipe_A	 = 'Kost Kelinci Bunder 5 Tipe A\n\n'
    harga = 'Harga: 1.6 juta / bulan\n\n'
    Kost_157_Tipe_A	 += harga
    Kost_157_Tipe_A	 += 'Fasilitas\n'
    for i in range(len(fasilitas_Kost_157_Tipe_A)):
        curr_str_Kost_157_Tipe_A	 = f'{i+1}. {fasilitas_Kost_157_Tipe_A[i]}\n'
        Kost_157_Tipe_A	+=curr_str_Kost_157_Tipe_A	
    Kost_157_Tipe_A	+="\nJarak Dari CIT:\n"
    jarak_dari_cit = "+= 5.3 km\n"
    Kost_157_Tipe_A	+=jarak_dari_cit
    Kost_157_Tipe_A	+="\nInformasi Tambahan:\n"
    for i in range(len(add_Kost_157_Tipe_A)):
        curr_str_Kost_157_Tipe_A	 = f'{i+1}. {add_Kost_157_Tipe_A[i]}\n'
        Kost_157_Tipe_A	+= curr_str_Kost_157_Tipe_A	


    if text=='kos-7': return Kost_157_Tipe_A	

    #Kost Kelinci --> kos-8
    Kost_Putri_Bu_Aan = 'Kost Putri Bu Aan\n\n'
    harga = 'Harga: 800 ribu / bulan\n\n'
    Kost_Putri_Bu_Aan += harga
    Kost_Putri_Bu_Aan += 'Fasilitas\n'
    for i in range(len(fasilitas_Kost_Putri_Bu_Aan)):
        curr_str_Kost_Putri_Bu_Aan	 = f'{i+1}. {fasilitas_Kost_Putri_Bu_Aan[i]}\n'
        Kost_Putri_Bu_Aan	+=curr_str_Kost_Putri_Bu_Aan	
    Kost_Putri_Bu_Aan	+="\nJarak Dari CIT:\n"
    jarak_dari_cit = "5 - 10 menit jalan kaki\n"
    Kost_Putri_Bu_Aan	+= jarak_dari_cit


    if text=='kos-8': return Kost_Putri_Bu_Aan	

        # Kos Tabhita --> kos-9
    kos_tabhita = 'Kost Tabhita Details\n\n'
    harga = 'Harga: 1.5 juta / bulan\n\n'
    kos_tabhita += harga
    kos_tabhita += 'Fasilitas\n'
    for i in range(len(fasilitas_kos_tabhita)):
        curr_str_tabhita = f'{i+1}. {fasilitas_kos_tabhita[i]}\n'
        kos_tabhita+=curr_str_tabhita
    kos_tabhita+="\nJarak Dari CIT:\n"
    jarak_dari_cit = "2.8 km"
    kos_tabhita+=jarak_dari_cit
    kos_tabhita += '\n\nInformasi Tambahan:\n'
    for i in range(len(add_kos_tabhita)):
        curr_str_tabhita = f'{i+1}. {add_kos_tabhita[i]}\n'
        kos_tabhita += curr_str_tabhita

    if text=='kos-9':
        return kos_tabhita

    
        
    # Cari Apartemen
    apartement_responds = 'Berikut merupakan apartemen terdekat dari CIT berdasarkan riset kami:\n'
    for i in range(len(list_apart_terdekat)):
        curr_str = f'{i+1}. {list_apart_terdekat[i]}\n'
        apartement_responds+=curr_str
    apartement_responds+='Klik nomor apartemen untuk mendapatkan detail mengenai apartemen tersebut. Contoh: aprt-<nomor-apartemen>' 
    for apartement in apartement_terdekat:
        if apartement.strip() in text: 
            return apartement_responds
    
    # Apart The Mansion Jasmine Tower --> aprt-1
    aprt_jasmine = 'Apartment The Mansion Jasmine Tower Details\n\n'
    harga = 'Harga: ± 1.42 juta / bulan\n\n'
    aprt_jasmine += harga
    aprt_jasmine += 'Fasilitas\n'
    for i in range(len(fasilitas_aprt_jasmine)):
        curr_str_jasmine = f'{i+1}. {fasilitas_aprt_jasmine[i]}\n'
        aprt_jasmine+=curr_str_jasmine
    aprt_jasmine+="\nJarak Dari CIT:\n"
    jarak_dari_cit = "± 3 km"
    aprt_jasmine+=jarak_dari_cit
    aprt_jasmine += '\n\nInformasi Tambahan:\n1. Harga belum termasuk air dan listrik'

    if text=="aprt-1":
        return aprt_jasmine

    # Apart Springhill --> aprt-2
    aprt_springhill = 'Apartment Springhill Details\n\n'
    harga = 'Harga: 2.05 juta / bulan\n\n'
    aprt_springhill += harga
    aprt_springhill += 'Fasilitas\n'
    for i in range(len(fasilitas_aprt_springhill)):
        curr_str_springhill = f'{i+1}. {fasilitas_aprt_springhill[i]}\n'
        aprt_springhill+=curr_str_springhill
    aprt_springhill+="\nJarak Dari CIT:\n"
    jarak_dari_cit = "± 2.9 km"
    aprt_springhill+=jarak_dari_cit
    aprt_springhill += '\n\nInformasi Tambahan:\n1. Bisa muat maksimal 6 orang'

    if text=="aprt-2":
        return aprt_springhill

    # Apart Springhill Lain --> aprt-3
    aprt_springhill_lain = 'Apartment Springhill Lain Details\n\n'
    harga = 'Harga: 2.13 juta / bulan\n\n'
    aprt_springhill_lain += harga
    aprt_springhill_lain += 'Fasilitas\n'
    for i in range(len(fasilitas_aprt_springhill_lain)):
        curr_str_springhill_lain = f'{i+1}. {fasilitas_aprt_springhill_lain[i]}\n'
        aprt_springhill_lain+=curr_str_springhill_lain
    aprt_springhill_lain+="\nJarak Dari CIT:\n"
    jarak_dari_cit = "± 2.9 km"
    aprt_springhill_lain+=jarak_dari_cit

    if text=="aprt-3":
        return aprt_springhill_lain
    
    # Apart Grand Palace Kemayoran --> aprt-4
    aprt_grand_palace = 'Apartment Grand Palace Kemayoran Details\n\n'
    harga = 'Harga: 1.55 juta / bulan\n\n'
    aprt_grand_palace += harga
    aprt_grand_palace += 'Fasilitas\n'
    for i in range(len(fasilitas_aprt_grand_palace)):
        curr_str_springhill_lain = f'{i+1}. {fasilitas_aprt_grand_palace[i]}\n'
        aprt_grand_palace+=curr_str_springhill_lain
    aprt_grand_palace+="\nJarak Dari CIT:\n"
    jarak_dari_cit = "± 1.7 km"
    aprt_grand_palace+=jarak_dari_cit
    aprt_springhill += '\n\nInformasi Tambahan:\n1. 81 m²(3 bed room)'

    if text=="aprt-4":
        return aprt_grand_palace


    
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
    print(f'User ({update.message.chat.id}) says: "{text}" in: {message_type}')

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