todos = []

while True:
    user_action = input('Type add, show, edit, or exit: ')
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('Enter a todo: ')
            todos.append(todo)
        case 'show':
            for i, todo in enumerate(todos):
                print(f'{i+1}. {todo}')
        case 'edit':
            num = int(input('Element would you like to edit: '))
            todos[num-1] = input(f"Enter the new todo, replacing '{todos[num-1]}': ")
        case 'exit':
            break

print('Bye!')