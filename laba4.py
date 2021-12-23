# user_input = input()


# отделение до первой   ;
    # [var]    <ident> : INTEGER(7)
    # <indent> _букваЦифра,  между литералами должна быть запятая, "а а,"
    # <ident> не более 11 символов
    # проверить кол-во символов между запятой и запятой (если запятая присутсвует)
    # не начинается и не заканчивается запятой)
    # после идентификатора должно идти :
    # после var минимум один пробел +
    # переменные записываем в словарь


# при присвоении должны использоваться только объвленные переменные

# VAR aboba, aboba1:INTEGER;
import string
import re

class _:
    literals = []
    def var_declaration(self, s:str) -> str:

        if ";" not in s:
            print("отсутствует точка с запятой")
            return
        if s[:3].lower() == "var":
            s = s[3:]
            try:
                literals, s = s.split(':')
                if "INTEGER;" not in s:
                    print("ошибка в объявлении переменной 1")
                    return
            except:
                print("ошибка в объявлении переменной 2")
                return

            if [",", 's1','s2'][0] in literals:
                literals = literals.split(",")

                literals = [l.strip(" ") for l in literals]
            else:
                literals = [literals.strip("")]
            print(literals)
            for l in literals:
                print(f"'{l}'") # показ переменных
                if len(l) > 11:print("Идентификаторы должны быть не длиннее 11 символов"); return
                if re.fullmatch(r"(_|([a-zA-Z]|\d))+", l) == None:
                    print("некорректное название переменной")
                if literals == set(literals):print("названия идентификаторов не должны повторяться"); return
            self.literals = literals

        else:
            print("отсутствует ключевое слово VAR")
            return


shop_machine = _()
shop_machine.var_declaration(input())

















