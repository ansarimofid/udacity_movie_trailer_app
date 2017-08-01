import media

# Movie 1 Data
toy_story = media.Movie('Toy Story',
                        'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
                        'https://www.youtube.com/watch?v=KYz2wyBy3kc')
# Movie 2 Data
avatar = media.Movie('Avatar',
                      'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',  # noqa
                     'https://www.youtube.com/watch?v=aVdO-cx-McA')

# Movie 3 Data
despicable_me = media.Movie('Despicable Me 3',
                            'https://upload.wikimedia.org/wikipedia/en/9/91/Despicable_Me_3_%282017%29_Teaser_Poster.jpg',  # noqa
                            'https://www.youtube.com/watch?v=euz-KBBfAAo')

# Movie 4 Data
inception = media.Movie('Inception',
                        'https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg',
                        'https://www.youtube.com/watch?v=YoHD9XEInc0')


# Movie List
movies = [toy_story, avatar, inception, despicable_me]
