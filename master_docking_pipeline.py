import os
import xml.etree.ElementTree as ET
import pandas as pd

def parse_plip_xml(xml_path):
    if not os.path.exists(xml_path):
        return []
    
    tree = ET.parse(xml_path)
    root = tree.getroot()
    interactions = []

    # Parse Hydrogen Bonds
    for hb in root.findall(".//hydrogen_bond"):
        interactions.append({
            "Type": "Hydrogen Bond",
            "Residue": f"{hb.findtext('restype')}{hb.findtext('resnr')}",
            "Distance_A": hb.findtext('dist_d-a') or hb.findtext('dist_h-a'),
            "Ligand_Atom": hb.findtext('ligatom')
        })

    # Parse Hydrophobic Contacts
    for hp in root.findall(".//hydrophobic_interaction"):
        interactions.append({
            "Type": "Hydrophobic Contact",
            "Residue": f"{hp.findtext('restype')}{hp.findtext('resnr')}",
            "Distance_A": hp.findtext('dist'),
            "Ligand_Atom": hp.findtext('ligatom')
        })

    return interactions

def generate_consolidated_report(plip_dir, output_csv):
    compounds = {
        "Osimertinib": "Osimertinib_plip.xml",
        "EGCG": "EGCG_plip.xml",
        "Curcumin": "Curcumin_plip.xml"
    }

    all_data = []
    for compound, xml_file in compounds.items():
        xml_path = os.path.join(plip_dir, xml_file)
        data = parse_plip_xml(xml_path)
        for row in data:
            row["Compound"] = compound
            all_data.append(row)

    if all_data:
        df = pd.DataFrame(all_data)
        df = df[["Compound", "Type", "Residue", "Distance_A", "Ligand_Atom"]]
        df.to_csv(output_csv, index=False)
        print(f"Consolidated PLIP report saved to: {output_csv}")
    else:
        print("No XML data found to parse.")

if __name__ == "__main__":
    BASE_DIR = os.getcwd()
    PLIP_DIR = os.path.join(BASE_DIR, "plip_reports")
    OUT_CSV = os.path.join(BASE_DIR, "plip_interaction_summary.csv")
    generate_consolidated_report(PLIP_DIR, OUT_CSV)
