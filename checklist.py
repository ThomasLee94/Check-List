

checklist = []

def create(item):
    checklist.append(item)

def read(index):
    return checklist[index]

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(1)

def print_index(element):
    index_counter = -1
    index_output = []

    for i in checklist:
        if element == i:
            index_output.append(index_counter)
        index_counter += 1
    return index_output


def test():
    # Create Test
    element_1 = "purple sox"
    create(element_1)
    if read(0) == element_1:
        print(read(0))
        print("Test Create {} SUCCESS".format(read(0)))
    else:
        print("Test Create {} FAILURE".format(element_1))

    # Update Test
    index = 0
    element_2 = "purple socks"
    update(index, element_2)
    for i in print_index(element_2):
        if checklist[i] == element_2:
            print("Update Test {} SUCCESS".format(checklist[i]))
        else:
            print("Update Test {} FAILURE".format(element_2))

    # Destroy Test
    element_3 = "Tom"
    create(element_3)
    destroy(element_3)
    for i in checklist:
        if i == element_3:
            print("Test Destroy {} FAILURE".format(element_3))
        else:
            print("Test Destroy {} SUCCESS".format(element_3))

test()
