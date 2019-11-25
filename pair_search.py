###This script contains the function pair_search that require input of a protein 
###and returns all its interacting partners


    
#print(l[0][0])

def pair_search1(p1):

    f = open("./human_interactome.txt","r")
    rang = 13189 #number of rows
    trang = 40 #testing range
    f.readline() #to skip the first row (which are titles)
    l = [] #list of pairs
    r=[]
    for i in range(rang):
        lines = f.readline(10000) 
        split_colume = lines.split("\t") #\t for tab 
        y = split_colume[5]
        x = split_colume[4]
        y = y[:-1]
        pair = [x,y]
        l.append(pair) #add new pair to l
    #print(pair)

    for j in range(rang):
        for k in range(2):
            if p1 == l[j-1][k-1]:
                inpair = l[j-1]
                #print(inpair)
                inpair.remove(p1)
                r.append(inpair)
				
    return r
	
def pair_search(p1):

    f = open("./human_interactome.txt","r");
    f.readline() #to skip the first row (which are titles)
    r=[]
    for line in f:
        split_column = line.split("\t"); #\t for tab 
        y = split_column[5];
        x = split_column[4];
        y = y[:-1];
        if(p1==y):
            r.append(x);
        elif(p1==x):
            r.append(y);
        else:
            continue;	
    f.close();
    return r
	
def pairs_search(p,d):
	#prev.append(p["name"]);
	if(d!=0):
		tmp = pair_search(p["name"]);
		for x in tmp:
			child = {
				"name":x,
				"children":[]
			}
			p["children"].append(child);
		for x in p["children"]:
			pairs_search(x,d-1);
	
		
	return p;
	
result = {
	"name":'Q13685',
	"children":[]
}
#prev=[];
a=pairs_search(result,2);
#a=pair_search("Q13685");
#b=pair_search1("Q13685");


print(a);
#print(b);
                

