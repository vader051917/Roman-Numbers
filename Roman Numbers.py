def find_pos(ls, number):
    """Fetch the next smallest element  and next largest element from a list of numbers
    corresponding to roman numerals

    Args:
        ls (list): The list of numbers corresponding to roman alphabets
        number (int): Given Number
    """
    new_ls = ls.copy() #Get a copy so that original list is not modified
    new_ls.append(number) 
    new_ls = sorted(new_ls) #Sort the list
    least_index = new_ls.index(number) - 1 
    max_index = new_ls.index(number)
    
    if number in ls:
        least_val = number
        max_val = None

    elif number > 1000: 
        least_val = ls[least_index]
        max_val = None

    else:
        least_val = ls[least_index]
        max_val = ls[max_index]

    return least_val, max_val

def roman_numbers(number):

    dict_val = {1:'I',
                5:'V',
                10:'X',
                50:'L',
                100:'C',
                500:'D',
                1000:'M'}

    ls = [*dict_val]
    roman = ''
    remainder = number

    while True:
        
        if remainder == 0:
            break
        
        least_val, max_val = find_pos(ls, number)

        remainder = number %least_val
        multiple = int(number/least_val) 
        
        if number in ls and remainder == 0:
            tmp_char = dict_val[number]
            roman = roman + tmp_char
            break
        
        elif '1' in str(least_val): #If the number lies between 1s category
            
            if multiple <= 3:
                
                tmp_char = dict_val[least_val]*multiple
                roman = roman + tmp_char
            
            else:
                tmp_char = dict_val[least_val]
                roman = roman + tmp_char
                tmp_char = dict_val[max_val]
                roman = roman + tmp_char  
                
            number = remainder
                
        else: #If the number lies between 5s category
            threshold = max_val - (max_val/10)
            
            if number >= threshold:
                roman = roman + dict_val[(max_val/10)]
                roman = roman + dict_val[max_val]
                number = number - threshold
                
            else:
                tmp_char = dict_val[least_val]*multiple
                roman = roman + tmp_char
                number = remainder
            
    return roman

if __name__ == "__main__":

    try:
        number = int(input('Enter a number:'))

    except Exception:
        print('Enter a valid number')
    
    if number > 0 and number <= 3999:
        roman_number = roman_numbers(number)
        print('Roman number for {} is {}'.format(number,roman_number))

    elif number > 3999 and number <= 3999999:
        
        rmndr = number%5000
        if rmndr <= 3999:
            multiple = int((number - rmndr)/1000)

        else:
            multiple = int(number/1000)
            rmndr = number%1000

        roman_number_mltpl = roman_numbers(multiple)
        roman_number_mltpl = ''.join([u'{}\u0305'.format(i) for i in roman_number_mltpl])
        if rmndr != 0:
            roman_number_rmndr = roman_numbers(rmndr)
        else:
            roman_number_rmndr = ''

        roman_number = roman_number_mltpl + roman_number_rmndr
        print('Roman number for {} is {}'.format(number,roman_number))

    else:
        print('Enter a valid number from 1 to 3,999,999')