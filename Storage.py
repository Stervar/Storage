## Модуль №1
## Основы программирования


# Привет! Я рад помочь тебе разобраться в основах программирования с самого начала, как если бы ты никогда не сталкивался с этим миром.
#  Постараюсь объяснить всё максимально подробно и понятно.
#  Давай представим, что мы с тобой находимся в классе, и ты впервые услышал слово «программирование». 
# Готов? Поехали!

# Что такое программирование?
# Программирование — это процесс создания программ, которые дают компьютеру команды на выполнение определённых действий. 
# Программа — это набор инструкций, который компьютер выполняет в точной последовательности. 
# Компьютер сам по себе ничего не понимает, он выполняет команды, которые ему задаёт человек — программист. Задача программиста — написать такие команды (или инструкции), чтобы компьютер мог выполнить их правильно и последовательно.

# Программист использует специальный язык программирования, который понятен компьютеру. 
# Это как общение с компьютером на его языке. 
# Существует множество языков программирования (например, Python, C++, Java и т. д.), и все они используются для различных целей. 
# Язык программирования можно сравнить с иностранным языком, только предназначенным для общения с машинами.

# Теперь, когда мы определились, что такое программирование, давай разберём, из чего оно состоит.

# Основные понятия в программировании
# Прежде чем приступить к программированию, нужно понять несколько ключевых понятий. 
# Эти понятия встречаются в любом языке программирования.








# 1. Переменные
# Переменные — это один из самых базовых элементов программирования. 
# Представь переменные как ящики, в которых можно хранить какие-то значения. 
# Например, числа, слова или даже более сложные вещи.

# Каждая переменная имеет имя (чтобы ты мог к ней обращаться) и значение (это то, что ты в ней хранишь). 
# Имя переменной должно быть уникальным, и оно помогает программе отличать одну переменную от другой.







# Пример:


# x = 5
# Здесь мы создали переменную с именем x, и она хранит в себе число 5. 
# Теперь, если нам нужно использовать это число где-то в коде, мы можем обращаться к x.








# 2. Типы данных
# Переменные могут хранить различные типы данных. 
# Вот несколько основных типов данных:

# Числа (целые числа и числа с плавающей точкой): Например, 5 или 3.14.
# Строки: Это текст, например, "Привет, мир!".
# Логические значения (True/False): Это значения, которые используются для проверки условий. Например, True означает «истина», а False — «ложь».
# Каждый тип данных служит для определённых целей. Например, если ты хочешь хранить возраст человека, ты будешь использовать число, а если его имя — строку.






# Пример:



# age = 25      # переменная хранит целое число
# name = "Alex" # переменная хранит строку (текст)
# is_student = True # переменная хранит логическое значение





# 3. Операции и операторы
# Операции и операторы — это действия, которые программа может выполнять с переменными. Основные операции включают:

# Арифметические операторы (сложение, вычитание, умножение, деление и т. д.):
# Пример: x + y (сложение переменных x и y)
# Операторы сравнения (больше, меньше, равно и т. д.):
# Пример: x == y (проверка, равны ли значения x и y)
# Логические операторы (и, или, не):
# Пример: x > 5 and y < 10 (проверка условия, что x больше 5 и y меньше 10)
# 4. Условные операторы
# Часто в программах нужно принимать решения, что делать дальше, в зависимости от какого-то условия. 
# Например, если возраст человека больше 18 лет, можно разрешить ему доступ к сайту, иначе — запретить. 
# Это реализуется с помощью условных операторов.







# Пример:


# if age >= 18:
#     print("Доступ разрешён")
# else:
#     print("Доступ запрещён")
# Здесь программа проверяет, больше ли значение переменной age или равно 18. Если это правда, она выводит сообщение "Доступ разрешён", иначе — "Доступ запрещён".









# 5. Циклы
# Циклы позволяют повторять одно и то же действие несколько раз.
#  Например, ты можешь попросить компьютер вывести на экран числа от 1 до 10.
#  Для этого не нужно писать десять строк кода — достаточно одного цикла.




# Пример:


# for i in range(1, 11):
#     print(i)
# Цикл for пробегает по значениям от 1 до 10 и выводит их по одному на экран.








# Пример 1. Вывод текста
# Теперь давай рассмотрим простой пример программы, которая выводит текст на экран.



# Пример:


# print("Привет, мир!")


# Разберём этот код:
# print() — это встроенная функция, которая выводит текст на экран. Всё, что ты напишешь в круглых скобках, будет выведено на экран.
# "Привет, мир!" — это строка (текст), которую мы хотим вывести.
# Когда программа выполнит этот код, ты увидишь на экране фразу «Привет, мир!».



# Объяснение:
# Мы вызвали функцию print, которая принимает аргумент — строку (текст), заключённую в кавычки.
#  Эта строка передаётся функции, и она выводит её на экран.






# Пример 2. Работа с переменными и условием
# Теперь рассмотрим пример программы, которая спрашивает у пользователя возраст и выводит, является ли пользователь совершеннолетним.



# Пример:


# age = int(input("Введите ваш возраст: "))

# if age >= 18:
#     print("Вы совершеннолетний!")
# else:
#     print("Вы ещё не совершеннолетний.")


# Разберём этот код:
# input() — это функция, которая запрашивает ввод у пользователя. Всё, что введёт пользователь, будет считаться строкой.
# int() — это функция, которая преобразует строку в число, потому что возраст — это числовое значение.
# if age >= 18 — это условие, которое проверяет, достиг ли возраст пользователя 18 лет.
# print() — функция, которая выводит текст на экран в зависимости от выполнения условия.



# Объяснение:
# Сначала программа запрашивает возраст пользователя через input(). Пользователь вводит число.
# Функция int() преобразует введённую строку в число.
# Программа проверяет, больше ли это число 18 или равно 18 с помощью условия if.
# Если условие выполняется (возраст больше или равен 18), программа выводит "Вы совершеннолетний!". Если нет — "Вы ещё не совершеннолетний."



# Итог:

# Теперь ты познакомился с основными понятиями программирования: переменными, типами данных, операциями, условиями и циклами. 
# Это базовые кирпичики, на которых строится любой код. 
# Программирование — это как создание конструктора: ты используешь разные детали, чтобы собрать нужную программу.







# Два рассмотренных примера — это простейшие программы, но на их основе можно строить более сложные и интересные программы, которые смогут решать различные задачи.






## Модуль №2
## Как работает компьютерная программа?






# Представь, что мы начинаем с самого начала.
#  Ты никогда не сталкивался с программированием, и перед тобой стоит вопрос: как вообще работает компьютерная программа? 
# Давай разбираться шаг за шагом, начиная с самых базовых понятий и объясняя всё детально.

# Что такое компьютерная программа?
# Компьютерная программа — это набор инструкций, которые выполняет компьютер для того, чтобы достичь какой-то цели или решить конкретную задачу. Эти инструкции написаны на языке, понятном компьютеру, а их выполнение контролируется центральным процессором компьютера.

# Проще говоря, программа — это как рецепт, который говорит компьютеру, что нужно делать. Рецепт может быть очень простым (например, показать текст на экране) или сложным (управлять самолётом или анализировать данные с миллионов датчиков). Но в любом случае программа — это просто набор последовательных команд.

# Из чего состоит программа?
# Любая программа состоит из таких элементов, как:

# Команды или инструкции — это действия, которые компьютер должен выполнить.
# Данные — это информация, с которой работает программа. Это могут быть числа, текст, изображения или что угодно.
# Операции — это действия, которые программа выполняет над данными (например, сложение чисел, проверка условий, сравнение значений).
# Поток управления — это порядок, в котором выполняются инструкции программы. Компьютер выполняет инструкции одну за другой, как будто он читает рецепт по шагам.
# Как программа взаимодействует с компьютером?
# Теперь представь себе компьютер как огромную машину, которая состоит из нескольких важных частей. Чтобы понять, как работает программа, нужно знать о двух ключевых компонентах компьютера:

# Процессор (CPU) — это "мозг" компьютера. Процессор отвечает за выполнение всех инструкций программы. Он может обрабатывать данные, выполнять математические операции, управлять памятью и контролировать, какие команды исполнять в следующую очередь.
# Память (RAM) — это место, где хранится временная информация, с которой работает программа. Когда программа запускается, она загружает свои данные и инструкции в память, чтобы процессор мог получить к ним быстрый доступ.
# Когда программа запускается, происходит следующее:

# Программа загружается в оперативную память (RAM) с жёсткого диска или другого устройства хранения.
# Процессор считывает первую инструкцию программы.
# Процессор выполняет эту инструкцию, например, сложение двух чисел или вывод текста на экран.
# Процессор переходит к следующей инструкции и так далее.
# Как компьютер понимает программу?
# Компьютер не понимает человеческий язык. Вместо этого он работает с машинным кодом — набором команд, которые состоят из нулей и единиц (бинарный код). Эти команды напрямую управляют процессором.

# Однако программисту было бы сложно писать программы на таком низком уровне, поэтому используются языки программирования — это своего рода переводчики между человеком и машиной. Программисты пишут код на языке, который понятен человеку (например, Python, Java или C++), а специальная программа (компилятор или интерпретатор) переводит этот код в машинный язык, который понимает процессор.

# Есть два основных типа программ, которые обрабатывают код:

# Компиляторы — они берут весь код программы и сразу переводят его в машинный код, создавая исполняемый файл (например, в Windows это файл с расширением .exe). После компиляции программа может запускаться без компилятора.

# Интерпретаторы — они обрабатывают код построчно, сразу выполняя команды. Пример интерпретируемого языка — Python. Каждая команда программы выполняется немедленно, как только она интерпретируется.

# Основные этапы работы программы
# Давай разберём основные этапы работы программы:

# Написание кода: Программист пишет код на языке программирования. Этот код содержит инструкции, которые компьютер должен выполнить.

# Компиляция/интерпретация: Код переводится в машинный язык (или исполняется напрямую, как в случае интерпретации).

# Загрузка в память: Программа загружается в оперативную память. Это позволяет процессору получить доступ к инструкциям и данным программы.

# Выполнение: Процессор начинает выполнять инструкции программы одну за другой. Он может выполнять арифметические операции, проверять условия, работать с памятью и управлять различными устройствами (например, клавиатурой или экраном).

# Хранение данных: Программа может сохранять данные на диске (например, файлы) или работать с временными данными в оперативной памяти.

# Вывод результатов: Программа может выводить данные на экран, отправлять их в файл или по сети. Это конечный результат её работы.

# Пример: Простая программа вывода текста
# Теперь, когда у нас есть базовое понимание того, как работает программа, давай посмотрим на первый простой пример программы. Мы напишем программу, которая просто выведет текст на экран.

# Пример 1:

# python
# Копировать код
# print("Привет, мир!")
# Что здесь происходит?

# print — это функция. Функция — это как мини-программа внутри программы, которая выполняет определённое действие. В данном случае функция print отвечает за вывод текста на экран.

# "Привет, мир!" — это строка текста, которую мы хотим вывести. Строка всегда заключается в кавычки, чтобы программа понимала, что это текст.

# Когда ты запускаешь эту программу, она выполнит единственное действие: выведет на экран текст "Привет, мир!".

# Как программа принимает данные от пользователя?
# Теперь давай посмотрим на более интересный пример программы, где пользователь может ввести данные, а программа их обработает.

# Пример 2:

# python
# Копировать код
# name = input("Введите ваше имя: ")
# print("Привет, " + name + "!")
# Здесь уже немного сложнее, но давай разберём по частям.

# input() — это функция, которая позволяет пользователю ввести текст с клавиатуры. То, что введёт пользователь, сохраняется в переменную name.

# name — это переменная. Переменная — это как коробка, в которую можно положить какие-то данные. В данном случае в переменной name хранится имя пользователя, которое он ввёл.

# print("Привет, " + name + "!") — здесь снова используется функция print, но теперь она выводит не только заранее заданный текст, но и значение переменной name. Знак + соединяет (конкатенирует) строки, то есть создаёт единый текст из нескольких частей: "Привет, ", имя пользователя и "!".

# Когда программа запустится, она сначала попросит ввести имя. Пользователь введёт, например, "Алексей", и программа выведет "Привет, Алексей!".

# Объяснение работы программы:
# Программа начинает выполнение с вызова функции input(), которая выводит на экран сообщение "Введите ваше имя:". Пользователь вводит текст, и этот текст сохраняется в переменной name.

# Затем программа вызывает функцию print(). Она выводит строку "Привет, " и добавляет значение переменной name (то есть имя пользователя), а затем добавляет восклицательный знак.

# Важные аспекты работы программы
# Теперь давай обсудим несколько важных аспектов того, как работают программы:

# 1. Алгоритм — это последовательность шагов, которые программа выполняет для решения задачи. Каждый шаг должен быть точно определён и выполняться в строго определённом порядке.
# Пример: если ты хочешь приготовить пирог, сначала нужно смешать ингредиенты, затем поместить их в духовку и подождать определённое время. То же самое происходит в программах: нужно точно определить порядок действий.

# 2. Ошибки — иногда программы не работают так, как задумано. Это может произойти из-за ошибок в коде, неправильных данных или неожиданных ситуаций (например, пользователь ввёл текст вместо числа). Такие ошибки называются "багами", и их нужно исправлять. Программисты часто сталкиваются с багами и занимаются их поиском и исправлением (этот процесс называется "отладка").
# 3. Оптимизация — это процесс улучшения программы, чтобы она выполнялась быстрее или использовала меньше ресурсов (например, памяти или процессорного времени).
# Заключение
# Теперь ты имеешь общее представление о том, как работает компьютерная программа. Мы прошли путь от простого понимания, что программа — это набор инструкций для компьютера, до рассмотрения конкретных примеров кода. Программы состоят из данных и инструкций, которые процессор выполняет шаг за шагом. Программисты пишут эти инструкции на специальных языках программирования, которые затем переводятся в машинный код, понятный компьютеру.

# Мы также увидели два примера кода, где программа сначала просто выводит текст, а затем взаимодействует с пользователем.









## Модуль №3
## Из чего состоит язык программирования?








# Программирование может показаться сложным, но если разобрать его на основные части, всё становится намного проще. Представь себе, что язык программирования — это способ общаться с компьютером. Как и любой язык, он состоит из разных элементов, которые помогают строить общение. Давай разберёмся, из чего именно состоит язык программирования, а затем рассмотрим два примера кода, чтобы всё было понятно на практике.

# 1. Синтаксис
# Каждый язык, будь то русский, английский или любой другой, имеет правила — синтаксис. Это законы, по которым мы строим предложения. В языке программирования синтаксис — это правила, которые определяют, как именно нужно писать команды, чтобы компьютер их понял. Если ты не соблюдаешь эти правила, программа не будет работать или выдаст ошибку.

# Например, в языке Python каждая инструкция пишется на новой строке, и отступы (пробелы в начале строки) имеют значение. А в других языках, например, в C++ или Java, в конце каждой команды нужно ставить точку с запятой.

# Пример в Python:

# python
# Копировать код
# print("Привет!")
# Пример в C++:

# cpp
# Копировать код
# cout << "Привет!";
# 2. Переменные и типы данных
# Переменные — это "контейнеры", в которых программа хранит данные. Данные могут быть разными: числа, текст, логические значения (истина или ложь) и т.д. Например, если тебе нужно сохранить возраст человека или его имя, ты используешь переменные.

# Каждая переменная имеет тип данных. Это значит, что ты должен указать компьютеру, что за тип данных ты собираешься хранить в переменной. Тип данных — это категория данных, например:

# int (целые числа): 10, 42, -5
# float (вещественные числа): 3.14, 0.01, -2.5
# str (строки): "Привет", "Я учусь программировать"
# bool (логический тип): True (истина) или False (ложь)
# Пример на Python:

# python
# Копировать код
# age = 25  # переменная age хранит целое число
# name = "Алексей"  # переменная name хранит строку (текст)
# is_student = True  # переменная is_student хранит логическое значение
# Здесь:

# age хранит число 25.
# name хранит текст "Алексей".
# is_student хранит значение True, что означает "истина".
# 3. Операторы
# Операторы — это символы или слова, с помощью которых выполняются действия над переменными или данными. В языке программирования операторы помогают выполнять операции над данными: сложение, вычитание, сравнение, логические проверки и многое другое.

# Основные операторы:

# Арифметические операторы: выполняют математические операции, такие как сложение, вычитание, умножение и деление.

# Пример:

# python
# Копировать код
# a = 5
# b = 10
# c = a + b  # результат будет 15
# Операторы сравнения: сравнивают два значения и возвращают True (истина) или False (ложь).

# Пример:

# python
# Копировать код
# a = 5
# b = 10
# result = a < b  # результат будет True, потому что 5 меньше 10
# Логические операторы: помогают проверять несколько условий одновременно, используя логические "и" (and), "или" (or) и "не" (not).

# Пример:

# python
# Копировать код
# a = 5
# b = 10
# result = (a > 3) and (b < 15)  # результат будет True, потому что оба условия верны
# 4. Условия и ветвления
# Программы часто принимают решения, основанные на условиях. Для этого используются условные операторы, такие как if, else и elif. Это позволяет программе выбирать, что делать в зависимости от того, какое условие истинно.

# Пример:

# python
# Копировать код
# age = 18

# if age >= 18:
#     print("Вы совершеннолетний!")
# else:
#     print("Вы ещё не совершеннолетний.")
# Здесь программа проверяет, достиг ли возраст пользователя 18 лет. Если это так, она выводит "Вы совершеннолетний!". Если возраст меньше 18, программа выводит "Вы ещё не совершеннолетний."

# 5. Циклы
# Часто нужно выполнять одно и то же действие много раз. Для этого существуют циклы. Например, если нужно вывести числа от 1 до 10, можно использовать цикл вместо того, чтобы писать десять строк кода вручную.

# Пример:

# python
# Копировать код
# for i in range(1, 11):
#     print(i)
# Цикл for пробегает по значениям от 1 до 10 и выводит каждое из них на экран.

# 6. Функции
# Функция — это как мини-программа внутри программы. Она принимает на вход какие-то данные, выполняет действия и может вернуть результат. Функции помогают избежать повторяющегося кода.

# Пример:

# python
# Копировать код
# def greet(name):
#     print("Привет, " + name + "!")

# greet("Алексей")
# greet("Мария")
# Функция greet принимает имя и выводит приветствие. Мы можем вызывать эту функцию с разными именами, и она каждый раз будет выводить своё сообщение.

# 7. Библиотеки и модули
# Большинство языков программирования поддерживают использование готовых библиотек или модулей. Это наборы заранее написанных функций и классов, которые можно подключить к программе, чтобы использовать их функциональность. Например, библиотека для работы с математикой, графикой или для создания игр.

# Пример в Python:

# python
# Копировать код
# import math

# print(math.sqrt(16))  # Выведет 4, так как это квадратный корень из 16
# Здесь мы подключаем библиотеку math и используем её функцию sqrt(), чтобы найти квадратный корень числа.

# Теперь, когда мы разобрали основные элементы языка программирования, давай посмотрим на два простых примера кода с детальным объяснением каждого элемента.

# Пример 1. Программа для сложения двух чисел
# Пример:

# python
# Копировать код
# a = 10  # Переменная a хранит число 10
# b = 20  # Переменная b хранит число 20

# sum = a + b  # Переменная sum хранит результат сложения a и b

# print("Сумма:", sum)  # Выводим на экран текст "Сумма:" и результат сложения
# Разберём код:

# a = 10 и b = 20: Мы создаём две переменные, a и b, и присваиваем им значения 10 и 20 соответственно.
# sum = a + b: Мы складываем значения a и b и сохраняем результат в переменной sum. В данном случае результат будет 30.
# print("Сумма:", sum): Мы выводим на экран текст "Сумма:" и значение переменной sum. То есть программа выведет: "Сумма: 30".
# Пример 2. Программа, которая проверяет возраст пользователя
# Пример:

# python
# Копировать код
# age = int(input("Введите ваш возраст: "))  # Считываем возраст пользователя и преобразуем его в целое число

# if age >= 18:
#     print("Вы совершеннолетний!")
# else:
#     print("Вы ещё не совершеннолетний.")
# Разберём код:

# age = int(input("Введите ваш возраст: ")): Мы используем функцию input(), чтобы запросить у пользователя возраст. Введённое значение преобразуем в целое число с помощью функции int() и сохраняем его в переменной age.

# if age >= 18: Здесь программа проверяет, больше или равно ли значение age числу 18. Если да, выполняется код внутри блока if.

# print("Вы совершеннолетний!"): Если условие истинно (то есть возраст больше или равен 18), программа выводит "Вы совершеннолетний!".

# else: Если условие не выполнено (возраст меньше 18), программа переходит к блоку else.

# print("Вы ещё не совершеннолетний."): В этом случае программа выводит "Вы ещё не совершеннолетний."

# Заключение
# Мы разобрали, из чего состоит язык программирования: это синтаксис, переменные, типы данных, операторы, условия, циклы, функции и библиотеки. Все эти элементы составляют основу любого языка программирования, будь то Python, C++, Java или любой другой.

# Программирование — это процесс, где каждый шаг понятен и логичен, если разобрать его по частям. Понимание этих основных элементов даёт возможность создавать любые программы







## Модуль №4
## Компиляция и интерпретация [Python]









## Модуль №5
## Что на самом деле делает интерпретатор [Python]?









## Модуль №6
## Компиляция и интерпретация —
## преимущества и недостатки [Python]









## Модуль №7
## Что такое Python?









## Модуль №8
## Кто создал Python?









## Модуль №9
## Цели Python









## Модуль №10
## Почему Python особенный?









## Модуль №11
## Конкуренты Python?









## Модуль №12
## Где мы можем увидеть Python в действии?









## Модуль №13
## Python ака CPython









## Модуль №14
## Cython









## Модуль №15
## Jython









## Модуль №16
## PyPy и RPython









## Модуль №17
## Литералы Python










## Модуль №18
## Литералы — данные в себе [Python]









## Модуль №19
## Целые числа (Integers) [Python]









## Модуль №20
## Целые числа: восьмеричные
## и шестнадцатеричные числа [Python]








## Модуль №21
## Числа с плавающей точкой
## (Floating-point numbers) [Python]









## Модуль №22
## Кодирование чисел с плавающей точкой [Python]








## Модуль №23
## Строки [Python]








## Модуль №24
## Кодирование строк [Python]








## Модуль №25
## Булевы значения (логические типы данных) [Python]









## Модуль №26
## Ключевые выводы [Python]








## Модуль №27
## Операторы — инструменты управления данными [Python]









## Модуль №28
## Python как калькулятор [Python]








## Модуль №29
## Основные операторы [Python]









## Модуль №30
## Арифметические операторы:
## возведение в степень [Python]









## Модуль №31
## Арифметические операторы: умножение [Python]









## Модуль №32
## Арифметические операторы: деление [Python]









## Модуль №33
## Арифметические операторы:
## целочисленное деление [Python]








## Модуль №34
## Операторы: остаток
## (деление по модулю, с остатком) [Python]










## Модуль №35
## Операторы: как не делить [Python]









## Модуль №36
## Операторы: суммирование [Python]










## Модуль №37
## Оператор вычитания,
## унарные и бинарные операторы [Python]









## Модуль №38
## Операторы и их приоритеты [Python]









## Модуль №39
## Операторы и связывание [Python]









## Модуль №40
## Операторы и связывание: возведение в степень [Python]









## Модуль №41
## Список приоритетов [Python]









## Модуль №42
## Операторы и скобки [Python]









## Модуль №43
## Переменные — поля в форме данных
## Что такое переменные [Python]? 










## Модуль №44
## Правильные и неправильные имена переменных
## Ключевые слова [Python]













## Модуль №45
## Создание переменных [Python]












## Модуль №46
## Использование переменных [Python]













## Модуль №47
## Присвоение нового значения
## уже существующей переменной [Python]


















## Модуль №48
## Решение простых математических задач [Python]
















## Модуль №49
## Сокращенные формы записи [Python]
























## Модуль №50
## Ключевые выводы [Python]






























## Модуль №51
## Комментарий к комментариям [Python]
























## Модуль №52
## Комментарии в коде: зачем, как и когда [Python]





























## Модуль №53
## Ключевые выводы [Python]
































## Модуль №54
## Как общаться с компьютером [Python]

















## Модуль №55
## Функция ввода input() [Python]



























## Модуль №56
## Функция input() с аргументом [Python]



























## Модуль №57
## Результат функции input() [Python]

























## Модуль №58
## Функция input() — запрещенные операции [Python]





















## Модуль №59
## Преобразование типов [Python]



























## Модуль №60
## Больше об input() и преобразовании типов [Python]



























## Модуль №61
## Строковые операторы — введение [Python]


























## Модуль №62
## Конкатенация (concatenation) [Python]

























## Модуль №63
## Повторение строки (replication) [Python]






















## Модуль №64
## Преобразование типов: str() [Python]



























## Модуль №65
## Снова возвращаемся
## к прямоугольному треугольнику [Python]




























## Модуль №66




































## Модуль №67




























## Модуль №68



































## Модуль №69


























## Модуль №70



























## Модуль №71

























## Модуль №72





























## Модуль №73




































## Модуль №74































## Модуль №75
