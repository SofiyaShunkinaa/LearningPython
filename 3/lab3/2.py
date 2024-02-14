shopping_list = []
item=''
while item != 'готово':
    item=input('Enter item name: ')
    if item != 'готово':
        shopping_list.append(item)
if not shopping_list:
    print('No items')
else:
    print(shopping_list)
update_index = int(input('Enter index to update: '))
shopping_list[update_index] = input('Enter changes: ')
print(shopping_list)
delete_index = input('Enter element to delete: ')
if delete_index in shopping_list:
    shopping_list.remove(delete_index)
else:
    print('Item is not in shopping list')
print(shopping_list)
shopping_list.sort()
for item in shopping_list:
    print(item)
print("List length: ", len(shopping_list))