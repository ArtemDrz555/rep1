f=open('Perepis.txt','r')
sum=0
ot=int(input('введите от -'))
do=int(input('введите до -'))



for i in f:

    l=i.split()
    god=l[3]

    god4=int(god[6:])
    if god4<=1978:
        sum+=1
        name=l[0]
    print(name)


    if god4>=ot and god4<=do:
       fam=l[1]
       o4=l[2]
       print(name, fam, o4, god)

print(sum)



f.close()