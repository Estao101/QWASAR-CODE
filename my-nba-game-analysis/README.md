# Welcome to My Nba Game Analysis
***

## Task
The goal is to analyze an NBA game play-by-play file and extract relevant in-game statistics such as successful 3-point shots by individual players.
The challenge lies in correctly parsing structured text data and identifying meaningful patterns using regular expressions.

## Description
The project reads a play-by-play .txt file in pipe-delimited (|) format.
It uses Python's csv module to load the data, applies regular expressions to identify specific play actions (like 3-point jump shots), 
and then attributes these plays to either the home or away team based on metadata in the file.

## Installation
Make sure you have Python 3 installed.
No external packages are required. Do not forget to import re

## Usage
Place the input file (e.g. nba_game_warriors_thunder_20181016.txt) in the same directory.

Run the analysis script using python my_nba_game_analysis.py
It will print play actions matching the defined regular expressions (currently looking for "makes 3-pt jump shot"). 
You can expand the logic to extract more stats or generate reports.
```
./my_project argument1 argument2
```

### The Core Team


<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>
