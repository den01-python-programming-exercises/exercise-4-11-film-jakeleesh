class Film:
    def __init__(self, film_name, film_age_rating):
        self.film_name = film_name
        self.film_age_rating = film_age_rating

    def name(self):
        return self.film_name

    def age_rating(self):
        return self.film_age_rating