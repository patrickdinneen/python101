from flask import Flask, render_template
from dataclasses import dataclass, field
from typing import List, Dict

app = Flask(__name__)


@dataclass
class Human:
    name: str
    pets: List[str] = field(default_factory=list)


def get_humans() -> Dict[str, Human]:
    humans = [
        Human('Ada Lovelace', pets=['Bork the Dog',
                                    'Henrietta the Chicken',
                                    'Davis the Duck']),
        Human('John von Neumann', pets=['127 the Cellular Automata']),
        Human('Claude Shannon', pets=[])
    ]

    return {human.name.split()[0].lower(): human for human in humans}


humans = get_humans()

@app.route('/human/<name>', methods=['GET'])
def get_human(name):
    human = humans.get(name.lower())

    if human:
        return render_template("human.html", human=human)
    else:
        return f"Couldn't find human {name}", 404
