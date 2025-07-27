
    while True:
        print("Select a generator:")
        for key, value in generator_options.items():
            print(key, value.__name__)

        generator_choice = input("Enter the number of your choice: ")
        if generator_choice in generator_options:
            break
        else:
            print("Invalid input! Please enter a valid generator choice.")

    while True:
        width_input = input("Enter the width for the maze: ")
        if width_input.isdigit():