import fresh_tomatoes
import media

wonder_woman = media.Movie(
                            "Wonder Woman",
                            "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",  # noqa
                            "https://www.youtube.com/watch?v=1Q8fG0TtVAY"
                            )

beauty_and_the_beast = media.Movie(
                                    "Beauty and the Beast",
                                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTUwNjUxMTM4NV5BMl5BanBnXkFtZTgwODExMDQzMTI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # noqa
                                    "https://www.youtube.com/watch?v=e3Nl_TCQXuw"  # noqa
                                    )

fantastic_beasts = media.Movie(
                                "Fantastic Beasts",
                                "https://images-na.ssl-images-amazon.com/images/M/MV5BMjMxOTM1OTI4MV5BMl5BanBnXkFtZTgwODE5OTYxMDI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # noqa
                                "https://www.youtube.com/watch?v=VYZ3U1inHA4"  # noqa
                                )

la_la_land = media.Movie(
                        "La La Land",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMzUzNDM2NzM2MV5BMl5BanBnXkFtZTgwNTM3NTg4OTE@._V1_SY1000_SX675_AL_.jpg",  # noqa
                        "https://www.youtube.com/watch?v=0pdqf4P9MB8"
                        )

doctor_strange = media.Movie(
                            "Doctor Strange",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BNjgwNzAzNjk1Nl5BMl5BanBnXkFtZTgwMzQ2NjI1OTE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # noqa
                            "https://www.youtube.com/watch?v=HSzx-zryEgM"  # noqa
                            )

zootopia = media.Movie(
                        "Zootopia",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BOTMyMjEyNzIzMV5BMl5BanBnXkFtZTgwNzIyNjU0NzE@._V1_SY1000_SX675_AL_.jpg",  # noqa
                        "https://www.youtube.com/watch?v=g9lmhBYB11U"
                        )

movies = [
          fantastic_beasts, wonder_woman, beauty_and_the_beast,
          la_la_land, doctor_strange, zootopia
         ]

fresh_tomatoes.open_movies_page(movies)
