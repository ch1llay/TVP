# user_input = input()


# отделение до первой   ;
    # [var]    <ident> : INTEGER(7)
    # <indent> _букваЦифра,  между литералами должна быть запятая, "а а,"
    # <ident> не более 11 символов
    # проверить кол-во символов между запятой и запятой (если запятая присутсвует)
    # не начинается и не заканчивается запятой)
    # после идентификатора должно идти :
    # после var минимум один пробел +


    # начинается BEGIN заканчивается END








# VAR aboba, aboba1:INTEGER;Begin
import string
import re

class _:
    literals = []
    def var_declaration(self, s:str) -> str:

        if ";" not in s:
            print("отсутствует точка с запятой")
            exit(0)
        if s[:3].lower() == "var":
            s = s[3:]
            try:
                literals, s = s.split(':')
                if "INTEGER;" not in s:
                    print("ошибка в объявлении переменной")
                    exit(0)
            except:
                print("ошибка в объявлении переменной")
                exit(0)

            if [",", 's1','s2'][0] in literals:
                literals = literals.split(",")

                literals = [l.strip(" ") for l in literals]
            else:
                literals = [literals.strip("")]
            print(literals)
            for l in literals:
                print(f"'{l}'") # показ переменных
                if len(l) > 11:print("Идентификаторы должны быть не длиннее 11 символов"); exit(0)
                if re.fullmatch(r"(_|([a-zA-Z]|\d))+", l) == None:
                    print("некорректное название переменной")
                if literals == set(literals):print("названия идентификаторов не должны повторяться"); exit(0)
            self.literals = literals
        else:
            print("отсутствует ключевое слово VAR")
            exit(0)
        self.main_part(''.join(s.split(";")[1:]))

    def check_correct_math(self, exp):
        try:
            result = eval(exp)
            return True
        except:
            return False
    def check_expression(self, expression:str):
        # a = a + a
        # b = 1;
        # c = 10;
        # a = (((b)c) + (b-c))/(c+b)-(c-b))/100 + 1
        expression.replace(' ', '')
        literal, expression = expression.split("=")[0]
        if literal not in self.literals:
            print("в присвоении должны использоваться только объявленные переменные")
            exit(0)
        if expression.count("(") != expression(")"):
            print("ошибка, проверьте правильность скобок")
            exit(0)

        operator_indexes = []
        for i in len(expression):
            if expression[i] in ['+', '-', '/']:
                operator_indexes.append(i)
        for i in operator_indexes:
            if expression[i] != '-':
                if i == 0:
                    print("ошибка выражения")
                    exit(0)
            if re.fullmatch(r"\d+|[a-zA-Z]+", expression[i-1]) == None:
                print("ошибка выражения")
                exit(0)
            if re.fullmatch(r"\d+|[a-zA-Z]+", expression[i+1]) == None:
                print("ошибка выражения")
                exit(0)
        expression = expression.replace("+", '')
        expression = expression.replace("-", '')
        expression = expression.replace("/", '')
        for c in expression:
            if re.fullmatch(r"/d", c) == None:
                if re.fullmatch(r"(_|([a-zA-Z]|\d))+", c) == None:
                    print("некорректное название переменной")








        
        
        # должны использоваться только объявленные переменные
        # начинаться с корректного идентификатора уже объявленной перменной
        # после знак =
        # после (), (унарный -) существующий корректный идентификатор, + - /
        # количество открывающихся скобочек должно быть равно количеству закрывающих скобочек
        # + строго между переменными | (переменной и скобкой)->(a+(a/b)->(a/b)+a) | (выражение1) + (выражение2) ...
        # - перед переменными | перед открывающей скобкой | (переменной и скобкой) | (выражение1) + (выражение2) ...
        # / строго между переменными | (переменной и скобкой)->(a/(a/b)->(a/b)/a) | (выражение1) / (выражение2) ...
        # + - / для цифр

    def main_part(self, s):
        pass



# shop_machine = _()
# shop_machine.var_declaration(input())

eval(input())

















