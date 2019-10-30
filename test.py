import lyricsgenius as genius
import csv


# Insert client ID
api = genius.Genius('CGA3NpDGaDEHwWhZiKucP1DMvZm1gDFpD4nXoCsOmoprn-owOZeKK6SFbOrRycVS')

with open('tylerthecreator.csv', encoding='mac_roman') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            item_year = row[0]
            item_artist = row[1]
            item_song = row[2]
            # print(f'\t{row[0]}\t{row[1]}\t{row[2]}')
            song = api.search_song(item_song,item_artist)
            filename = item_song.replace("/","_") + "|" + item_artist.replace("/","_")
            if song is not None:
                song.save_lyrics(filename='lyrics/txt/'+filename+'.json',format_='txt')
                song.save_lyrics(filename='lyrics/json/'+filename+'.json',format_='json')

            line_count += 1

    printf('Processed {line_count} lines.')
