from email.mime import base


def print_stats(data: list[dict]) -> None:
    """
    Accepts a dataset stored as a list of dictionaries.
    Prints each column's name, and its most common value (for text columns)
    or it's average value (for numeric columns)
    """
    
    # assuming that all dictionaries in the list will have same keys
    columns = data[0].keys()

    for column in columns:
        # determine if this is a text or numeric column
        if type(data[0][column]) == float:
            # process this as a numeric column
            total = sum(row[column] for row in data) / len(data)
            print(f"{column}: average {round(total, 1)}")
            pass # not in this partial solution :)

        else:  # this is a text column
            
            # build a dict that counts number of times we've seen each value
            # within this column
            value_counts = dict()
            for row in data:
                value_counts[row[column]] = value_counts.get(row[column], 0) + 1

            # identify the key correponding to the max value
            biggest_count = 0
            most_common = None
            for value, count in value_counts.items():
                if count > biggest_count:
                    biggest_count = count
                    most_common = value
            
            # print(f"most common value for {column}: {most_common}")
            print(f"{column}: most common value {most_common}")


def values_to_json(value):
    # convert a single value to a JSON string representation
    if value is None:
        return "null"
    if isinstance(value, bool):        # must come before int
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, str):
        escaped = (value.replace("\\", "\\\\")
                        .replace('"', '\\"')
                        .replace("\n", "\\n")
                        .replace("\r", "\\r")
                        .replace("\t", "\\t"))
        return f'"{escaped}"'
    raise TypeError(f"Cannot serialize type: {type(value).__name__}")

def to_json(obj):
    # convert a Python object to a JSON string representation
    if isinstance(obj, (list, tuple)):
        return "[" + ",".join(to_json(item) for item in obj) + "]"

    if isinstance(obj, dict):
        pairs = [f"{values_to_json(str(k))}:{to_json(v)}" for k, v in obj.items()]
        return "{" + ",".join(pairs) + "}"

    return values_to_json(obj)

def save_to_json_file(data, filename):
    # save a Python object to a JSON file
    base, ext = filename.rsplit(".", 1)
    new_filename = f"{base}_json.{ext}"   
    with open(new_filename, "w") as file:
        json_str = to_json(data)
        file.write(json_str)