1. Взял список фильмов про свадьбу отсюда [с КиноПоиска+](http://plus.kinopoisk.ru/catalogue/?tags=свадьба)
2. Скопировал весь html страницы в [отдельный файл](https://github.com/matyuschenko/wedding-films/blob/master/kp-wed-top-html.txt). Так нужно, потому что страница загружается динамически при прокрутке, и обычными средствами её всю сразу не распарсить.
3. По регулярке [вытащил из html](https://github.com/matyuschenko/wedding-films/blob/master/get_id.py) ссылки на фильмы. Сохранил отдельными файлами [ссылки](https://github.com/matyuschenko/wedding-films/blob/master/urls.txt) и [id](https://github.com/matyuschenko/wedding-films/blob/master/ids.txt).
4.  Распарсил страницы фильмов на старом КиноПоиске, вытащил вот такую инфу:
  * год выхода
  * страну
  * имя режиссёра (возможно, заметим какого-то «свадебного» режиссёра)
  * список актёров (то же самое)
  * жанры
  * продолжительность
  * рейтинг
  * количество голосов (косвенно показывает популярность и известность фильма)
