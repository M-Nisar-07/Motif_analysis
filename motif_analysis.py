import pandas as pd

import requests

def get_deq_win(s,f):
    try:
        s = int(s[1:]) - 1
        ws = f[s-7:s+8]

        wsl = len(ws)
        if  wsl < 15:

            un = ['_' for i in range(0,15-wsl)]

            if s < 7:
                ws = ''.join(un) + ws
            else:
                ws = ws + ''.join(un)

            return ws
        else:
            return ws
    except:
        return None

def get_fasta(protein):
    protein = str(protein)
    print(protein)
    if protein != "nan":
        fasta = requests.get("https://rest.uniprot.org/uniprotkb/"+str(protein)+".fasta").text
        fasta = fasta.split("\n")[1:]
        print(protein ,fasta)
        return  "".join(fasta)
    else:
        return ""

df = pd.read_excel("no fasta_op.xlsx")

df["window_sequence"] = df.apply(lambda x: get_deq_win(x["SIT"],x["fasta"]) , axis = 1)

df.to_excel("NF_DN.xlsx")
