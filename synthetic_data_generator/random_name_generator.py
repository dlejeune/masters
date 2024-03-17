import adjectives_and_nouns
import random


def get_random_name(exclude=None):
    potential_name = f"{random.choice(adjectives_and_nouns.adjectives)}_{random.choice(adjectives_and_nouns.nouns)}"
    if exclude is None:
        return potential_name
    else:
        while potential_name in exclude:
            potential_name = f"{random.choice(adjectives_and_nouns.adjectives)}_{random.choice(adjectives_and_nouns.nouns)}"

        return potential_name
