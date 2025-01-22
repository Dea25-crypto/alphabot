import os
import fnmatch
import sqlite3

class AlphaBot:
    def __init__(self, root_directory):
        self.root_directory = root_directory
        self.db_name = 'file_index.db'
        self.conn = sqlite3.connect(self.db_name)
        self.cur = self.conn.cursor()
        self._initialize_database()

    def _initialize_database(self):
        """Initialize the SQLite database."""
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS files (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                path TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def index_files(self):
        """Index files within the root directory."""
        for root, _, files in os.walk(self.root_directory):
            for filename in files:
                full_path = os.path.join(root, filename)
                self.cur.execute('INSERT INTO files (name, path) VALUES (?, ?)', (filename, full_path))
        self.conn.commit()
        print("Indexing complete.")

    def search_files(self, pattern):
        """Search for files matching the pattern."""
        self.cur.execute('SELECT path FROM files WHERE name LIKE ?', ('%' + pattern + '%',))
        results = self.cur.fetchall()
        if results:
            print("Files found:")
            for result in results:
                print(result[0])
        else:
            print("No files found.")

    def close(self):
        """Close the database connection."""
        self.conn.close()

if __name__ == '__main__':
    root_directory = input("Enter the root directory to index: ")
    alphabot = AlphaBot(root_directory)
    
    while True:
        print("\nOptions: index, search, exit")
        option = input("Choose an option: ").strip().lower()

        if option == 'index':
            alphabot.index_files()
        elif option == 'search':
            pattern = input("Enter the search pattern: ")
            alphabot.search_files(pattern)
        elif option == 'exit':
            alphabot.close()
            print("Exiting AlphaBot.")
            break
        else:
            print("Invalid option, please try again.")