from django_unicorn.components import UnicornView
from game.models import Guess, Category


STATES = {
    'initial': {
        'success': False,
        'allow_skip': False,
        'allow_guess': True,
        'display_answer': False,
        'allow_next': False,
        'show_result': False,
        'allow_give_up': False
    },
    'success': {
        'success': True,
        'allow_skip': False,
        'allow_guess': False,
        'display_answer': True,
        'allow_next': True,
        'show_result': True,
        'allow_give_up': False
    },
    'failure': {
        'success': False,
        'allow_skip': False,
        'allow_guess': True,
        'display_answer': False,
        'allow_next': False,
        'show_result': True,
        'allow_give_up': True
    },
    'answer': {
        'success': False,
        'allow_skip': False,
        'allow_guess': False,
        'display_answer': True,
        'allow_next': True,
        'show_result': False,
        'allow_give_up': False
    }
}


class PlayerView(UnicornView):
    categories = Category.objects.all()
    category_id = None
    attempt_count = 0
    score = 0
    attempt = ''
    guess = None

    display = STATES['initial']

    def mount(self):
        self.guess = self.random_guess()

    def make_guess(self, guess_id):
        guess = Guess.objects.get(id=guess_id)
        if guess.prompt == self.attempt:
            self.approve()
        else:
            self.disapprove()

    def skip(self):
        self.next_guess()

    def next_guess(self):
        self.guess = self.random_guess()
        self.result = ''
        self.attempt = ''
        self.set_state('initial')

    def change_category(self, category_id):
        self.category_id = category_id
        self.guess = self.random_guess()
        self.set_state('initial')

    def approve(self):
        self.guess.save_good_guess()
        self.score += 1
        self.attempt_count += 1
        self.set_state('success')

    def disapprove(self):
        self.guess.save_bad_guess()
        self.attempt_count += 1
        self.attempt = ''
        self.set_state('failure')

    def give_up(self):
        self.set_state('answer')

    def random_guess(self):
        if self.category_id:
            return Guess.objects.filter(category__id=self.category_id).order_by('?').first()
        else:
            return Guess.objects.order_by('?').first()

    def set_state(self, state):
        self.display = STATES[state]
