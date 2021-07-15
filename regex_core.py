#!/usr/bin/env python
# coding: utf-8

import re
from typing import Any, List

class RegexCore:
    def __init__(self):
        self.global_counter = 0

    def __insight_decoder(self,txt: str, grit: int) -> str:
        """
        This is method is a Insight Query decoder
        :param txt:
        :param grit:
        :return:
        """

        # Removes any Near: before or After from the
        # TODO: this Logic will need to built later.
        print(txt)
        text1 = re.sub(r'(?<!(NEAR|FORE|FTER)):\d+\.?\d*s?', r'', txt)
        # Replace quotes if they are present in the beginning and end
        text1 = re.sub(r'^"(.*)"$', r'\g<1>', text1)
        # replace multiple spaces with single spac
        text1 = re.sub(r'[ ]+', r' ', text1)
        # Replace OR with Pipe
        text2 = re.sub(r'\s+OR\s+', '|', text1)
        # Remove space beside the pipe
        text3 = re.sub(r'\s*\|\s*', '|', text2)
        # Remove {60%-100%} like tags from the text
        text3 = re.sub(r'\{.*?\}', '', text3)

        # Find the innermost square bracket pair and then process it to a regular expression group which implements
        # the any order Logic. 'FirstInnermostSquareMatch' is a match object; As long as we find leftmost innermost
        # square brackets will will keep replacing them with the regular expression equivalent. Until we dont find
        # any more square brackets. Updated this code on 2020-04-02 00:01:58 to fix a bug where the square brackets
        # were being replaced at the first occurrence only.
        first_innermost_square_match = re.search(r'(?<=\[)[^/[]*?(?=])', text3)

        while first_innermost_square_match:
            its = self.__square_bracket(mystring=first_innermost_square_match,
                                grit=grit)
            text3 = re.sub(r'\[([^\]]*?)]', its, text3, 1)
            first_innermost_square_match = re.search(r'(?<=\[)[^/[]*?(?=])',
                                                    text3)

        # Replace all space with upto "Grit" number of characters
        text4 = re.sub(r'\s', '.{,' + str(grit) + '}', text3)
        # Remove all 'double quotes' surrounding parentheses
        text5 = re.sub(r'"(.*?)"', r'(\g<1>)', text4)
        # Replace every open parentheses '(' with '(?:' so that it becomes a non capturing group
        text6 = re.sub(r'\((?!\))', r'(?:', text5)
        # Enclose every word alternation in a non capturing group
        text7 = re.sub(r"([a-zA-Z|`'*%]+\|[a-zA-Z|`'*%]+)",
                    r"(?:\g<1>)", text6)
        # case 8 repalce % with a placeholder so that it can be corrected back to \w* in text11
        text8 = re.sub(r"%", r"Placeholder", text7)
        # Replace * with a placeholder so that it can be corrected back to \w* in text11
        text9 = re.sub(r"\*", r"Placeholdes", text8)
        # Put the regex for word boundary '\b' befor and after very word, so that regular expression correctly
        # identifies words
        text10 = re.sub(r"([a-zA-Z`']+)", r"\\b\g<1>\\b", text9)
        # Replace % and * with any alphanumeric string '\w*'
        text11 = re.sub(r"Placeholder", r"\\w*", text10)
        text12 = re.sub(r"Placeholdes", r"\\w+", text11)
        return text12


    def compose(self,text: str, limit: int) -> str:
        """
        convert Insight Query to Regex equivalent
        :param self:
        :param text:
        :param limit:
        :return:
        """
        self.global_counter=0
        return self.__insight_decoder(txt=text, grit=limit)


    def __square_bracket(self,mystring: Any, grit: int):
        """

        This function is Magic, it converts a group of words that are enclosed in square brackets(which means they can
        appear in any order according to callminer Logic) to a regular expression using undocumented ReGex engine
        behaviour to define the logic of words appearing in any order.

        :param mystring:
        :param grit:
        :return:
        """
        thingy = re.split(r'\s', mystring.group().strip())
        thingy = list(
            map(lambda x: r'(' + x + r'.{,' + str(grit) + '}?' + r')', thingy))
        thingy1 = self.__group_maker(
            term=r'|'.join(list(
                x + '()' * (len(thingy) - 1) for x in thingy))) + '{' + str(
            len(thingy)) + '}\\\\' + r'\\'.join(
            list(str(x) for x in range(1+self.global_counter, len(thingy) + 1 + self.global_counter)))
        self.global_counter+=(len(thingy)*(len(thingy)-1))
        # print(thingy)
        return thingy1


    def __group_maker(self,term: str) -> str:
        """
        This function takes a string and encloses it in parantheses, which is
        a group in regular expressions, hence the name groupmaker.
        :param term:
        :return:
        """
        return r'(' + term + r')'

regex_core= RegexCore()
# def __transform__(self, tr1):
#     re.split(r' ', tr1)
if __name__ == '__main__':
    #start('callminer_cats')
    print (regex_core.compose('''([tire% damag%] | [tire% bust%])''',limit=30))