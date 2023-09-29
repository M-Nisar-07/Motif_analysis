import pandas as pd
import requests

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


df_ref =  pd.read_excel('For motif analysis.xlsx', sheet_name = 2)
df_fasta = pd.read_excel("ALL HUMAN FASTA.xlsx")

df_1 = pd.read_excel('For motif analysis.xlsx', sheet_name = 1)
df_1 = df_1.merge(df_ref, how = 'left' , left_on = '513 common elements in "Up-down" and "Down-up":', right_on = 'mapped_genesymbol')
df_1 = df_1.merge(df_fasta, how = 'left', left_on="new_uniprot", right_on="protein_Accession_fasta")

df_no_f = df_1.loc[df_1["fasta"].isnull()]

df_no_f.to_csv("no fastaaaa.csv")

df_1 = df_1.loc[~df_1["fasta"].isnull()]

print(df_1.columns)

df_1["window_sequence"] = df_1.apply(lambda x:get_deq_win(x['SIT'], x['fasta']) , axis =1 )

df_1.drop(columns=['fasta'], inplace = True)

df_1.to_excel("MOTIF_output.xlsx")
