from read_data import read_dataa
from add_data import add_dataa


option = int(input('Insert 1 to show file or insert 2 to add content to file: '))
match option:
    case 1:
        read_dataa()
    case 2:
        add_dataa()
    case 3:
        pass
        edit_dataa()

# Способ редактирования и перезаписи данных о студенте