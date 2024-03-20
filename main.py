#!/usr/bin/env python3
import zipfile
import datetime
import numpy as np
#import database.connect as con
import scrapping.scraperCVM as scraper
import os
from zipfile import ZipFile

def status_carteira(): #Esta função retorna o status da carteira,
    for i in range(len(ativos_carteira)):
        tickers.append(yf.Ticker(ativos_carteira[i][0]))
        print(id(tickers[i]))
    return 0

def aporte(): #Aqui implementarei a logica do aporte mensal
    return 0

def main():
    dfps = scraper.scraperCVM()
    #dataframe = dfps.prepareDFP()
    #dfcias = dfps.getCias()
    dfps.downloadDFPZIP()
    #print(dfcias.to_dict("records"))
    #print(dataframe[0].columns)

    #print(dataframe[0]["DENOM_CIA"].unique().size)
    return 0

if __name__ == '__main__':
    main()
