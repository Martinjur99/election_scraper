# Scraper volebních výsledků 2017

Tento projekt slouží k získávání volebních výsledků z roku 2017 z webových stránek a ukládání těchto výsledků do souboru CSV pro další analýzu. Tento skript využívá knihovny pro scraping a práci s daty v Pythonu.

## Požadavky

Pro správné fungování tohoto projektu je potřeba nainstalovat závislosti uvedené v souboru `requirements.txt`. K tomu můžete využít následující příkazy:

### 1. Instalace požadovaných knihoven

Pokud máte nainstalovaný Python a pip, spusťte následující příkaz v adresáři projektu:

```bash
pip install -r requirements.txt

```

### 2. Spuštění skriptu
```bash
python main.py "URL" vysledky_obec.csv

python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7202" vysledky_uherskehradiste.csv

```

### 3. Ukázka části výstupu

```bash
Kód obce,Obec,Registrovaní voliči,Obálky,platné hlasy,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů
592013,Babice,1452,870,866,79,0,0,60,0,55,66,5,6,3,0,2,74,0,23,254,1,0,95,5,1,0,133,4
592021,Bánov,1707,1069,1063,92,2,1,75,0,117,62,10,1,11,1,2,71,1,11,293,1,0,148,6,0,0,156,2
592030,Bílovice,1473,1018,1008,98,0,0,67,1,66,80,10,5,14,0,1,90,0,28,264,0,2,147,4,3,1,92,35
592048,Bojkovice,3635,2181,2170,290,6,0,165,1,79,225,23,7,20,1,1,134,4,37,612,0,3,208,16,1,3,322,12
592064,Boršice,1788,1141,1131,103,0,0,74,1,61,136,14,3,14,0,0,95,0,33,279,2,0,199,4,1,1,108,3
592056,Boršice u Blatnice,660,407,404,49,0,0,24,0,13,59,1,3,8,0,0,25,1,9,95,0,2,73,1,1,0,39,1
592072,Břestek,657,405,402,49,0,0,36,0,19,33,6,1,10,0,0,37,0,13,128,0,2,27,4,0,0,37,0
592081,Březolupy,1359,881,877,99,3,0,64,1,68,84,7,10,9,2,1,80,0,24,189,0,2,87,22,1,1,112,11
592099,Březová,827,442,439,44,2,0,10,0,32,51,1,2,3,0,0,19,0,3,128,0,2,59,1,0,1,80,1
592102,Buchlovice,2085,1330,1320,173,4,0,107,3,57,135,20,6,15,1,1,123,0,38,358,1,3,129,5,1,1,131,8
592111,Bystřice pod Lopeníkem,663,428,423,25,0,0,20,1,71,31,6,4,4,0,0,25,0,2,105,0,2,40,1,1,1,81,3
592137,Částkov,308,197,195,9,0,0,10,0,6,17,1,4,3,0,1,10,1,1,64,0,0,26,4,0,0,38,0
592145,Dolní Němčí,2464,1473,1469,120,0,0,104,4,151,67,10,13,17,0,1,95,0,35,384,1,0,235,6,3,6,206,11
592153,Drslavice,431,308,307,23,0,0,16,0,6,18,1,2,6,0,2,15,0,8,61,0,0,87,1,0,0,54,7
592170,Hluk,3503,2187,2171,222,4,2,149,2,131,164,25,10,33,1,2,157,3,50,560,1,4,322,7,3,2,306,11
592188,Horní Němčí,681,434,434,32,0,0,31,0,30,55,2,2,3,3,1,21,1,7,105,0,1,42,10,0,2,82,4
592196,Hostějov,36,33,33,1,0,0,3,0,2,6,0,0,0,0,0,2,0,3,2,0,0,12,1,0,0,1,0
550736,Hostětín,192,137,136,15,0,0,10,0,6,7,7,0,5,0,0,10,0,2,24,0,0,36,2,0,0,12,0
592200,Hradčovice,810,570,564,37,0,0,24,0,18,17,6,3,7,0,0,27,0,20,137,0,0,149,4,0,2,59,54
592218,Huštěnovice,793,535,531,37,1,0,32,0,22,51,9,3,6,0,2,44,1,8,172,0,3,62,3,0,2,71,2




```
