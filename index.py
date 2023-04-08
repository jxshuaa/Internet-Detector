url = "https://github.com" # You can use any website that has a good uptime.
try:
    response = requests.get(url)  # Get the responce from the url
    print("Internet check")
    time.sleep(.4)
except requests.exceptions.ConnectionError:
    # Tell the user
    input("You are not connected to internet, check your connection and try again.\nPress enter to exit")
    exit()  # Exit program explain this code in simple terms
