from genkidama import connect_to_session

import time

import logging

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    session_local = connect_to_session("localhost")
    session_metal = connect_to_session("192.168.1.195")
    session_gosi = connect_to_session("192.168.1.207")
    session_SOTA = connect_to_session("192.168.1.187")

    sessions = [session_local,
                session_metal,
                session_gosi,
                session_SOTA]

    procs = []

    for _ in range(1000):
        procs = [s.execute("print(input())") for s in sessions]
        for proc in procs: proc.stdin.write("Hello World\n".encode())
        for proc in procs: proc.wait()
        for proc in procs: print(proc.stdout.read().decode(), end="")

