# WordleSolver

## Running

This is an algorithm to solve Wordle. It can be run using by moving to the home directory of the repo and running

```
python3 main.py
```

## Usage

To use the algorithm, you'll use the correct and incorrect letters as returned by Wordle as inputs into the algorithm.

First, you have to choose a word to input into Wordle before obtaining any inputs for the algorithm. I'd recommend `crane`.


The algorithm will ask which letters are correct (green) or partially correct (yellow). You can input
them after the first prompt, using lowercase letters for partially correct letters, uppercase letters for correct
letters, and underscores for incorrect letters. The order in which you put the letters is important.


Then, the algorithm will ask for which letters were incorrect. Simply input any letters which are incorrect.
The ordering of the letters does not matter.

Lastly, the algorithm will provide a list of possible words that can be formed from the provided letters.
The first few words are likely to be more helpful. 

If you want more words, than the algorithm outputs the first time, you can input nothing at the first prompt and the algorithm
will search for more words.

The algorithm will repeat this process until find the correct word, at which point you can type "done" for the first
prompt and the program will exit.

## Example (Wordle 246)

```
Whats the result? Lowercase if wrong position, Uppercase if correct, Underscore if unknown. If no words, hit enter and if finished, type done.
____E
Wrong Letters?
cran
Possible words: ['slime', 'fudge', 'spite', 'guile', 'pulse', 'style', 'bilge', 'slope', 'those', 'lithe', 'bulge', 'tilde', 'thyme', 'lodge', 'slide', 'imbue', 'guise', 'utile', 'budge', 'flute', 'plume', 'boule', 'biome', 'mouse', 'suite', 'smote', 'globe', 'midge', 'house', 'poise', 'flume', 'glide', 'bugle', 'guide', 'smile', 'smite', 'stole', 'louse', 'issue', 'ledge', 'tithe', 'butte', 'loose', 'bible', 'diode', 'elite', 'liege', 'elope', 'etude', 'tulle', 'fugue', 'belie', 'moose', 'segue', 'theme', 'hedge', 'dodge', 'posse', 'goose', 'gouge', 'these', 'obese', 'elide', 'title', 'elude', 'siege', 'geese', 'belle', 'tepee', 'melee', 'femme']

Whats the result? Lowercase if wrong position, Uppercase if correct, Underscore if unknown. If no words, hit enter and if finished, type done.
____E
Wrong Letters?
slim
Possible words: ['vogue', 'budge', 'fudge', 'booze', 'gouge', 'dodge', 'evoke', 'etude', 'wedge', 'fugue', 'hedge', 'butte', 'tepee']

Whats the result? Lowercase if wrong position, Uppercase if correct, Underscore if unknown. If no words, hit enter and if finished, type done.
_Og_E
Wrong Letters?
vu
Possible words: ['dodge']

Whats the result? Lowercase if wrong position, Uppercase if correct, Underscore if unknown. If no words, hit enter and if finished, type done.
done

Process finished with exit code 0
```

## Testing

To test it on today's Wordle, visit https://www.nytimes.com/games/wordle/index.html.

If you'd like to test it on old Wordles, feel free to visit https://metzger.media/games/wordle-archive/.


