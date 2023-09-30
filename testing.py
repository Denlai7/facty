
def create_table():
    conn = sqlite3.connect("main.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS user_input (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            input_text TEXT
        )
        """
    )
    conn.commit()
    conn.close()

def insert_input(input_text):
    conn = sqlite3.connect("main.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user_input (input_text) VALUES (?)", (input_text,))
    conn.commit()
    conn.close()

def get_all_inputs():
    conn = sqlite3.connect("main.db")
    cursor = conn.cursor()
    cursor.execute("SELECT input_text FROM user_input")
    rows = cursor.fetchall()
    conn.close()
    return [row[0] for row in rows]

def main():
    create_table()
    print("Type your input. Enter 'exit' to stop.")
    while True:
        user_input = input(">> ")
        if user_input.lower() == "exit":
            break
        insert_input(user_input)

    print("Stored inputs:")
    stored_inputs = get_all_inputs()
    for input_text in stored_inputs:
        print(input_text)
