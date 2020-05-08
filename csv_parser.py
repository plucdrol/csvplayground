

filename = "input"

CSV_SEPARATOR = ";"


def _parse_array(array, length):
    split_array = array.split(", ")
    if len(split_array) != length:
        to_return = []
        for i in range(length):
            to_return.append("null")
        return CSV_SEPARATOR.join(to_return)
    split_array[0] = split_array[0][1:]
    split_array[-1] = split_array[-1][:-1]
    return CSV_SEPARATOR.join(split_array)


def _get_field(fields, field_number):
    return fields[field_number].rstrip()


def do_the_bartman():
    with open(filename, 'r') as f:
        truc = f.readlines()
        for line in truc[1:]:
            fields = line.split(CSV_SEPARATOR)
            print("fields:" + str(fields))
            first_field = _get_field(fields, 0)
            print("first field: " + first_field)


# python csv_parser.py > output
if __name__ == "__main__":
    do_the_bartman()
