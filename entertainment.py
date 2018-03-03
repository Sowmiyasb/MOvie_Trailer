import media
import fresh_tomatoes



The_Pursuit_of_Happiness = media.Movie("The Pursuit of happiness",
                       "Chris Gardner takes up an unpaid internship in a brokerage firm after he loses his life's earnings selling a product"
"he invested in. His wife leaves him and he is left with the custody of his son.",
                       "http://myworldtoyou.com/wp-content/uploads/The-pursuit-of-happiness.jpg",
                       "https://youtu.be/89Kq8SDyvfg"
                       )

Cast_Away = media.Movie("Cast Away",
                        "Chuck Noland wakes up on a deserted island after his plane crash-lands in the Pacific. He must harness every skill" "he knows to survive the mental and physical agony of living alone.",
                        "http://cinema.com/image_lib/3870_heading.jpg",
                        "https://youtu.be/PJvosb4UCLs"
                        )
Divergent = media.Movie("Divergent",
                                  "Tris, an adult resident of a futuristic world divided into five factions, elects to join the Dauntless" "faction. But she actually belongs to another faction, which she must hide, as a major war looms.",
                                  "https://www.lionsgate.com/uploads/cache/d1/84/d1845d98ad14b25f9bbcc5c9caf1ae30.jpg",
                                  "https://youtu.be/sutgWjz10sM"
                                  )

Lucy = media.Movie("Lucy",
                    "A woman's strength and thinking power grow exponentially after the effects of a performance-enhancing drug set in.",
                    "http://cdn.movieweb.com/img.site/PHAvqqn2hR0yDE_1_l.jpg",
                    "https://youtu.be/MVt32qoyhi0"
                    )

The_Fault_In_Our_Stars = media.Movie("The Fault in Our stars",
                     "Teenager Hazel Grace's life changes when she meets Augustus Waters at a cancer support group. The two then embark on"  "a life-changing journey which brings them even closer.",
                   " http://images.hellogiggles.com/uploads/2016/11/07065812/fault-in-our-stars-shailene-woodley.jpg",
                     "https://youtu.be/9ItBvH5J6ss"
                     )
Life_Of_Pi = media.Movie("Life of Pi",
                     "Pi Patel finds a way to survive in a lifeboat that is adrift in the middle of nowhere. His fight against the odds is" "heightened by the company of a hyena and a male Bengal tiger.",
                     "https://upload.wikimedia.org/wikipedia/en/5/57/Life_of_Pi_2012_Poster.jpg",
                     "https://youtu.be/j9Hjrs6WQ8M"
                     )





# creating a list of all the movies
list_of_movies = [
                  The_Pursuit_of_Happiness,
                  Cast_Away,
                  Divergent,
                  Lucy,
                  The_Fault_In_Our_Stars,
                  Life_Of_Pi
                  ]

# sending the list to fresh_tomatoes.py file to open web page
fresh_tomatoes.open_movies_page(list_of_movies)
