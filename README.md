# Variant 7 (Egor Baklanov, BS17-03)

#### Содержание:
1. [Уравнение](#eq)
2. [Решение](#solution)
2. [Метод Эйлера](#euler)
3. [Усовершенствованный метод Эйлера](#imp_euler)
4. [Классический метод Рунге-Кутты](#runge_kutta)
5. [Сравнение методов для заданной задачи](#comparing)
6. [Заключение](#conclusion)
7. [Запуск](#launch)
8. [Ссылки](#links)

## <a name="eq"></a>Уравнение
№7:

<img src="http://latex.codecogs.com/gif.latex?-x%20&plus;%20%5Cfrac%7By%282x&plus;1%29%7D%7Bx%7D">

## <a name="solution"></a>Решение
<img src="https://image.ibb.co/feWJq0/Screenshot-2018-11-03-at-23-07-50.png">

Пусть: <img src="http://latex.codecogs.com/gif.latex?u(x)%20=e^{-2x}/x">

Домножим обе части уравнения на u(x):

<img src="https://image.ibb.co/mbF6tL/Screenshot-2018-11-03-at-23-28-46.png">

Заменяем страшную штуку на первообразную от нее:

<img src="https://image.ibb.co/mraLnf/Screenshot-2018-11-03-at-23-38-47.png">

Используем ету замечательную формулу:

<img src="https://image.ibb.co/cN3qnf/Screenshot-2018-11-03-at-23-43-19.png">


<img src="https://image.ibb.co/mfMzf0/Screenshot-2018-11-03-at-23-45-09.png">

Вуаля

<img src="http://latex.codecogs.com/gif.latex?y%28x%29%20%3D%20x%28C1*e%5E%7B2x%7D&plus;%5Cfrac%7B1%7D%7B2%7D%29">


## <a name="euler"></a>Метод Эйлера

Метод Эйлера дает возможность приближенно выразить функцию теоретически с любой наперед заданной точностью. Суть метода Эйлера в пошаговом вычислении значений решения y=y(x) дифференциального уравнения вида y’=f(x,y) с начальным условием (x0;y0).
Метод Эйлера является методом 1-го порядка точности и называется методом ломаных. 

Для вычисления используются следующие формулы:

<img src="https://latex.codecogs.com/gif.latex?\left\{\begin{matrix}&space;&x_{n&plus;1}=x_{n}&space;&plus;&space;h&space;\\&space;&y_{n&plus;1}=y_{n}&space;&plus;&space;hf(x_{i},&space;y_{i})&space;\end{matrix}\right.">

В Python:
	
	res = []
    while x < _to:
        res.append([x, y])
        f = get_function_value(funct, x, y=y)
        hf = step * f
        x += step
        y += hf
    return res    

## <a name="imp_euler"></a>Усовершенствованный метод Эйлера

Суть усовершенствованного метода Эйлера в пошаговом вычислении значений решения y=y(x) дифференциального уравнения вида y’=f(x,y) с начальным условием (x0;y0).
Усовершенствованный метод Эйлера является методом 2-го порядка точности и называется модифицированным методом Эйлера.

Разница между данным методом и методом Эйлера минимальна и заключается в использовании следующих формул:

<img src="https://latex.codecogs.com/gif.latex?\left\{\begin{matrix}&space;&x_{n&plus;1}=x_{n}&space;&plus;&space;h&space;\\&space;&y_{n&plus;1}=y_{n}&space;&plus;&space;\Delta&space;y&space;\\&space;&\Delta&space;y&space;=&space;hf(x_{n}&space;&plus;&space;\frac{h}{2},&space;y_{n}&space;&plus;&space;\frac{h}{2}f(x_{i},y_{i})))&space;\end{matrix}\right.">

В Python:
	
	res = []
    while x < _to:
        res.append([x, y])
        x_t = x + step / 2
        f_t = get_function_value(funct, x=x, y=y)
        y_t = y + step * f_t / 2
        f_res = get_function_value(funct, x=x_t, y=y_t)
        d_y = f_res * step
        y = y + d_y
        x = x + step
    return res


## <a name="runge_kutta"></a>Классический метод Рунге-Кутты
Суть метода Рунге-Кутты в пошаговом вычислении значений решения y=y(x) дифференциального уравнения вида y’=f(x,y) с начальным условием (x0;y0).
Классический метод Рунге-Кутты является методом 4-го порядка точности и называется методом Рунге-Кутты 4-го порядка точности.

Ну и как обычно, формулы:

<img src="https://latex.codecogs.com/gif.latex?\left\{\begin{matrix}&space;&x_{n&plus;1}=x_{n}&space;&plus;&space;h&space;\\&space;&y_{n&plus;1}=y_{n}&space;&plus;&space;\Delta&space;y&space;\\&space;&\Delta&space;y&space;=&space;\frac{k_{1}&plus;2k_{2}&plus;2k_{3}&plus;k_{4}}{6}&space;\\&space;&k_{1}&space;=&space;hf(x_{n},&space;y_{n})&space;\\&space;&k_{2}&space;=&space;hf(x_{n}&space;&plus;&space;\frac{h}{2},&space;y_{n}&space;&plus;&space;\frac{k_{2}}{2})\\&space;&k_{3}&space;=&space;hf(x_{n}&space;&plus;&space;\frac{h}{2},&space;y_{n}&space;&plus;&space;\frac{k_{2}}{2})&space;\\&space;&k_{4}&space;=&space;hf(x_{n}&space;&plus;&space;h,&space;y_{n}&space;&plus;&space;k_{3})&space;\end{matrix}\right.">

В Python:
	
	res = []
    while x < _to:
        res.append([x, y])
        k1 = get_function_value(funct, x=x, y=y)
        k2 = get_function_value(funct, x=x + step / 2, y=y + step * k1 / 2)
        k3 = get_function_value(funct, x=x + step / 2, y=y + step * k2 / 2)
        k4 = get_function_value(funct, x=x + step, y=y + step * k3)
        d_y = step / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        x += step
        y += d_y
    return res

## <a name="comparing"></a>Сравнение методов для заданной задачи
<figure>
<img src="https://image.ibb.co/j2QZf0/Screenshot-2018-11-03-at-23-58-46.png">
<figcaption>График всех методов на промежутке [1, 18.2] с шагом 0.2. Как видите, с методом Эйлера все очень плохо.</figcaption>
</figure>

<figure>
<img src="https://image.ibb.co/bWf0L0/Screenshot-2018-11-04-at-00-01-04.png">
<figcaption>Размер ошибки всех методов на промежутке [0, 18.2] с шагом 0.2. Где-то там на дне Рунге-Кутта</figcaption>
</figure>

## <a name="conclusion"></a>Заключение

Очевидно что, классический метод Рунге-Кутты справляется с задачей аппроксимации в случае данного уравнения намного лучше чем Метод Эйлера и Усовершенствованный метод Эйлера. 

## <a name="launch"></a>Запуск

1. Установить Python3
2. Все пакеты необходимые для работы находятся в **requirements.txt** (лучше в венве)
    ```
    pip3 install -r requirements.txt
    ```
3. Запустить app.py в корневой директории проекта
4. Открыть `http://127.0.0.1:5000/` в броузере
5. ???
6. Profit

### <a name="links"></a>Ссылки
Latex Редактор: <a href="https://www.codecogs.com/latex/eqneditor.php">https://www.codecogs.com/latex/eqneditor.php</a><br>
Метод Эйлера: <a href="https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D1%82%D0%BE%D0%B4_%D0%AD%D0%B9%D0%BB%D0%B5%D1%80%D0%B0">Wikipedia</a>
<br>
Усовершенствованный метод Эйлера: <a href="http://mathprofi.ru/metody_eilera_i_runge_kutty.html">Mathprofi</a> (кык)
<br>
Метод Рунге — Кутты: <a href="https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D1%82%D0%BE%D0%B4_%D0%A0%D1%83%D0%BD%D0%B3%D0%B5_%E2%80%94_%D0%9A%D1%83%D1%82%D1%82%D1%8B">Wikipedia</a>