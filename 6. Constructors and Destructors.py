class Logger:
    def __init__(self):
        print("Meesage befor :Logger cobject created.")

    def __del__(self):
        print("Message after : Logger object destructor.")


log = Logger()
del log