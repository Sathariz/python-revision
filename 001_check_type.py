#

# function used for testing
def f():
    pass

# converts type into a neat string of only the type name
def to_str_type(s):
    seq_type = str(type(s))[8:-2]
    return seq_type

# l = [0, 1.5, 2j, ("ab", "bc", "g"), "d", False, [], f, True]
# l = [6, [], (3.4, "s"), 2, 3, 3]
# l = ()
# l = [0, 1, 2, 3]
l = []

example_element = l

# this function handles one element at a time (only a list or a typle)
# does not support listing elements of nested lists or tuples on 2rd or lower level
def list_type(seq):
    i = 0

    # check if given sequence is empty
    if len(seq) == 0:
        return print(f"Empty {to_str_type(seq)}")
    else:
        end_result = f"{to_str_type(seq)} of:"

    # check if all elements are of the same type
    while i+1 != len(seq):
        if isinstance(seq[i], type(seq[i+1])):
            i += 1

        else:
            break
    
    else:
        return print(f"{to_str_type(seq)} of {to_str_type(seq[i])}")


    for x in seq:
        # if element of the sequence is another sequence
        if isinstance(x, list) or isinstance(x, tuple):
            end_result += f"\n  {to_str_type(x)} of:"

            # if nested sequence is empty
            if len(x) == 0:
                end_result += f"\n    - empty {to_str_type(seq)}"
                continue

            for j in x:
                end_result += f"\n    - {to_str_type(j)}"

        else:
            end_result += f"\n  {to_str_type(x)}"

    print(end_result)


# list_type(example_element)



def process_on_many_elements(x):
    if isinstance(x, list) or isinstance(x, tuple):
        pass
    else:
        lst = [x]
        print(lst)

process_on_many_elements(example_element)


# shift + alt + arrow up/down
# ctrl + /