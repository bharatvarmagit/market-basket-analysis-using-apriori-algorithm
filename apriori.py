import sys


def generate_itemsets(itemset):
    candidates_lst=dict()
    for i in range(len(itemset)):
        item1=str(itemset[i])
        l1=len(item1)-1
        for j in range(i+1,len(itemset)):
            item2=str(itemset[j])
            l2=len(item2)-1
            if item1[0:l1]==item2[0:l2]:
                supset=item1[0:l1]+item2[:l2]
                sortsupset=sorted(supset)
                sortsupset=','.join(sortsupset)
                candidates_lst.insert(len(candidates_lst),sortsupset)
    return candidates_lst
def pruning_stage(c,support):
    lst=dict()
    for item in c:
        if support < c[item]:
            lst.insert(len(lst),item)
    return sorted(lst)                             



def find_L_K(c):
    l_k= dict()
    f= open(str(sys.argv[2]),'r')
    for line in f:
        l=str(line.split())
        for i in range(len(c)):
            item =str(c[i])
            if not (item in l_k):
                l_k[item]=0
            flag = True
            
            for i in item:
                if not (item in l):
                    flag = False
                if flag:
                    l_k[item]+=1
    f.close()
    return l_k


support=sys.argv[1]/5
c1=dict()
f=open(str(sys.argv[2]),'r')
for line in f:
    for item in line.split(" "):
        if item in c1:
            c1[item]=c1[item]+1
        else:
            c1[item]=1
f.close()
l1=pruning_stage(c1,support)
L=dict()
L=generate_itemsets(l1)
print("frequent 1-pair itemset"+ l1)
k=2
while not L:
    ck ={}
    ck=find_L_K(L)
    freq_items=dict()
    freq_items=pruning_stage(ck,support)
    print 'Frequent'k'pair itemset\t',fruquent_items
    L = generate_itemsets(freq_items)
    k = k + 1