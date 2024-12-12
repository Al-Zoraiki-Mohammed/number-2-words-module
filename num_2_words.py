""""""
zero_to_nine = {'0': '','1':'One', '2': 'Two', '3': 'Three', '4': 'Four', '5':'five',
            '6': 'Six', '7': 'Seven', '8':'Eight', '9': 'Nine'}

ten_to_ninteen= {'10': 'Ten', '11': 'Eleven', '12': 'Tweleve', '13': 'Thirteen', '14': 'Fourteen',
                        '15': 'Fivteen', '16': 'Sixteen', '17': 'seventeen', '18': 'eighteen',
                        '19': 'Ninteen'}
                      
tens = {'2': 'Twenty', '3': 'Thirty', '4': 'Forty', '5':'fivty',
            '6': 'Sixty', '7': 'Seventy', '8':'Eighty', '9': 'Ninty'}

units = {  0: '', 1:"Thousands", 2: "Millions", 3: 'Billions'}


def read_number():
    while True:
        try:
            number = input('Type integer number: ').strip()
            if len(number) > 12:
                raise ValueError()
            break
        except ValueError:
            print(f'Invalid input. Type correct integer number  <= 12 digits:)')
               
    return number


def n_2_w(number, unit=0):
    if len(number) ==0:
        return ''
    
    elif len(number)==1:
        if number == '0':
            return ''
        return f'{zero_to_nine.get(number)} {units.get(unit)}'
    
    elif len(number)==2:
        if number == '00':
            return f'{units.get(unit)}'
        if number[0] == '0':
            return f'{zero_to_nine.get(number[1])} {units.get(unit)}'
        elif number[0] == '1':
            return f'{ten_to_ninteen.get(number)} {units.get(unit)}'
        else:
            return f'{tens.get(number[0])} {zero_to_nine.get(number[1])} {units.get(unit)}'
        
    elif number[-3] == '0':
        return f'{n_2_w(number[:-3], unit +1)} {n_2_w(number[-2:])}'
    else:
        return f' {n_2_w(number[:-3], unit + 1)} {zero_to_nine.get(number[-3])} Hundered {n_2_w(number[-2:], unit)}'


if __name__ == "__main__":
    number = read_number()

    if int(number) == 0:
        print ('Zero')
    else:
        print(n_2_w(number, unit=0))
