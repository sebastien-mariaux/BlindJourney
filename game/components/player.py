from django_unicorn.components import UnicornView
from game.models import Guess, Category


class PlayerView(UnicornView):
    attempt = ''
    result = ''
    success = False
    categories = Category.objects.all()
    guess = None
    category_id = None
    attempt_count = 0
    score = 0

    def mount(self):
        self.guess = self.random_guess()

    def make_guess(self, guess_id):
        if self.success:
            self.next_guess()
            return
        guess = Guess.objects.get(id=guess_id)
        if guess.prompt == self.attempt:
            self.approve()
        else:
            self.disapprove()

    def next_guess(self):
        self.guess = self.random_guess()
        self.result = ''
        self.attempt = ''
        self.success = False

    def change_category(self, category_id):
        self.category_id = category_id
        self.guess = self.random_guess()
        print(self.guess)
        print(self.category_id)

    def approve(self):
        self.score += 1
        self.attempt_count += 1
        self.success = True
        self.result = 'Correct!'

    def disapprove(self):
        self.attempt_count += 1
        self.success = False
        self.result = 'Incorrect!'
        self.attempt = ''

    def random_guess(self):
        if self.category_id:
            return Guess.objects.filter(category__id=self.category_id).order_by('?').first()
        else:
            return Guess.objects.order_by('?').first()
