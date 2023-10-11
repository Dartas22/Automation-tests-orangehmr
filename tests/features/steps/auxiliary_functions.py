def remove_spaces(text):
    remove = list()
    for i in range(len(text)):
        if text[i] == ' ':
            remove.append(i)

    for num in remove[::-1]:
        text = text[:num] + text[num+1:]

    return text

def return_result_number(text):
    number = str()
    for i in text:
        if i.isnumeric():
            number += i
    
    return int(number)

def convert_british_time_format(time):
    if time[1] == ':':
        hour = int(time[0])
        minuets = int(time[2:4])
    else:
        hour = int(time[:2])
        minuets = int(time[3:5])

    if time[-2] == 'P':
        hour += 12

    return [hour, minuets]

def shift_length(start, finish):
    start, finish = convert_british_time_format(start), convert_british_time_format(finish)
    hours = finish[0] - start[0]
    minuets = finish[1] - start[1]
    if minuets < 0:
        hours -= 1
        minuets = 60 + minuets

    if hours < 0:
        hours += 24

    ret = str(hours + round(minuets/60, 2))
    if ret[-2] == '.':
        ret = ret + '0'

    return ret
