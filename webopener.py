import webbrowser

url = input("Enter the url you have to open multiple-times : ")

num_times =int (input("enter the value how much time you want to open that website :"))


for _ in range(num_times):
    webbrowser.open(url)
