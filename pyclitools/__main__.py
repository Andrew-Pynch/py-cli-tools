import pprint


def print_symbol_row(symbol="-", length=50):
    print(f"{symbol * length}")


def print_list(list_to_print):
    for item in list_to_print:
        print(f"| {item}")


def print_json(json_to_print):
    pprint.pprint(json_to_print)


def print_data_type_retrieval(data, type, file=None):
    if file:
        print(f"Got {len(data)} of type {type} from {file}")
    else:
        print(f"Got {len(data)} of type {type}")
