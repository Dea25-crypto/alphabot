# AlphaBot

AlphaBot is a Python-based program designed to facilitate rapid file searching and indexing on Windows systems for quicker data retrieval. It leverages SQLite to maintain an index of files, allowing users to perform searches efficiently.

## Features

- **Index Files**: Traverse a specified directory and index all files found within it.
- **Search Files**: Quickly search for files using a pattern match on file names.
- **Persistent Storage**: Uses SQLite to store file indices, ensuring data persistence across sessions.

## Requirements

- Python 3.x
- SQLite3 (comes bundled with Python)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd alphabot
   ```

2. Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/).

## Usage

1. Run the script:
   ```bash
   python alphabot.py
   ```

2. Enter the root directory you want to index when prompted.

3. Use the options provided in the program:
   - `index`: Index all files in the specified directory.
   - `search`: Search for files using a partial or full file name.
   - `exit`: Exit the program.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for review.