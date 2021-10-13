#DNA
#Katie King

DNA = "GTGACCCTGGCCAGGACTGACCTGGAGATGCAGATCGAAGGCCTGAAGGAGGAGCTGGCC"

print("The total of nitrogen bases are ",len(DNA),".")

cb = DNA.count("C")
print("The total of cytosine bases are",cb,".")

tb = DNA.count("T")
print("The total of thymine bases are",tb,".")

ab = DNA.count("A")
print("The total of adenine bases are",ab,".")

gb = DNA.count("G")
print("The total of guanine bases are",gb,".")

er = DNA.find("GAATTC") +1
print("The EcoRI is postioned at ",er,".")

RNA = []

for i in range(len(DNA)):
    if DNA[i] == ("A"):
        RNA.append("U")
    elif DNA[i] == ("G"):
        RNA.append("C")
    elif DNA[i] == ("C"):
        RNA.append("G")
    elif DNA[i] == ("T"):
        RNA.append("A")

for i in range (len(RNA)):
    print(RNA[i], end="")

