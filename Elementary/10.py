import enum

class UserGrade(enum.Enum):
    a = 'A'
    bp = 'B+'
    b = 'B'
    cp = 'C+'
    c = 'C'
    dp = 'D+'
    d = 'D'
    f = 'F'

config = (
    (80, UserGrade.a),
    (75, UserGrade.bp),
    (70, UserGrade.b),
    (65, UserGrade.cp),
    (60, UserGrade.c),
    (55, UserGrade.dp),
    (50, UserGrade.d),
    (0, UserGrade.f),
)

scoreStr = input("Enter you score: ")
score = int(scoreStr)
print("You score is " + scoreStr)

if score not in range(101):
    print("Score must be in range [0, 100]")
else:
    for (s, g) in config:
        if score >= s:
            print("You got: '{}'".format(g.value))
            break;
