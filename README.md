Описание алгоритма:
1. Из данного на вход графа делает два новых графа.
Первый граф,в котором все вершины из S1 объединены в одну вершину A и все рёбра перевёрнуты.
При этом в новом графе только вершины,
не входящие в S1 и вершина A. Все рёбра строятся из начального графа(например,
если было ребро из некоторой вершины v, принадлежащей S1, в вершину u не из S1, то в новом графе
есть ребро из A в u)
Второй граф, в котором все вершины из S2 объединены в одну вершину B и все рёбра перевёрнуты.
При этом в новом графе только вершины,
не входящие в S2 и вершина B. Все рёбра строятся из начального графа(например,
если было ребро из некоторой вершины v, принадлежащей S2, в вершину u не из S2, то в новом графе
есть ребро из A в u)
2. Запускается поиск в ширину из A в первом графе, таким образом, мы найдём расстояние от каждой вершины до S1
(если S1 недостижимо, оно равно -1, а для вершин из S1 равно 0).
Именно для этого мы брали перевёрнутые рёбра: если в исходном графе S1 достижимо из u, то в получившемся
u достижимо из A и расстояния совпадают.
3. Создаётся словарь, где ключи - номера подходящих вершин, значения - суммарное расстояние. Если из вершины
какое-то множество не достижимо, то её не будет в этом словарике
4. Сортируем словарь


Вычислительная сложность: создание двух новых графов O(n+e), где n - количество вершин исходного, e - количество рёбер,
два поиска в ширину - каждый O(n+e). Общее время работы O(n+e)

Альтернативные способы реализации: запуск поиска в ширину из каждой вершины, пока не найдутся на пути вершины из S1 и вершины из S2.
Если вершина окажется достижимой из S1 и из S2, поиск в ширину из этой вершины прерывается,
она добавляется в множество подходящих вершин, вместе с суммой d1+d2. Потом это сортируется.
Это наивный алгоритм, который по времени займёт больше, чем приведённый алгоритм, но по памяти меньше.
Например, если нам неважно время и есть ограниченные ресурсы памяти, то он может стать альтернативой