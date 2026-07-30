class Flower:
    def __init__(self, color, freshness, stem_length, price, lifetime):
        self.color = color
        self.freshness = freshness
        self.stem_length = stem_length
        self.price = price
        self.lifetime = lifetime


class Iris(Flower):
    flower_type = 'Iris'


class Tulip(Flower):
    flower_type = 'Tulip'


class Carnation(Flower):
    flower_type = 'Carnation'


class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers

    def get_price(self):
        total_price = 0

        for flower in self.flowers:
            total_price += flower.price

        return total_price

    def get_lifetime(self):
        total_lifetime = 0

        for flower in self.flowers:
            total_lifetime += flower.lifetime

        return total_lifetime / len(self.flowers)

    def sort_by_freshness(self):
        self.flowers.sort(key=lambda flower: flower.freshness)

    def sort_by_color(self):
        self.flowers.sort(key=lambda flower: flower.color)

    def sort_by_stem_length(self):
        self.flowers.sort(key=lambda flower: flower.stem_length)

    def sort_by_price(self):
        self.flowers.sort(key=lambda flower: flower.price)

    def find_by_lifetime(self, lifetime):
        found_flowers = []

        for flower in self.flowers:
            if flower.lifetime == lifetime:
                found_flowers.append(flower)

        return found_flowers


iris1 = Iris('purple', 5, 45, 300, 7)
iris2 = Iris('pink', 4, 40, 250, 6)
tulip1 = Tulip('yellow', 3, 35, 200, 5)
tulip2 = Tulip('orange', 5, 40, 250, 5)
carnation1 = Carnation('peach', 4, 60, 400, 8)

flowers = [iris1, iris2, tulip1, tulip2, carnation1]

bouquet = Bouquet(flowers)

print('Bouquet price:', bouquet.get_price())
print('Bouquet life time:', bouquet.get_lifetime())

bouquet.sort_by_price()

for flower in bouquet.flowers:
    print(
        flower.flower_type,
        flower.color,
        flower.freshness,
        flower.stem_length,
        flower.price,
        flower.lifetime
    )

found_flowers = bouquet.find_by_lifetime(5)

print('Flowers with lifetime 5:')

for flower in found_flowers:
    print(flower.flower_type, flower.color)
