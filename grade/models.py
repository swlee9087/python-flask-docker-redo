class Grade(object):

    def __int__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def addScores(self, score):
        self.scores.append(score)

    def avg(self):
        return sum(self.scores) / len(self.scores)

    # def main(self):
    #     grade = Grade(input('Input Student Name : '))
    #
    #     for i in ['Korean', 'English', 'Math']:
    #         grade.addScores(int(input(f'{i}: ')))
    #
    #     avg = grade.avg()
    #
    #     if avg >= 90:
    #         result = 'A'
    #     elif avg >= 80:
    #         result = 'B'
    #     elif avg >= 70:
    #         result = 'C'
    #     elif avg >= 60:
    #         result = 'D'
    #     elif avg <= 50:
    #         result = 'E'
    #     else:
    #         result = 'F'
    #     print(f'{result}')