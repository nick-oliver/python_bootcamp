playlist = {
	'title': 'patagonia bus',
	'author': 'colt steele',
	'songs': [
        {
        'title': 'song1',
        'artist': ['blue'],
        'duration': 2.4
        },
        {
        'title': 'song2',
        'artist': ['squeakers','kitten'],
        'duration': 6.6
        },
        {
        'title': 'song3',
        'artist': ['browse'],
        'duration': 5.0
        },
	]
}

for song in playlist['songs']:
	print(song['title'])

total_length = 0
for song in playlist['songs']:
	total_length += song['duration']
	
print(total_length)
