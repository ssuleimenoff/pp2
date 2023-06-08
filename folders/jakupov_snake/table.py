import psycopg2
def user_table():
    conn = psycopg2.connect('snake_game.db')
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE snake_users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE)'''
    );
    print('[INFO] Table created successfully!')
    conn.commit()
    cur.close()
    conn.close()
def user_score_table():
    conn = psycopg2.connect('snake_game.db')
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE user_score (
    score_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    level INTEGER,
    score INTEGER,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES  snake_users(user_id));''')