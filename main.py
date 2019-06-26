import gensim,math
import numpy as np
def cosine_similarity(v1,v2):
    "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/math.sqrt(sumxx*sumyy)


print("Loading GoogleNews-vectors-negative300.bin")
model=gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin',binary=True,limit=200000)
print("OK!")
my_dict = dict({})
print("Copy corpus for faster access to my_diict")
for idx, key in enumerate(model.wv.vocab):
    my_dict[key] = model.wv[key]
print("OK!")
relations=["capital-world", "currency", "city-in-state", "family","gram1-adjective-to-adverb", "gram2-opposite", "gram3-comparative","gram6-nationality-adjective"]
lastrelation=""
all_lines=[]
print("OK!")

for line in open("word-test.v1.txt","r"):
    #read files according to given relations
    line=line.rstrip()
    if line[0]==":":
        lastrelation=line[2:]
    if lastrelation in relations and line[0]!=":":
        all_lines.append(line)

score=0
total=0
for words in all_lines:
    total+=1
    similarityarray = {}
    words=words.split()
    #Vd=Vb-Va+Vc
    Vd=(np.array(model.get_vector(words[1]).tolist())-np.array(model.get_vector(words[0]).tolist()))+(np.array(model.get_vector(words[2]).tolist()))
    for wordvector in my_dict.keys():
    #find cosine similarity between one word and all other words in my_dict
        value=cosine_similarity(Vd,my_dict[wordvector])
        if value > 0.1:
            similarityarray[wordvector]=value

    sorted_d = sorted((value, key) for (key, value) in similarityarray.items())
    mostsimilarword=sorted_d.pop()
    if mostsimilarword[1]==words[0] or mostsimilarword[1]==words[1] or mostsimilarword[1]==words[2]:
        mostsimilarword=sorted_d.pop()
    if mostsimilarword[1]==words[0] or mostsimilarword[1]==words[1] or mostsimilarword[1]==words[2]:
        mostsimilarword=sorted_d.pop()
    if mostsimilarword[1]==words[0] or mostsimilarword[1]==words[1] or mostsimilarword[1]==words[2]:
        mostsimilarword=sorted_d.pop()
    if mostsimilarword[1] == words[3]:
        score+=1
    print(words,mostsimilarword[1])
    print("Accuracy:%",(score / total) * 100)

#find accuracy
print((score/len(total))*100)
