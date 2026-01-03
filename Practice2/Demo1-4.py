user_choice=int(input('enter the value : '))


def generate_table(a):
    for i in range(1,11):
        print(f'{user_choice} x {i} = {user_choice*i}')
        
generate_table(user_choice)