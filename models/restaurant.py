from models.avaluation import Evaluation


class Restaurant:
    restaurants = []

    def __init__(self, name, categorie):
        self._name = name.title()
        self.categorie = categorie.upper()
        self._active = False
        self._evaluations = []
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f"{self._name} | {self.categorie}"

    @classmethod
    def list_restaurants(cls):
        print(
            f"{'Nome'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'} "
        )
        for restaurant in cls.restaurants:
            print(
                f"{restaurant._name.ljust(25)} | {restaurant.categorie.ljust(25)} | {str(restaurant.media_evaluations).ljust(24)}  | {restaurant.active}"
            )

    @property
    def active(self):
        return "Ativo" if self._active else "Inativo"

    def update_status(self):
        self._active = not self._active

    def get_avaluation(self, client, score):
        if 0 < score <= 5:
            avaluation = Evaluation(client, score)
            self._evaluations.append(avaluation)

    @property
    def media_evaluations(self):
        if not self._evaluations:
            return '-'
        sum_scores = sum(evalutation._score for evalutation in self._evaluations)
        qtd_scores = len(self._evaluations)
        media = round(sum_scores / qtd_scores, 1)
        return media
