#!/usr/bin/env python3
import os
import pandas as pd
import zipfile
import requests
class scraperCVM:

    def getCias(self):
        r = requests.get("https://dados.cvm.gov.br/dados/CIA_ABERTA/CAD/DADOS/cad_cia_aberta.csv")
        df = pd.read_csv(r.text,sep=";",encoding='ISO-8859-1',dtype={"ORDEM_EXERC":"category"})
        return df

    def getDFP(self):
        df = pd.DataFrame(lines[1:],columns=lines[0])
        return df

    def clearDFP(self):
        os.remove()
        return 0

    def downloadDFPZIP(self):
        cvm_dfp_url = 'http://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/'
        for ano in range(2010,2023):
            r = requests.get(cvm_dfp_url+f'dfp_cia_aberta_{ano}.zip')
            open(f"./dfps/dfp_cia_aberta_{ano}.zip","wb").write(r.content)
        return 0

    def prepareDFP(self):
        dfps=[]
        for file in os.listdir('./dfps'):
            uncompressed_data = zipfile.ZipFile(f'./dfps/{file}','r')
            for spread in uncompressed_data.namelist():
                df = pd.read_csv(uncompressed_data.open(spread),sep=";",encoding='ISO-8859-1',dtype={"ORDEM_EXERC":"category"})
                dfps.append(df)
        return dfps
