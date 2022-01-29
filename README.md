# About the script

This script generates a markdown table for Round-Robin events, from a provided PGN file.

# Installing

Assuming you already have Python and git installed, clone this repository and install the dependencies with the following commands.

- `git clone https://github.com/michael1241/markdown-standings.git`
- `cd markdown-standings`
- `pip install -r .\requirements.txt`

# Usage

Provide a PGN file with all tournament results as an input to this sctript. Optionally, you also have the option to provide the location and name of the output file. By default, it will be called `standings.md` and it will be generated in the script's directory.

`python main.py lichess_broadcast_tata-steel-masters-2022_IsMvGXWN_2022.01.26.pgn`

Or

`python main.py lichess_broadcast_tata-steel-masters-2022_IsMvGXWN_2022.01.26.pgn -o tata.md`

This will generate a markdown table with the current standings

|                         | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10   | 11   | 12   | 13   | 14   |   Total |
|:------------------------|:----|:----|:----|:----|:----|:----|:----|:----|:----|:-----|:-----|:-----|:-----|:-----|--------:|
| Carlsen, Magnus         | -   | 1   | 1   | 0.5 | -   | -   | 1   | 0.5 | 0.5 | 0.5  | 0.5  | -    | 1    | 0.5  |     7   |
| Giri, Anish             | 0   | -   | 0.5 | 0.5 | 0.5 | 1   | -   | 1   | 0.5 | -    | 1    | 1    | 0.5  | -    |     6.5 |
| Mamedyarov, Shakhriyar  | 0   | 0.5 | -   | -   | -   | -   | 0.5 | 0.5 | 1   | 1    | 0.5  | 0.5  | 1    | 0.5  |     6   |
| Karjakin, Sergey        | 0.5 | 0.5 | -   | -   | -   | 0.5 | 0.5 | 0   | 0.5 | 1    | -    | 0.5  | 1    | 0.5  |     5.5 |
| Vidit, Santosh Gujrathi | -   | 0.5 | -   | -   | -   | 0.5 | 0.5 | 0.5 | 0.5 | 0    | 1    | 1    | *    | 1    |     5.5 |
| Caruana, Fabiano        | -   | 0   | -   | 0.5 | 0.5 | -   | *   | 0.5 | 1   | 0.5  | 0.5  | 0.5  | -    | 1    |     5   |
| Rapport, Richard        | 0   | -   | 0.5 | 0.5 | 0.5 | *   | -   | -   | 0   | 1    | 0.5  | -    | 1    | 1    |     5   |
| Esipenko, Andrey        | 0.5 | 0   | 0.5 | 1   | 0.5 | 0.5 | -   | -   | 0.5 | *    | 0.5  | 0.5  | -    | -    |     4.5 |
| Duda, Jan-Krzysztof     | 0.5 | 0.5 | 0   | 0.5 | 0.5 | 0   | 1   | 0.5 | -   | -    | -    | 0.5  | 0.5  | -    |     4.5 |
| Van Foreest, Jorden     | 0.5 | -   | 0   | 0   | 1   | 0.5 | 0   | *   | -   | -    | -    | 0.5  | 1    | 1    |     4.5 |
| Shankland, Sam          | 0.5 | 0   | 0.5 | -   | 0   | 0.5 | 0.5 | 0.5 | -   | -    | -    | 0.5  | 0.5  | 0.5  |     4   |
| Dubov, Daniil           | -   | 0   | 0.5 | 0.5 | 0   | 0.5 | -   | 0.5 | 0.5 | 0.5  | 0.5  | -    | -    | *    |     3.5 |
| Praggnanandhaa R        | 0   | 0.5 | 0   | 0   | *   | -   | 0   | -   | 0.5 | 0    | 0.5  | -    | -    | 1    |     2.5 |
| Grandelius, Nils        | 0.5 | -   | 0.5 | 0.5 | 0   | 0   | 0   | -   | -   | 0    | 0.5  | *    | 0    | -    |     2   |