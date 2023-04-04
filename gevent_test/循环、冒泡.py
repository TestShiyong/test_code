# for i in range(1,10):
#     for a in range(1,10):
#         if a<=i:
#             print(a,'*',i,'=',i*a,end='\t')
#     print()
#
#
# i1=1
# while i1<=9:
#     b=1
#     while b<=i1:
#         print(b,'*',i1,'=',i1*b,end='\t')
#         b+=1
#     print()
#     i1+=1
#
#
#
# list=[9,8,7,6,5,4,3,2,1]
#
# for i2  in  range(len(list)):
#     for i3 in  range(i2+1,len(list)):
#         if list[i2]>list[i3]:
#             cun=list[i2]
#             list[i2]=list[i3]
#             list[i3]=cun
#     print(list)
#
# print('*'*40)
# list2=[9,8,7,6,5,4,3,2,1]
# cc=0
# while cc<len(list2):
#     dd=cc+1
#     while dd<len(list2):
#         if list2[cc]>list2[dd]:
#             cun2=list2[cc]
#             list2[cc]=list2[dd]
#             list2[dd]=cun2
#         dd+=1
#     print(list2)
#     cc+=1

# for i in  range(1,10):
#     for j in  range(1,10):
#         if j<=i:
#             print(j,'*',i,'=',i*j,end='\t')
#     print()
#

# a=1
# while  a<=9:
#     b=1
#     while b<=a:
#         print(b,'*',a,'=',b*a,end='\t')
#         b+=1
#     print()
#     a+=1


#
# for  i in  range(len(list)):
#     a=i+1
#     for b in  range(a,len(list)):
#         if list[i]>list[b]:
#             c=list[i]
#             list[i]=list[b]
#             list[b]=c
#     print(list)

# i=0
# while i< len(list):
#     b=i+1
#     while b<len(list):
#         if  list[i] > list[b]:
#             c = list[i]
#             list[i] = list[b]
#             list[b] = c
#         b+=1
#     print(list)
#     i+=1















list=[1,9,3,8,28,3,6,19,4,3,1,0]

i=0
while i<len(list):
    j=i+1
    while j<len(list):
        if list[i] == list[j]:
            del list[j]
        else:
            if list[i]>list[j]:
                b=list[i]
                list[i]=list[j]
                list[j]=b
            j+=1
    print(list)
    i+=1



# def  dd(a,b):
#     c=a+b
#     print(c)
#
# dd(5,9)