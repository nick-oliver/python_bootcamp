# CAR GAME

command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print('Car is already started!!')
        else:
            started = True
            print('The Car has Started!!')
    elif command == "stop":
        if not started:
            print("The car is already stopped")
        else:
            started = False
            print('The Car has Stopped!!')
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif command == 'quit':
        break
    else:
        print("Sorry, I don't understand that")