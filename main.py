string = ['abc.def', 'Abc,Def', 'ABc1DEf', 'ABCDEF']
# string.isupper() - ПЕРЕВІРЯЄ чи ВСІ літери у ВЕРХНЬОМУ реєстрі;
print('string.isupper()', string[0], '=', string[0].isupper())
print('string.isupper()', string[1], '=', string[1].isupper())
print('string.isupper()', string[2], '=', string[2].isupper())
print('string.isupper()', string[3], '=', string[3].isupper())
# string.islower() - ПЕРЕВІРЯЄ чи ВСІ літери у НИЖНЬОМУ реєстрі;
print('\nstring.islower()', string[0], '=', string[0].islower())
print('string.islower()', string[1], '=', string[1].islower())
print('string.islower()', string[2], '=', string[2].islower())
print('string.islower()', string[3], '=', string[3].islower())
# string.lower() - ПЕРЕТВОРЮЄ ВСІ літери у НИЖНІЙ реєстр;
print('\nstring.lower()', string[0], '=', string[0].lower())
print('string.lower()', string[1], '=', string[1].lower())
print('string.lower()', string[2], '=', string[2].lower())
print('string.lower()', string[3], '=', string[3].lower())
# string.upper() - ПЕРЕТВОРЮЄ ВСІ літери у ВЕРХНІЙ реєстр;
print('\nstring.upper()', string[0], '=', string[0].upper())
print('string.upper()', string[1], '=', string[1].upper())
print('string.upper()', string[2], '=', string[2].upper())
print('string.upper()', string[3], '=', string[3].upper())
# string.capitalize() - ПЕРЕТВОРЮЄ ПЕРШУ літеру у ВЕРХНІЙ реєстр;
print('\nstring.capitalize()', string[0], '=', string[0].capitalize())
print('string.capitalize()', string[1], '=', string[1].capitalize())
print('string.capitalize()', string[2], '=', string[2].capitalize())
print('string.capitalize()', string[3], '=', string[3].capitalize())
# string.split() - РОЗБИВАЄ РЯДОК на СЛОВА, за допомогою РОЗДІЛЬНИКА;
print('\nstring.split()', string[0], '=', string[0].split(','))
print('string.split()', string[1], '=', string[1].split(','))
print('string.split()', string[2], '=', string[2].split(','))
print('string.split()', string[3], '=', string[3].split(','), '\n')


lis = ['a', 'b', 'c', 1, 2, 3, 3.14, False, True]
print(lis[0:6:2])  # print(lis[початок(від 0):кінець(від 1):крок])
