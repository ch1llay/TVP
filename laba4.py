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


class O:
    literals =[]

    def var_declaration(self, s: str) -> str:
        if len(s.strip()) == 0:
            print("введена пустая строка")
            exit(0)
        for c in s:
            if c in "<>?.!@#$%^&*":
                print("ошибка синтаксиса")
                exit(0)
        if ";" not in s:
            print("отсутствует точка с запятой")
            exit(0)
        if s[:4].lower() == "var ":
            s = s[3:]
            try:
                literals, s = s.split(':')
                if "INTEGER;" not in s:
                    print("ошибка в объявлении переменной")
                    exit(0)
            except:
                print("ошибка в объявлении переменной")
                exit(0)

            if [",", 's1', 's2'][0] in literals:
                literals = literals.split(",")

                literals = [l.strip(" ") for l in literals]
            else:
                literals = [literals.strip("")]
            for l in literals:
                if len(l) > 11:
                    print("Идентификаторы должны быть не длиннее 11 символов")
                    exit(0)
                if re.fullmatch(r"(_|([a-zA-Z]|\d))+", l) == None:
                    print("некорректное название переменной")
                    exit(0)
                def sort(lst):
                    lst.sort()
                    return lst
                if sort(literals) != sort(list(set(literals))):
                    print("названия идентификаторов не должны повторяться")
                    exit(0)
            self.literals = literals
        else:
            print("ошибка объявления переменных")
            exit(0)
        self.main_part(';'.join(s.split(";")[1:]))

    def check_correct_math(self, exp):
        try:
            result = eval(exp)
            return True
        except:
            return False

    def check_expression(self, expression: str):
        try:
            literal, expression = expression.split("=")
            literal = literal.replace(" ", '')
            expression = expression.replace(" ", '')
        except Exception as e:
            print("ошибка выражения")
            exit(0)
        if literal not in self.literals:
            print("ошибка выражения")
            exit(0)
        if "(" in expression or ")" in expression:
            if expression.count("(") != expression.count(")"):
                print("ошибка, проверьте правильность скобок")
                exit(0)

        operator_indexes = []
        for i in range(len(expression)):
            if expression[i] in ['+', '-', '/']:
                operator_indexes.append(i)
        for i in operator_indexes:
            if expression[i] == '-':

                if re.fullmatch(r"\(|\)|\d+|[a-zA-Z]+", expression[i - 1]) == None:
                    print("ошибка выражения")
                    exit(0)
                if re.fullmatch(r"\(|\(|\d+|[a-zA-Z]+", expression[i + 1]) == None:
                    print("ошибка выражения")
                    exit(0)

            else:
                if i == 0:
                    print("ошибка выражения")
                    exit(0)
                if re.fullmatch(r"\)|\d+|[a-zA-Z]+", expression[i - 1]) == None:
                    print("ошибка выражения")
                    exit(0)
                if re.fullmatch(r"\(|\d+|[a-zA-Z]+", expression[i + 1]) == None:
                    print("ошибка выражения")
                    exit(0)
        i = 0
        words = []
        while i < len(expression):
            if re.fullmatch(r"\d|[a-zA-Z]", expression[i]) != None:
                j = i + 1
                while j < len(expression) and expression[j] not in "+-/()":
                    j += 1
                words.append(expression[i:j])
                i = j-1
            i += 1
        for w in words:
            if not w.isnumeric():
                if w not in self.literals:
                    print("проверьте корректность переменных в выражении")
                    exit(0)

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
        if "BEGIN" not in s:
            print("ошибка синтаксиса")
            exit(0)
        _, expressions = s.split("BEGIN")
        if expressions[-3:] != "END":
            print("ошибка синтаксиса")
            exit(0)
        expressions = expressions[:-3]
        for expr in expressions.split(";"):
            if expr not in ' ':
                self.check_expression(expr)
        print("программа корректна")


shop_machine = O()
shop_machine.var_declaration(input())
