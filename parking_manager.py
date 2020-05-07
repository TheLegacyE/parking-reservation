import serial
import sqlite3
from datetime import datetime

LED_GREEN = 4
LED_RED = 8
BUZZER = 3

PORT = '/dev/tty.usbmodem141401'
BUAD = 9600

def create_primary_table(cur, conn):
    cur.execute('''CREATE TABLE IF NOT EXISTS ParkingManager (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "datetime" TEXT,
    "parking_space" TEXT NOT NULL,
    "state" TEXT NOT NULL
);''')
    conn.commit()

def update_states(cur, conn, data: list):
    cur.executemany('''INSERT INTO ParkingManager (
        datetime, parking_space, state
    )
    VALUES (
        ?, ?, ?
    )''', data)
    conn.commit()

def update_state(cur, conn, datum: list):
    cur.execute('''INSERT INTO ParkingManager (
        datetime, parking_space, state
    )
    VALUES (
        ?, ?, ?
    )''', datum)
    conn.commit()

def main():
    # CREATE DATABASE
    # ========================================
    # db = 'ParkingManager.db'
    db = ':memory:'


    conn = sqlite3.connect(db)
    cur = conn.cursor()

    # # Dummy Data
    # data = [
    #     (datetime.now().isoformat(), 1, "occupied"),
    #      (datetime.now().isoformat(), 1, "vacant"),
    #      (datetime.now().isoformat(), 1, "occupied"),
    # ]

    datum = (datetime.now().isoformat(), 1, "occupied")


    create_primary_table(cur, conn)
    # update_states(cur, conn, data)
    # update_state(cur, conn, datum)

    # # MONITOR SERIAL
    # # ========================================
    ser = serial.Serial(PORT, BUAD, timeout = 1)
    while True:
        if (ser.in_waiting > 0):
            line = ser.readlines()

            if line == str(LED_GREEN):
                datum = (datetime.now().isoformat(), 1, "vacant")
            elif line == str(LED_RED):
                datum = (datetime.now().isoformat(), 1, "occupied")
            print(datum)    
            update_state(cur, conn, datum)

    # # Close out serial
    # # ----------------------------------------
    ser.close()

    # Close out connection and cursor
    # ----------------------------------------
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
