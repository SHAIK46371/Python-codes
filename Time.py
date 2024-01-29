import datetime

def display_current_time():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_time}")

if __name__ == "__main__":
    display_current_time()

