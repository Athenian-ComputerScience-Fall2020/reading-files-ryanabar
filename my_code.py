# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  

def avg_temp():
    with open('temps.txt') as file_object:
        line_list = file_object.readlines()

    list_length = len(line_list)
    for i in range(list_length):
        line_list[i] = line_list[i].rstrip()

    total = 0
    for i in range (1, list_length):
        total = total + int(line_list[i])
    average = total / (list_length - 1)

    return average


if __name__ == '__main__':
    print (avg_temp())



