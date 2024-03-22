def CesarSH(key, offset, message):

    alphabet = sorted(set(message))
    tab = [None] * len(alphabet)
    offset -= 1
    insert_start = offset
    for char in key:
        if char not in tab:
            tab[insert_start] = char
            insert_start += 1
    for element in alphabet:
        if insert_start < len(alphabet):
            if element not in tab:
                tab[insert_start] = element
                insert_start += 1
        else:
            insert_start = 0
            tab[insert_start] = element
            insert_start += 1

    coded = ''
    for char in message:
        coded += tab[alphabet.index(char)]

    print("MESSAGE:")
    print(message)
    print("CODED MESSAGE:")
    print(coded)
    print("Ghystogram 1:")
    ghystogram1 = getFrequency(message)
    for element in alphabet:
        percent = (ghystogram1.get(element, 0) / len(message))
        print(f"{element}: {percent * 100}%")
    print("Ghystogram 2:")
    ghystogram2 = getFrequency(coded)
    for element in alphabet:
        percent = (ghystogram2.get(element, 0) / len(coded))
        print(f"{element}: {percent * 100}%")
    print("Tab:")
    print(tab)
    return coded


def CesarDSH(key, offset, coded):
    alphabet = sorted(set(coded))
    tab = [None] * len(alphabet)
    offset -= 1
    insert_start = offset
    for char in key:
        if char not in tab:
            tab[insert_start] = char
            insert_start += 1
    for element in alphabet:
        if insert_start < len(alphabet):
            if element not in tab:
                tab[insert_start] = element
                insert_start += 1
        else:
            insert_start = 0
            tab[insert_start] = element
            insert_start += 1

    decoded = ''
    for char in coded:
        decoded += alphabet[tab.index(char)]

    print("DECODED MESSAGE:")
    print(decoded)
    return decoded


def getFrequency(string):
    freq = {}
    for char in string:
        freq[char] = freq.get(char, 0) + 1
    return freq
message = "ЖилбылнасветекоролЖилбылнасветекорольукоторогобылотрисынаСтаршийсынбылсильнымиумелымвоиномсреднийбылловкимиумелымкупцомамладшийбылнеобычайноумнымиспособныммолодымчеловекомОднаждыкорользаболелтяжелойболезньюинемогнайтилекарствоотсвоейболезниТогдаонобратилсяксвоимсыновьямзапомощьюСтаршийсынотправилсянапоискицелебныхтравикорнейсреднийотправилсянапоискилекарственныхрастенийифруктовамладшийотправилсянапоискимудрогомагакоторыймогбывылечитьегоотболезниМладшийсынпрошелдолгийитрудныйпутьновконцеконцовнашелмудрогомагакоторыйсказалемучтоонсможетвылечитькороляеслипринесетемутриволосазолотойголовыдраконаМладшийсынотправилсянапоискизолотойголовыдраконаОнпутешествовалмногоднейимногоночейпреодолеваятрудностиииспытанияновконцеконцовнашелдраконакоторыйсогласилсяотдатьемутриволосасвоейзолотойголовыМладшийсынвернулсякмудромумагуиотдалемуволосыМудрыймагсмогвылечитькороляикорольбылтакрадчтообещалмладшемусынудатьемувсечтоонзахочетМладшийсынпопросилукоролятолькооднувещькоролевствоКорольбылсильноудивленновидячтоегосынтакуверенвсебеисвоихспособностяхотдалемукоролевствоТакмладшийсынсталкоролемиправилсвоимкоролевствоммудроисправедливоИжилондолгоисчастливозаслуживаялюбовьиуважениесвоихподданных"

coded = CesarSH('безопасность', 0, message)
decoded = CesarDSH('безопасность', 0, coded)
