def func(file):
    with open(file)as f:
        ave=.0
        sum=0
        nbr=0
        for line in f:
            nbr+=1
            if ',' in line:
                line=line.replace(',','')
                try:
                    sum+=float(line)
                except:
                    nbr-=1
                    break
            else:
                try:
                    sum+=float(line)
                except:
                    nbr-=1
                    break
    ave=sum/nbr
    print('{0:.2f}'.format(ave))
    with open(file,'a') as f:
        f.write('\nThe average is:{0:.2f}'.format(ave))
func('myfile.txt')
