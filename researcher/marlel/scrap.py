import requests
import xml.etree.ElementTree as ET
import re
import bibtexparser
import json


pids = {"Odalric-Ambrym Maillard": "83/7401",
        "Audrey Durand": "70/9804",
        "Ronald Ortner": "22/2525",
        "Mohammad Sadegh Talebi": "32/1105",
        "Aditya Gopalan": "90/9826",
        "Anders Jonsson": "05/3488",
        "Shubhada Agrawal": "247/9653"}


def safe(s):
    # keep letters, numbers, hyphen and underscore; replace other chars with underscore
    return re.sub(r'[^0-9A-Za-z\-_]', '_', s)


def retrieve_bibtex(pid):
    # 1) fetch XML and get name attribute
    url_xml = f"https://dblp.org/pid/{pid}.xml"
    r = requests.get(url_xml)
    if r.status_code != 200:
        raise SystemExit(f"Failed to fetch XML for {pid}: HTTP {r.status_code}")

    root = ET.fromstring(r.text)
    name_attr = root.attrib.get("name")
    if not name_attr:
        raise SystemExit("No 'name' attribute found in dblpperson element")

    # 2) split into first and last (best-effort)
    parts = name_attr.strip().split()
    if len(parts) == 0:
        basename = "unknown_author"
    elif len(parts) == 1:
        basename = safe(parts[0])
    else:
        first = safe(parts[0])
        last = safe(parts[-1])
        basename = f"{first}_{last}"

    # 3) fetch bib and save with new filename
    url_bib = f"https://dblp.org/pid/{pid}.bib"
    r2 = requests.get(url_bib)
    if r2.status_code != 200:
        raise SystemExit(f"Failed to fetch BibTeX for {pid}: HTTP {r2.status_code}")

    filename = f"{basename}.bib"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(r2.text)

    print(f"Saved BibTeX to {filename}")
    return filename



import shutil

# Paths to input files
#file_paths = ['file1.txt', 'file2.txt']

def merge(file_paths,outputfile="biblio.bib"):
    # Merge into a single file
    with open(outputfile, 'wb') as output_file:
        for file_path in file_paths:
            with open(file_path, 'rb') as input_file:
                shutil.copyfileobj(input_file, output_file)



def bib2json(bibtex):
    bib_file = bibtex+".bib"
    # Output JSON file
    json_file = bibtex+".json"

    with open(bib_file, encoding='utf-8') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    # bib_database.entries is a list of dicts
    # Optional: clean up braces in titles/authors
    for entry in bib_database.entries:
        if "title" in entry:
            entry["title"] = entry["title"].replace("{", "").replace("}", "")
        if "author" in entry:
            entry["author"] = entry["author"].replace("{", "").replace("}", "")

    with open(json_file, "w", encoding='utf-8') as f:
        json.dump(bib_database.entries, f, indent=2)

    print(f"Converted {bib_file} → {json_file} successfully.")




##

bibfiles=[]
for pid in pids:
    bibfiles.append(retrieve_bibtex(pids[pid]))
merge(bibfiles,outputfile="biblio.bib")
bib2json("biblio")

