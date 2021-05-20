from flask import Flask
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
        html_part1 = f"""
<html>
    <body>
        <h1>{human.name}</h1>
"""

        pets_html = ""

        if human.pets:
            pets_html += "<h2>Pets</h2><ul>"
            for pet in human.pets:
                pets_html += f"<li>{pet}</li>"
            pets_html += "</ul>"
        else:
            pets_html += "<h2>No pets! :(</h2>"
        
        html_part2 = "</body></html>"

        return html_part1 + pets_html + html_part2
    else:
        return f"Couldn't find human {name}", 404
