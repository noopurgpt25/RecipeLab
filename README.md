# EECS 337 Recipe Transformation Assignment

Python Version 3.6

Dependencies: `requests`, `beautifulsoup4`
Install: `pip install requests`, `pip install beautifulsoup4`

Our project completes the following tasks:

1. Fetches the page for a recipe on AllRecipes.com. See `recipeMain.py` for an example and `webScrape.py` for the underlying functions.

2. Parses it into a recipe data representation. Our parser recognizes ingredients (name, quantity, measurement), steps, tools, and cooking methods. See `webScrape.py`.

3. Transforms recipes along the vegetarian (see `vegitarian.py`), health (see `makeHealthy.py`), cuisine style (see `makeMexican.py`), and difficulty (see `makeSimple.py`) dimensions. Our transformations rely on a large set of constants (see `constants.py`) that represents pre-existing cooking knowledge.

TODO:
- ~~Parse tools~~
- ~~Parse methods~~
- ~~Ask user what kind of transformation~~
- Display transformed recipe in human-friendly format
- Improve vegetarian transformation
- Improve difficulty transformation