from utils.utils import loads_json, shows_last_operations

if __name__ == '__main__':
    all_operations = loads_json('operations.json')
    all_operations = filter(lambda item: item.get('date') and item['state'] == "EXECUTED", all_operations)
    all_operations = sorted(all_operations, key=lambda item: item['date'])[:-6:-1]

    shows_last_operations(all_operations)






