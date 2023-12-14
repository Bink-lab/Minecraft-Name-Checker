import requests

print("""
██████╗░██╗███╗░░██╗██╗░░██╗░░░░░░██╗░░░░░░█████╗░██████╗░
██╔══██╗██║████╗░██║██║░██╔╝░░░░░░██║░░░░░██╔══██╗██╔══██╗
██████╦╝██║██╔██╗██║█████═╝░█████╗██║░░░░░███████║██████╦╝
██╔══██╗██║██║╚████║██╔═██╗░╚════╝██║░░░░░██╔══██║██╔══██╗
██████╦╝██║██║░╚███║██║░╚██╗░░░░░░███████╗██║░░██║██████╦╝
╚═════╝░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░░░░░░╚══════╝╚═╝░░╚═╝╚═════╝░""")

def check_username(username):
    url = f'https://api.mojang.com/users/profiles/minecraft/{username}'
    response = requests.get(url)

    if response.status_code == 200:
        return f'The username "{username}" is taken.'
    elif response.status_code == 204:
        return f'The username "{username}" is available.'
    else:
        return f'The username "{username}" might be avaliable.'
    
if __name__ == '__main__':
    username_to_check = input('Enter the username to check: ')
    result = check_username(username_to_check)
    print(result)

con = input("Press enter to continue...")