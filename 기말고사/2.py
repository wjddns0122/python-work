import turtle
import sqlite3
import time

# SQLite 데이터베이스 연결과 테이블 생성
conn = sqlite3.connect('path_data.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS PathData (
    ID INTEGER PRIMARY KEY,
    LineID INTEGER,
    ColorR REAL,
    ColorG REAL,
    ColorB REAL,
    Sequence INTEGER,
    X INTEGER,
    Y INTEGER
)
''')
conn.commit()

# 거북이 설정
screen = turtle.Screen()
screen.setup(width=300, height=300)
t = turtle.Turtle()
t.speed(1)

# 거북이의 이동 경로를 저장하는 함수
def save_path_data(line_id, color, sequence, x, y):
    cursor.execute('''
    INSERT INTO PathData (LineID, ColorR, ColorG, ColorB, Sequence, X, Y)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (line_id, color[0], color[1], color[2], sequence, x, y))
    conn.commit()

# 거북이가 주어진 화면을 벗어나기 전까지 이동하면서 경로 저장
def draw_forward_and_save(line_id, color, sequence, distance):
    t.pencolor(color)
    t.forward(distance)
    x, y = t.position()
    save_path_data(line_id, color, sequence, x, y)

# 1) 순서대로 선 그리기
line_id = 1
for i in range(3):  # 2번 반복
    t.penup()
    t.goto(0, 0)
    t.pendown()
    save_path_data(line_id, (0, 0, 0), 0, 0, 0)  # 시작점 저장
    for j in range(1, 6):  # 5번 반복
        color = (0.1 * j, 0.2 * j, 0.3 * j)
        draw_forward_and_save(line_id, color, j, 10 * j)

    line_id += 1  # 다음 선분을 위해 LineID 증가

# 2) 역순대로 선 그리기
time.sleep(2)  # 2초 동안 대기 후 화면 지우기
t.clear()

# 데이터베이스에서 역순으로 경로 읽어오기
def fetch_reverse_path_data(line_id):
    cursor.execute('''
    SELECT ColorR, ColorG, ColorB, Sequence, X, Y
    FROM PathData
    WHERE LineID = ?
    ORDER BY Sequence DESC
    ''', (line_id,))
    return cursor.fetchall()

# 역순으로 선 그리기
for i in range(line_id - 1, 0, -1):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    path_data = fetch_reverse_path_data(i)
    for data in path_data:
        color = (data[0], data[1], data[2])
        draw_forward_and_save(i, color, data[3], 10)

# 데이터베이스 및 거북이 종료
conn.close()
turtle.done()
