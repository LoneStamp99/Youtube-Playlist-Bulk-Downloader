import colorama
from colorama import Fore, Back, Style

def printBanner():
    print(Fore.RED + '''
    
                                    
     
                                        ╓≡╖µ╫╫╗,,,
                                   ,╖@╫╫╣▓▓███▓▓▓▓▓▓╖
                                 ╖╢▒╢╢╢╣╫▓▓▓▓▓▓▓▓▓▓▓╢╣▒┐
                              ,╖▒▒▒▒╫╫╢╣▓╫╣╣╣╢▒╢╢╢╣▒▒▒▒▒║╖
                            ╖╢╢▒▒▒╢╢╢▒▒╫╣╢▒▒░▒▒╢▒╢▒▒▒▒╣▒▒▒╫
                          ╖╫╢╣╢╢╢╫╣╣▒╬▒╢▒▒▒░░▒▒░░▒▒▒▒▒▒╣▒▒▒╫╖
                        ╓╫╫▓▓╫▓▓▓▓▓▓▓▓▓▓▓╣▒░▒▒▒░▒▒╢▒╢╣▒╢▒╢╢╢╫╗
                      ,╫▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒╢▒╫▒▒╢╫╫╫▓▓▓▓▓▓▓▓▓▓▄
                     ╓▓▓▓▓╣▓▓▓█▓▓█▓▓▓▓▓▓█▓╣▓╣▓╣╣▒╫▓▓▓▓▓▓▓▓▓▓▓▓▓╗
                    ╠▓▓▓▓▓▓████████▓▓▓███▓▓▓▓▓╣╣╫▓▓▓▓▓█▓▓█████▓▓
                   g▓▓▓▓▓▓████▓╣▒╢▒▒▒╢╢╣╣╣▒▒▒╜▒▒╢▓▓▓▓██▓████████▓
                  ╓▓▓▓▓▓▓█▓██╣╜▀██████▓▓▒▒▒░  ░╢╢▒╢╫╣▓▓▓▓▓███████▌
                 ]▓▓▓▓▓▓▓▓██▒   └╨▀╝╝╝╨░`      ░▒╬▀▓██████▓███████
                 ╫▓▓▓▓▓▓▓██▌░                  ░░``╙╨▀▓▓▓╜▒▓██████▌
                ]▓▓▓╣▓▓████▌░                  ▒░       `░╜▒███████
                ╫▓▓╫╫▓█████▌░░           ,╓╥╥▒▒▒░░      ░░▒▒█▓█████▓
               ╫▓▓╣╫▓█████▓▓▒░          ▒╢▀╢▒╫▓▓╣▒░  .░░░▒╢▓████████▌
              ╫▓▓╣▓▓███████▓▒░░          `╙░▒▒▒╢▒░░░░░░░▒╢▓█████████▓╣
             ╫▓╣╣▓▓█████████▒░░       ,╓@║╫╬╬╬▓╣╢▒░░░░▒▒╢╫██████████▓▒─
            ╫▓╫╣▓▓██████████▌▒░░░    "▀▀▀▒▒H▒▒▓╣▓▒░░░▒▒╢╫████████████▓░
     ──   ,╖ ║▓██████████████▌▒░░░    ░▒╖╓▒▒░▒▒▒▒░░░▒▒╢╫█████████████▓▌
     ╢▒░░╙▓▄▄▓██▀▄▄▓██████████▓╣▒░░   `▒▒╢╫╫╣╫╣▒░░░▒╢╢▓███████████████▓
      ╓▒▒▒▒▀██▄]██████████████╣╣╢╣▒░.    `╙╜▒▒░░░▒▒╢╢█████████████████▓H
      ▀▓▓▀████▒▐██████████████╣▒▒▒▒╢╢▒╥╖╖░░░░░▒▒╫╫▓▓███████▓██████████▓W
         ▓▓▓██▒█████████████▓▓╣▒▒▒▒▒▒╢╣▒╢╢▒▒▒╫╬▓▓▓▓████████▓██████████▓▌
        ▐▓▓██▓▓█████████████▌╨╣▒▒▒▒▒▒▒▒▒▒▒▒▒╢╢╣╢╢╫▓████████▓██████████▓░
         ▀█▓████████████████▌░╙▒▒▒▒▒▒▒▒▒▒▒▒▒╢▒▒▒╢╢▓▓▓██████▓██▓███████▓[
           █████████████████▌▒ `╫▒░░░▒░░░▒▒▒▒▒▒▒╢╫▓▌╙█████▓██████████▓█▓▄▄▄▄▓
            ▀████████████████░░  ╙╢▒░░░░░░░▒▒▒▒▒╢╫▓  ╙███▓▓█▓████████▓█████▀
              ▀██████████████▒░ ░  ╙╢▒▒░░░░░▒▒▒▒╣╢`   ▐█▓▓▓█▓███████▓▓███▀
                ▀████████████▌ ┌░    ║▒▒░░░╜▒▒▒▒▒`     ▓████▓██████████▀
                  '▀██████████ ░`     ║▒▒▒░░▒▒▒▒▒      ]████████████▀`
                     "▀███████H░      '▒▒▒░░░▒▒░╙      ┌█████████▀'
                         ╙▀███M         ╙░`▒]░H▒╜      ]╨████▀╙
                              `          ]░.] ▒        ```
    
---
Miss K'

                                  
    ''' + Style.RESET_ALL)

printBanner()
print('\033[31mnamn: Kendrah Lonets karta\033[0m')
print('\033[32mÅlder: 24 år av ålder\033[0m')
print('\033[35mBeskrivning: Detta projekt skapades för skojs skull.\033[0m')
print('Address: Stockholm Sweden')
print('\033[36mSociala media: \033[0m\033[96m\033[4mFacebook\033[0m\033[0m, \033[96m\033[4mPintrest\033[0m\033[0m')
print('Click here for \033[96m\033[4mFacebook\033[0m\033[0m: \033[94m\033[4m\033[1mhttps://www.facebook.com\033[0m\033[0m')