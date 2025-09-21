# Py Map Quiz Game 🗺️❓

An interactive geography quiz game built with **Python Turtle Graphics** where players test their knowledge by guessing U.S. states and seeing them appear on the map.

---

## Demo / Preview

![Game Screenshot](game-video.gif)

---

## Table of Contents

- [Features](#features)  
- [Project Structure](#project-structure)  
- [Game Rules](#game-rules)  
- [Installation](#installation)  
- [Running-the-Game](#running-the-game)  
- [Usage](#usage)  
- [Future Improvements](#future-improvements)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Features

- Interactive U.S. states guessing game.  
- Uses **Turtle Graphics** to display a map and place state names on correct coordinates.  
- Accepts text input for state names.  
- Keeps track of guessed and missing states.  
- Provides a CSV file with states not guessed for further learning.  
- Simple, beginner-friendly Python project.  

---

## Project Structure

```
py-map-quiz-game/
│
├── 50_states.csv        # Dataset containing all U.S. states with their x,y coordinates
├── blank_states_img.gif # Map outline used as the game background
├── main.py              # Main game logic
├── Demo.png             # Screenshot/demo image of the game
└── README.md            # Project documentation
```

---

## Game Rules

1. The map of the United States will appear.  
2. You’ll be prompted to guess a U.S. state.  
3. If correct, the state’s name will be displayed at its correct location on the map.  
4. The game continues until all 50 states are guessed or you exit.  
5. At the end, a `states_to_learn.csv` file is generated with the states you missed.  

---

## Installation

1. Clone this repository:  
   ```bash
   git clone https://github.com/ShaileshLambode/py-map-quiz-game.git
   ```
2. Navigate into the project folder:  
   ```bash
   cd py-map-quiz-game
   ```
3. Install dependencies (Python 3.x required). No external libraries needed except the built-in `turtle` and `pandas`:  
   ```bash
   pip install pandas
   ```

---

## Running the Game

Run the main script using:  
```bash
python main.py
```

---

## Usage

- Type the name of a U.S. state in the input box.  
- Correct guesses will appear on the map.  
- Type "Exit" to quit early and generate a list of missing states.  

---

## Future Improvements

- Add support for different countries and regions.  
- Implement difficulty levels (time-based, limited attempts, etc.).  
- Improve visuals with better map graphics.  
- Add a scoring system with progress tracking.  

---

## Contributing

Contributions are welcome!  
1. Fork the repository  
2. Create a new branch (`feature-name`)  
3. Commit your changes  
4. Open a pull request  

