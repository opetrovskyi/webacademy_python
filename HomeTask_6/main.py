#2. Написать программу реализующую хранилище информации о пользователях.
# Разбить логику по модулям: storage (функции get, add, get_storage),
# main (взаимодействие с пользователем) (как в видео)


import storage, time
def main():
    while True:
        innput = int(input('1.get url\n2.add new url\n3.List storage\n4.Exit\n\t<<'))
        if innput == 4:
            break
        if innput == 1:
            alias = input('Enter URL alias: ')
            print(storage.get_url(alias))
            print('\n\n')
        if innput == 2:
            url = input('Enter full URL: ')
            alias = input('Enter URL alias: ')
            k = storage.add_url(url, alias)
            if k[1] == "alias_exist":
                force_input = input('Alias already exist!!!!\nOverwrite? "y/n"  <<')
                if force_input.lower() == 'y':
                    print(storage.force_add_url(k[0], url, alias, k[2]))
                elif force_input.lower() == 'n':
                    print('\n\t\tskipping')
                    pass
            else:
                print(k)
            print('\n')
        if innput == 3:
            rret = storage.print_all()
            for k, v in rret.items():
               print((time.strftime("%d %b %Y %H:%M:%S", time.gmtime(k)), v))
            print('\n')
if __name__ == '__main__':
    main()

