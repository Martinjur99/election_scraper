"""
election.py: Engeto projekt

autor: Martin Ondrůšek
email: ondrusek.martin89@gmail.com
"""

import sys
import csv
import requests
from bs4 import BeautifulSoup

def main():
    #Hlavní funkce, která spouští program.
    base_url = "https://www.volby.cz/pls/ps2017nss/"
    validate_arguments(base_url)
    election_url = sys.argv[1]
    output_filename = sys.argv[2]
    main_page_soup = fetch_html(election_url)
    election_data, header_row = scrape_municipality_data(main_page_soup, base_url)
    print(f"Ukladám data z: {output_filename}")
    save_to_csv(election_data, header_row, output_filename)
    print("Došlo k úspěšnému nahrání dat...")

def validate_arguments(base_url):
    #Kontroluje správnost argumentů z příkazové řádky.
    if len(sys.argv) != 3:
        print("Nesprávné zadání agrumentů!")
        exit()
    elif base_url not in sys.argv[1]:
        print("Byla zadána nesprávná URL adresa!")
        exit()
    elif ".csv" not in sys.argv[2]:
        print("Byla zvolena nesprávná přípona souboru!")
        exit()
    else:
        print(f"Stahuji data ze zvolené URL: {sys.argv[1]}")

def fetch_html(url):
    #Stáhne HTML stránku a vrátí její obsah jako BeautifulSoup objekt.
    response = requests.get(url)
    return BeautifulSoup(response.text, "html.parser")

def scrape_municipality_data(main_page_soup, base_url):
    #Získá odkazy na jednotlivé obce a zpracuje výsledky voleb.
    all_results = []
    header_row = []
    municipality_index = 0
    municipality_names = main_page_soup.find_all('td', {'class': 'overflow_name'})
    for municipality_code_td in main_page_soup.find_all('td', {'class': 'cislo'}):
        result_line = [municipality_code_td.text]
        for name in municipality_names[municipality_index]:
            result_line.append(name.text)
        
        detail_link = municipality_code_td.a['href']
        municipality_soup = fetch_html(base_url + detail_link)

        if municipality_index == 0:
            header_row = build_header(municipality_soup)
        
        result_line.extend(parse_municipality_data(municipality_soup))
        all_results.append(result_line)
        
        municipality_index += 1

    return all_results, header_row

def parse_municipality_data(municipality_soup):
    #Zpracuje data o voličích a výsledcích voleb z jedné obce.
    results = []

    registered_voters = municipality_soup.find('td', {'headers': 'sa2'}).text
    results.append(clean_number(registered_voters))

    envelopes_issued = municipality_soup.find('td', {'headers': 'sa5'}).text
    results.append(clean_number(envelopes_issued))

    valid_votes = municipality_soup.find('td', {'headers': 'sa6'}).text
    results.append(clean_number(valid_votes))

    results.extend(parse_votes(municipality_soup))

    return results

def build_header(municipality_soup):
    #Vytvoří hlavičku CSV souboru.
    header = ["Kód obce", "Obec", "Registrovaní voliči", "Obálky", "platné hlasy"]
    for party_td in municipality_soup.find_all('td', {'class': 'overflow_name'}):
        header.append(party_td.text)
    return header

def parse_votes(municipality_soup):
    #Získá počty hlasů jednotlivých stran v dané obci.
    votes_list = []
    table_index = 1
    total_tables = len(municipality_soup.find_all('table'))

    while table_index < total_tables:
        votes = municipality_soup.find_all('td', {'headers': f't{table_index}sa2 t{table_index}sb3'})
        for vote_td in votes:
            votes_list.append(clean_number(vote_td.text))
        table_index += 1

    return votes_list

def clean_number(number_string):
    #Odstraní nepotřebné mezery nebo speciální znaky z čísel.
    return ''.join(number_string.split()) if "\xa0" in number_string else number_string

def save_to_csv(data_rows: list, header_row: list, filename: str):
    #Uloží výsledky do CSV souboru v kódování UTF-8 (s BOM pro kompatibilitu s Excelem).
    with open(filename, "w", encoding="utf-8-sig", newline="") as csvfile:
        writer = csv.writer(csvfile, dialect="excel")
        writer.writerow(header_row)
        writer.writerows(data_rows)

if __name__ == "__main__":
    main()
