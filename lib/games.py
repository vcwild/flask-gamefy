class Game:
    def __init__(self, name, category, console) -> None:
        self.name = name
        self.category = category
        self.console = console



games_list = [
    Game('Killer Instinct', 'Fight', 'Dreamcast'),
    Game('Mortal Kombat', 'Fight', 'SNES'),
    Game('Pokémon', 'RPG', 'GBA'),
    Game('Super Mario', 'Adventure', 'SNES'),
    Game('Tetris', 'Puzzle', 'NES')
]