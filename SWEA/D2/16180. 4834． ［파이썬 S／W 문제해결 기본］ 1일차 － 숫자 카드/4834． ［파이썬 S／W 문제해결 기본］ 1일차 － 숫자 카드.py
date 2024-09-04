T = int(input())
for tc in range(1, T+1):
    n = int(input())
    number = map(str, input())
    number_dict = {'9':0, '8':0, '7':0, '6':0, '5':0, '4':0, '3':0, '2':0, '1':0,'0':0}
     
    for i in number:
        number_dict[i] += 1
 
    max_card = number_dict['9']
    result_key = '9'
 
    for key, value in number_dict.items():
        if max_card < value:
            max_card = value 
            result_key = key
 
    print(f'#{tc} {result_key} {max_card}')
