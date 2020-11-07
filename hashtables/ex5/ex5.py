# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # dict with filename as the key and a list of full paths as the value
    files_dict = {}
    result = []
    for path in files:
        file_name = path.split('/')[-1]
        if file_name in files_dict:
            files_dict[file_name] += [path]
        else:
            files_dict[file_name] = [path]

    for query in queries:
        if query in files_dict:
            result += files_dict[query]

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
