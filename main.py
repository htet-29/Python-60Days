import webbrowser

search_term = input("Enter search term: ").replace(" ", "+")

webbrowser.open("https://www.google.com/search?q=" + search_term)