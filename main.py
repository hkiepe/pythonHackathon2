import phoneBook


if __name__ == '__main__':

    selected_menu = 'empty'
    while selected_menu != '4':
          selected_menu = phoneBook.print_menu()
          if selected_menu == '1':
              phoneBook.print_adresslist()
          elif selected_menu == '2':
              phoneBook.input_new_adress()
          elif selected_menu == '3':
              phoneBook.drop_adressline()
          elif selected_menu == '4':
              print('Program quit!')
          else:
              print('no such menu entry: ' + selected_menu)
