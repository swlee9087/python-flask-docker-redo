import pandas as pd
from icecream import ic


class Conversion(object):
    def __init__(self):
        print('자료구조 타입변환 예제')
        print('Q1. 1부터 9까지 요소를 갖는 튜플 생성')
        tpl = self.create_tuple()
        ic(type(tpl))
        ic(tpl)
        print('Q2. 튜플을 리스트로 전환')
        lst = self.tuple_to_list(tpl)
        ic(type(lst))
        ic(lst)
        print('Q3. 리스트의 int 값을 float 로 전환')
        lst = self.int_to_float(lst)
        ic(type(lst))
        ic(lst)
        print('Q4. float 리스트를 int 리스트 로 전환')
        lst = self.float_to_int(lst)
        ic(type(lst))
        ic(lst)
        print('Q5. int 리스트를 딕셔너리로 전환. 단 키값은 int 를 str 로 변환시켜서 활용함')
        dic = self.list_to_dictionary(lst)
        ic(type(dic))
        ic(dic)
        print('Q6. "hello"를 가진 튜플생성')
        tpl = self.hello_to_tuple('hello')
        ic(type(tpl))
        ic(tpl)
        print('Q7. 6번 튜플를 리스트로 전환')
        df = self.hello_to_list(tpl)
        ic(type(df))
        ic(df)
        print('Q8. 5번 딕셔너리를 dataframe 으로 전환, orient 속성값으로 인덱스 지정')
        df = self.dictionary_to_dataframe(dic)
        ic(type(df))
        ic(df)
        print('Q9. 1번 튜플의 제곱을 요소로 갖는 리스트 출력')
        lst = self.tuple_square(self.create_tuple())
        ic(type(lst))
        ic(lst)
        print('Q10. 구구단 한 줄 출력 2*1=2, 2*2=4, ..., 9*9=81')
        lst = self.gugudan(self.create_tuple())
        ic(type(lst))
        ic(lst)
        print('Q11. 1번 튜플에서 3의 배수만 문자열로 갖는 리스트 출력')
        lst = self.tuple_multi_three_str_list(self.create_tuple())
        ic(type(lst))
        ic(lst)
        #################here on down is new, do in own time
        print("Q12. 키는 a, b, c 이고 값은[1,2,3],[4,5,6],[7,8,9] 인 딕셔너리 출력")
        dt = self.abc_dict()
        ic(type(dt))
        ic(dt)
        print("Q13. 12번 딕셔너리에서 키값을 인덱스로 갖는 데이터프레임 출력")
        df = self.orient_index(dt)
        ic(type(df))
        ic(df)
        print('Q14. 12번 딕셔너리에서 키값을 컬럼으로 갖는 데이터프레임 출력')
        df = self.orient_column(dt)
        ic(type(df))
        ic(df)


    def create_tuple(self) -> ():  # 1: 1부터 9까지 요소를 갖는 튜플 생성
        # t = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
        # tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9)
        # return tpl
        return (1, 2, 3, 4, 5, 6, 7, 8, 9)

    def tuple_to_list(self, tpl) -> []:  # 2: 튜플을 리스트로
        # lst = list(tpl)
        # return lst

        # ls = []
        # for i in tpl:
        #     ls.append(i)
        # return ls
        # return [i for i in tpl]
        return list(tpl)

    def int_to_float(self, lst) -> []:  # 3: 리스트의 int 값을 float 로
        # float_lint = float(lst)
        # float_tl = float(Conversion.tuple_to_list())
        # return float_lint

        # ls = []
        # for i in lst:
        #     ls.append(float(i))
        # return ls
        # return [float(i) for i in lst]
        return list(map(float, lst))

    def float_to_int(self, lst) -> []:  # 4: float 리스트를 int 리스트 로
        # int_float = int(lst)
        # return int_float

        # ls = []
        # for i in lst:
        #     ls.append(int(i))
        # return ls
        # return [int(i) for i in lst]
        return list(map(int, lst))

    def list_to_dictionary(self, lst) -> {}:  # 5: int 리스트를 딕셔너리로 전환. 단 키값은 int 를 str 로 변환시켜서 활용함
        # t = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # print([str(d) for d in t])  # - list compre
        # print(list(map(str,t)))  # - map fn

        # strings = []  # - for loop
        # for i in lst:
        #     strings.append(str(i))
        # return strings
        return {str(i): i for i in lst}
        # return list(map(str, lst))  -> Q8 답 안 나옴.

    def hello_to_tuple(self, param: str) -> ():  # 6: "hello"를 가진 튜플생성
        # t = "hello"
        # return t
        # t = str("hello")
        # return t
        # return str("hello")
        # return tuple("hello")
        return tuple(param)

    def hello_to_list(self, tpl) -> []:  # 7: 6번 튜플를 리스트로 전환
        # t = list("hello")
        # t = list(Conversion.hello_to_tuple())
        return list(tpl)

    def dictionary_to_dataframe(self, dt) -> object:  # 8: 5번 딕셔너리를 dataframe 으로 전환
        return pd.DataFrame().from_dict(dt, orient='index')

    def tuple_square(self, tpl) -> []:  # 9: 1번 튜플의 제곱을 요소로 갖는 리스트
        # return (tpl ** 2)
        # return [i**2 for i in tpl]
        return list(map(lambda x: pow(x, 2), tpl))
        # return list(map(pow(tpl,2),tpl))  -> TypeError: unsupported operand type(s) for ** or pow(): 'tuple' and 'int'

    def gugudan(self, tpl) -> []:  # 10: 구구단 한 줄 출력 2*1=2, 2*2=4, ..., 9*9=81
        # return list(map(lambda x: (x+1)*x, range(9)))
        #       -> lst: [0, 2, 6, 12, 20, 30, 42, 56, 72]
        # t = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # return list(map(lambda x, t: x * t, tpl, t))
        # -> lst: [1, 4, 9, 16, 25, 36, 49, 64, 81]

        # return list(map(lambda x: (x//10)*(x%10), range(10,100)))

        # return list(
        #     map(lambda x: str(x // 10) + ' x ' + str(x % 10)
        #                   + ' = ' + str((x // 10) * (x % 10)), range(10, 100)))  -> too pretty

        # return [(lambda x, y: '{}x{}={}'.format(x,y, x*y))(x,y) for x in range(2, 10) for y in range(1,10)]
        # return list(map(lambda x : f'{x} x {i} = {x*i}' for i in range(1,10)], tpl))
        return list(map(lambda x: list(map(lambda i: f'{x} x{i}={x * i}', range(1, 10))), tpl))

    def tuple_multi_three_str_list(self, tpl) -> []:  # 11: 1번 튜플에서 3의 배수만 문자열로 갖는 리스트 출력
        return list(map(lambda x: str(x) if x % 3 == 0 else 0, tpl))

    # def abc_dict(self):
    #     return {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
    #
    # def orient_index(self, dt):
    #     return pd.DataFrame() \
    #         .from_dict(dt, orient='index')
    #
    # def orient_column(self, dt):
    #     return pd.DataFrame().from_dict(dt)


if __name__ == '__main__':
    Conversion()
