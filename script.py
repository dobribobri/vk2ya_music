# -*- coding: utf-8 -*-

vk_path = 'vk_audio.html'   # Локальный путь к сохраненной копии страницы со всеми вашими аудиозаписями
# (VK: Главная > Мои треки)

ya_token = '%YOUR_TOKEN_HERE%'  # Ваш токен от Яндекс.Музыки
# (см. https://github.com/MarshalX/yandex-music-api/discussions/513#discussioncomment-2729781)


from bs4 import BeautifulSoup
from yandex_music import Client
from termcolor import colored
import time


if __name__ == '__main__':

    client = Client(ya_token).init()

    playlist = client.users_playlists_create(title='VK')
    kind = playlist['kind']

    with open(vk_path, 'r') as file:

        soup = BeautifulSoup(file, "html.parser")
        audio_rows = soup.findAll('div', {'class': lambda x:
            'audio_row' in str(x).split() and '_audio_row' in str(x).split()})

        print('====================================================')
        total = len(audio_rows)
        print('VK: найдено {} аудиозаписей.\n'.format(total))

        at = 0
        for i, audio_row in enumerate(audio_rows[::1]):
            info = audio_row.find_all('a')
            name = ' '.join([a.text for a in info])
            progress = (i + 1) / total * 100.

            try:
                track = client.search(text=name).tracks.results[0]
                # Только первый трек из выдачи по соответствующему поисковому запросу
                track_id = track['id']
                album_id = track['albums'][0]['id']

                client.users_playlists_insert_track(kind=kind, track_id=track_id, album_id=album_id,
                                                    at=at,
                                                    revision=client.users_playlists(kind=kind)['revision']
                                                    )
                at += 1
                print('{:.2f}%\t\tТрек: \"{}\"\t\tРезультат: {}'.format(
                    progress, name, colored('добавлен', color='green'))
                )

            except Exception as e:
                # print(e)
                print('{:.2f}%\t\tТрек: \"{}\"\t\tРезультат: {}'.format(
                    progress, name, colored('неудача', color='red'))
                )
                continue

            finally:
                time.sleep(1)
                pass

    print('Готово!')
