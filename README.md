# US States Game

Welcome to the **US States Game**! This Python game allows users to guess the names of all 50 U.S. states based on a map. As you type a state's name, it will appear at the correct coordinates on the map. This game is built using the `turtle` library for graphics and `pandas` to handle state data.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Game Rules](#game-rules)
- [Contributing](#contributing)
- [License](#license)

## Installation

To play the US States Game, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/masood2004/us-states-game.git
   cd us-states-game
   ```

2. **Install dependencies**:

   This project requires the `turtle` and `pandas` libraries. If they are not installed, you can install them using `pip`:

   ```bash
   pip install pandas
   ```

   The `turtle` library is included by default in Python installations, so no additional installation is required for that.

3. **Download the required image**:
   The game uses an image of the U.S. map for displaying the states. You can download the image file (`blank_states_img.gif`) and place it in the root directory of this repository. The image is used as the background of the game.

4. **Download the CSV data**:
   The game uses a CSV file (`50_states.csv`) which contains the names and coordinates of each U.S. state. Make sure the file is in the repository directory.

## Usage

1. Run the game by executing the following command in the project directory:

   ```bash
   python main.py
   ```

2. The game window will open, showing the U.S. map. A prompt will appear asking you to guess a state's name.
3. Type a state’s name and press Enter. If you guess correctly, the state name will appear at its designated location on the map.
4. The game continues until you have guessed all 50 states or choose to exit by typing "Exit".

## Game Rules

- You need to guess all 50 U.S. states.
- After guessing a state correctly, its name will appear at its location on the map.
- The game will show a text input box where you can type the name of a state.
- If you type an incorrect or non-existing state, it will show a message "No".
- Type "Exit" at any time to quit the game.

## Contributing

We welcome contributions to improve this project. If you want to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test them.
4. Commit your changes and push them to your fork.
5. Open a pull request to the main repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
