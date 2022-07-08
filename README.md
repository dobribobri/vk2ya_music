# vk2ya_music
Перенос аудиозаписей из ВК в Яндекс.Музыку

1. Перед запуском скрипта <i>script.py</i> убедитесь, что значения полей
<b>vk_path</b> и <b>ya_token</b> установлены верно.


2. Для работы скрипта необходимы 
- BeautifulSoup4 (https://pypi.org/project/beautifulsoup4/);
- MarshalX Yandex Music API 
(Неофициальная Python библиотека для работы с API сервиса Яндекс.Музыка
https://github.com/MarshalX/yandex-music-api);
- termcolor 1.1.0 (https://pypi.org/project/termcolor/).

Установка:
<pre>
pip3 install beautifulsoup4 termcolor yandex-music --upgrade
</pre>


3. Запуск скрипта:
<pre>
python3 script.py
</pre>


Ваши треки будут лежать 
в плейлисте с названием <b>VK</b>.


Всем хорошего настроения!
