print('calcultor')
opretion = int(input('first number:'))
opretion2 = int(input('second number:'))
opretion3 = input('opreation:')
multi,dvivson,minux,power,floor,plus= '*','/','-','**', '//','+'
if opretion3 == multi:
    print(opretion*opretion2)
elif opretion3==dvivson:
    print(opretion//opretion2)
elif opretion3==minux:
     print(opretion-opretion2)
elif opretion3==power:
    print(opretion**opretion2)
elif opretion3==floor:
    print(opretion//opretion2)
elif opretion3==plus:
    print(opretion+opretion2)

else:
    print('your input is wrong')

print('task completed')
