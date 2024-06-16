# Компьютерные сети. Домашнее задание 2
## Выполнил Канищев Илья Андреевич, БКНАД212

В данной работе реализован скрипт, который находит минимальное MTU на пути к введенному пользователем адресу. Можно ввести как IP-адрес (например, `8.8.8.8`), так и человекочитаемый url (например, `google.com`). Для поиска применяется библиотека subprocess, которая позволяет запускать команды linux, такие как `ping`. Для того чтобы собственно определить MTU используется двоичный поиск по ответу: отправляется ping запрос с некоторым количеством байт, и если ping выдает ошибку, то мы пытаемся взять размер пакета меньше, а если ping завершился успешно, то пытаемся взять размер пакета больше.

### Как запускать
В папке находится dockerfile. Чтобы запустить скрипт в докере, нужно выполнить следующие команды:
```bash
docker build -t find_mtu .
docker run -it find_mtu
```