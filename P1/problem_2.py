import os

def main():
    arr1 = find_files(".c", "/Users/contiq/Desktop/Udacity/P1/testdir")
    print(len(arr1))
    # Output should be 4, as there are 4 files that end with .c
    arr2 = find_files(".h", "/Users/contiq/Desktop/Udacity/P1/testdir")
    print(len(arr2))
    # Output should be 4, as there are 4 files that end with .h
    arr3 = find_files("z", "/Users/contiq/Desktop/Udacity/P1/testdir")
    print(len(arr3))
    # Output should be 0, as there are 0 files that end with z
    arr_none = find_files("", "/Users/contiq/Desktop/Udacity/P1/testdir")
    print(len(arr_none))
    # Output should be 0, as there is no input for suffix
    arr_no_path = find_files(".h", "")
    # Output should be 0, as there is no input for path


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if suffix is None or path is None:
        return []
    list = []
    return find_files_recurse(list,suffix, path)

def find_files_recurse(list, suffix, path):
    if (os.path.isdir(path)):
        elements = os.listdir(path)
        for element in elements:
            new_path = os.path.join(path, element)
            find_files_recurse(list, suffix, new_path)
    elif (os.path.isfile(path)):
        if (path.endswith(suffix)):
            list.append(path)
    return list


if __name__ == '__main__':
    main()
