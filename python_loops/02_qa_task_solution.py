domain = input('Domain daxil edin: ')
count = 2
iterator = 0
summary_result =0
while iterator < count:
    link = input('Test edilen sehifeni daxil edin: ')
    result = int(input('Eger sehife ugurlu test edildise 1 eks halda 0 daxil edin: 1/0: '))
    summary_result += result
    iterator += 1

print(count, ' sayda sehife test edildi, onlardan ', summary_result, ' qederi ugurlu, ', count -summary_result, ' qederi uguzsuz test edildi!')