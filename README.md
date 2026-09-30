# In Silico Virtual Screening of Phytochemicals Against Drug-Resistant EGFR (T790M) in Molecular Oncology

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22995607.svg)](https://doi.org/10.5281/zenodo.22995607)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)

**Author:** Krishna Kumar R.   
**Target Class:** Non-Small Cell Lung Cancer (NSCLC) / Epidermal Growth Factor Receptor (EGFR) T790M Gatekeeper Mutant
**Dataset DOI:** [10.5281/zenodo.22995607](https://doi.org/10.5281/zenodo.22995607)  


### Abstract
Acquired resistance to first- and second-generation epidermal growth factor receptor (EGFR) tyrosine kinase inhibitors (TKIs) in Non-Small Cell Lung Cancer (NSCLC) is primarily driven by the clinical acquisition of the **T790M gatekeeper mutation** within the ATP-binding domain of the kinase core (PDB ID: **3W2O**). The localized substitution of small threonine with bulky methionine at residue position 790 induces steric obstruction while simultaneously restoring wild-type ATP binding affinity, thereby rendering conventional targeted TKIs therapeutically ineffective. 

To explore alternative small-molecule inhibition strategies, this study established an automated *in silico* virtual screening and computational drug discovery pipeline evaluating candidate dietary polyphenols—**Epigallocatechin Gallate (EGCG)** and **Curcumin**—against the third-generation clinical TKI benchmark **Osimertinib**. Utilizing grid-based molecular docking in AutoDock Vina, non-covalent atomic interaction mapping via the Protein-Ligand Interaction Profiler (PLIP), and pharmacokinetic profiling through SwissADME, we systematically characterized the thermodynamic binding landscapes, pocket fitting geometries, and drug-likeness parameters across all target complexes. 

Empirical AutoDock Vina scoring demonstrated that **EGCG** achieved the highest thermodynamic binding stability at **\(-8.407\text{ kcal/mol}\)**, subtly outperforming the clinical reference drug **Osimertinib** (**\(-8.383\text{ kcal/mol}\)**), while **Curcumin** exhibited strong competitive affinity at **\(-8.213\text{ kcal/mol}\)**. Atomic interaction analysis revealed that EGCG's structural binding advantage is driven by an expansive, multi-anchored hydrogen bonding network directly engaging the key **Met790** gatekeeper residue as well as critical catalytic residues **Lys745** and **Glu762**. These findings provide a compelling biophysical foundation for using natural polyphenolic architectures as lead templates in developing next-generation TKIs capable of overcoming gatekeeper resistance in mutant EGFR oncology.

## 🔬 Methodology & Computational Workflow

### 1. Tools, Frameworks & Computational Technologies

#### Computational Pipelines & Software Engines
[![PyMOL](https://img.shields.io/badge/PyMOL-3D_Visualization-00599C?logo=python&logoColor=white)](https://pymol.org/)
[![AutoDock Vina](https://img.shields.io/badge/AutoDock_Vina-v1.2+-blue?logo=molecular-biology)](https://vina.scripps.edu/)
[![CB-Dock2](https://img.shields.io/badge/CB--Dock2-Blind_Docking_Server-green)](http://cbdock2.labshare.cn/)
[![PLIP](https://img.shields.io/badge/PLIP-v2.3.0_Interaction_Profiler-orange)](https://plip-tool.biotec.tu-dresden.de/)
[![SwissADME](https://img.shields.io/badge/SwissADME-Pharmacokinetics_%26_ADME-red)](http://www.swissadme.ch/)

#### Execution Environments & Languages
[![Google Colab](https://img.shields.io/badge/Google_Colab-Cloud_GPU/CPU-F9AB00?logo=googlecolab&logoColor=white)](https://colab.research.google.com/)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Open Babel](https://img.shields.io/badge/Open_Babel-3D_Conformer_Generation-000000)](http://openbabel.org/)
[![RDKit](https://img.shields.io/badge/RDKit-Cheminformatics-306998)](https://www.rdkit.org/)

### 2. Methodological Infrastructure Breakdown

| Stage | Infrastructure / Tool Used | Purpose / Specific Task Output |
| :--- | :--- | :--- |
| **Protein Preparation** | RCSB PDB / PyMOL | Downloaded PDB ID: `3W2O`, isolated EGFR-T790M mutant chain, removed water/heteroatoms, added polar hydrogens. |
| **Ligand Optimization** | Open Babel / SwissADME | Converted 2D SMILES to 3D PDBQT format, assigned Gasteiger charges, generated low-energy conformers. |
| **Virtual Screening** | AutoDock Vina / CB-Dock2 | Performed energy minimization and cavity-blind docking centered on Met790/Cys797 (\(\text{kcal/mol}\)). |
| **Interaction Mapping** | PLIP (CLI / Web) | Extracted atomic hydrogen bonding networks, hydrophobic contacts, and exported XML/TXT reports. |
| **ADME/PK Profiling** | SwissADME Web Server | Evaluated Lipinski's Rule of 5, TPSA (\(\text{\AA}^2\)), and generated Bioavailability Radar plots. |
| **Visual Rendering** | PyMOL 3D / `.pse` Sessions | Surface electrostatic rendering, ray-traced figures (\(1920 \times 1080\)), and interactive session outputs. |
| **Repository Archiving** | GitHub & Zenodo | Public code execution tracking, version control, and DOI registration (`10.5281/zenodo.22995607`). |

### 3. Macromolecular Target & Ligand Specifications

# Macromolecular Receptor Target

| Parameter | Details |
| :--- | :--- |
| **Protein Name** | Epidermal Growth Factor Receptor (EGFR) Kinase Domain |
| **Mutation State** | T790M Gatekeeper Mutation (Threonine \(\rightarrow\) Methionine at position 790) |
| **PDB ID** | [`3W2O`](https://www.rcsb.org/structure/3W2O) (Resolution: \(1.95\,\text{\AA}\)) |
| **Biological Function** | Key oncogenic driver in Non-Small Cell Lung Cancer (NSCLC) conferring resistance to 1st/2nd generation TKIs |
| **Active Site Center** | Centered on Met790 gatekeeper residue and nucleophilic Cys797 (\(X = 20.5\), \(Y = 30.2\), \(Z = 12.8\)) |
| **Preparation Steps** | Crystallographic water molecules and co-crystallized inhibitors removed, polar hydrogens added, Gasteiger charges assigned |

# Ligand Database & Chemical Properties

| Attribute | Benchmark Control | Phytochemical Lead 1 | Phytochemical Lead 2 |
| :--- | :---: | :---: | :---: |
| **Compound** | **Osimertinib** (AZD9291) | **Epigallocatechin Gallate** (EGCG) | **Curcumin** |
| **Compound Type** | 3rd-Gen Irreversible TKI | Green Tea Polyphenol | Turmeric Rhizome Polyphenol |
| **PubChem CID** | [71496458](https://pubchem.ncbi.nlm.nih.gov/compound/71496458) | [65064](https://pubchem.ncbi.nlm.nih.gov/compound/65064) | [5088](https://pubchem.ncbi.nlm.nih.gov/compound/5088) |
| **Molecular Formula** | \(\text{C}_{28}\text{H}_{33}\text{N}_{7}\text{O}_{2}\) | \(\text{C}_{22}\text{H}_{18}\text{O}_{11}\) | \(\text{C}_{21}\text{H}_{20}\text{O}_{6}\) |
| **Molecular Weight** | \(499.61\,\text{g/mol}\) | \(458.37\,\text{g/mol}\) | \(368.38\,\text{g/mol}\) |
| **Rotatable Bonds** | $8$ | $4$ | $8$ |
| **H-Bond Donors / Acceptors** | \(2\,/\,7\) | \(8\,/\,11\) | \(2\,/\,6\) |
| **Topological Polar Surface Area (TPSA)** | \(87.82\,\text{\AA}^2\) | \(197.37\,\text{\AA}^2\) | \(93.06\,\text{\AA}^2\) |
---

### 4. Consolidated Thermodynamic & Binding Results Table

| Compound | Target | Vina Binding Energy (\(\text{kcal/mol}\)) | Key H-Bond Residues | Key Hydrophobic Contacts |
| :--- | :---: | :---: | :--- | :--- |
| **EGCG** *(Phytochemical Lead)* | EGFR-T790M | **\(-8.407\)** | Lys745, Glu762, Met790 | Leu718, Phe723 |
| **Osimertinib** *(Benchmark Control)* | EGFR-T790M | **\(-8.383\)** | Met790, Cys797 | Leu718, Val726, Ala743, Lys745 |
| **Curcumin** *(Phytochemical Lead)* | EGFR-T790M | **\(-8.213\)** | Met790 | Val726, Leu844 |

### 📊 Structural Visualization & Binding Analysis

Three-dimensional structural visualizations and molecular docking conformations were generated using **PyMOL (v2.5+)**. High-resolution ray-traced figures (\(1920 \times 1080\), \(300\text{ DPI}\)) depict the spatial orientations, binding pocket topologies, and electrostatic surfaces of the receptor-ligand complexes for **EGFR-T790M** (PDB ID: [`3W2O`](https://www.rcsb.org/structure/3W2O)).

# 1. Global Binding Pocket Overview

The catalytic domain of the drug-resistant EGFR-T790M kinase (PDB ID: 3W2O) features the critical gatekeeper substitution at residue position 790, where the substitution of threonine with bulky methionine (Met790) induces steric hindrance in the ATP-binding pocket.

Figure 1: Global cartoon representation of the EGFR-T790M catalytic kinase domain (PDB ID: 3W2O) highlighting the central ATP-binding pocket cavity, key gatekeeper residue Met790, and nucleophilic residue Cys797.
![Global Pocket](fig1_global_pocket.png)

# 2. Multi-Ligand Binding Mode Superimposition & Alignment

Superimposition of the third-generation clinical TKI Osimertinib (benchmark control) with natural polyphenolic leads Epigallocatechin Gallate (EGCG) and Curcumin reveals structural convergence within the catalytic pocket.

Figure 2: Superimposed structural alignment of Osimertinib (Control, yellow), EGCG (Phytochemical Lead, magenta), and Curcumin (Phytochemical Lead, cyan) docked into the ATP-binding hinge region of EGFR-T790M.

Key Structural Insight: EGCG extends deeper into the back-pocket region adjacent to Met790 and Glu762, accommodating its polyhydroxyl rings, whereas Osimertinib adopts an elongated conformation spanning across Cys797.
![Multi-Ligand Alignment](fig3_ligand_overlay.png)

# 3. High-Resolution Atomic Interactions & Hydrogen-Bonding Network (EGCG Lead)

Detailed interaction analysis highlights the specific non-covalent contacts anchoring EGCG within the mutant kinase active site.

Figure 3: Close-up 3D interaction map showing Epigallocatechin Gallate (EGCG) forming direct polar hydrogen bonds (red dashed lines) with Met790, Lys745, and Glu762 alongside surrounding hydrophobic pocket residues.
![EGCG Atomic Interactions](fig2_EGCG_contacts.png)

# 4. Surface Electrostatics & Pocket Topology Occupancy

Electrostatic potential surface rendering of the EGFR-T790M active site pocket illustrates cavity volume occupancy, steric fit, and hydrophobic/hydrophilic surface complementarity.

Figure 4: Electrostatic surface cavity representation of the EGFR-T790M binding pocket demonstrating spatial occupancy and steric accommodation of the polyphenolic lead molecules within the Met790 gatekeeper cavity.
![Electrostatic Surface Map](fig4_surface_pocket.png)

## 🔗 Atomic-Level Interaction Profiling (PLIP Results)

Non-covalent interaction mapping was conducted using the **Protein-Ligand Interaction Profiler (PLIP)** to characterize the specific hydrogen-bonding networks, hydrophobic contacts, and electrostatic stabilization mechanisms within the ATP-binding site of **EGFR-T790M** (PDB ID: [`3W2O`](https://www.rcsb.org/structure/3W2O)).

## 🧬 High-Resolution Interaction Profiling & Raw Reports

# 1. Benchmark Control: Osimertinib (AZD9291)

Vina Binding Affinity: −8.383 kcal/mol

Key Hydrogen Bonds: Met790, Cys797

Hydrophobic Contacts: Leu718, Val726, Ala743, Lys745

Raw Files:[`View TXT Report`](/Osimertinib_report.txt) | [`Download XML Data`](Osimertinib_plip.xml)

Structural & Biological Explanation:

Osimertinib functions as a third-generation irreversible TKI designed specifically to overcome gatekeeper T790M resistance. PLIP interaction mapping reveals dual-anchoring polar interactions across the hinge region:

Hinge Region Engagement: Forms crucial hydrogen-bonding contacts with the backbone of Met790 and the thiol-containing residue Cys797. The interaction at Cys797 positions Osimertinib in optimal spatial proximity for targeted covalent bond formation in vivo.

Hydrophobic Pocket Fitting: The lipophilic indole and pyrimidine core fragments are stabilized by non-polar alkyl/pi-alkyl contacts with Leu718, Val726, and Ala743, providing strong steric complementation inside the hydrophobic cleft.
![Osimertinib Interactions](Osimertinib_interaction.png)

# 2. Phytochemical Lead 1: Epigallocatechin Gallate (EGCG)

Vina Binding Affinity: −8.407 kcal/mol (Highest Thermodynamic Stability)

Key Hydrogen Bonds: Lys745, Glu762, Met790

Hydrophobic Contacts: Leu718, Phe723

Raw Files: [`View TXT Report`](EGCG_report.txt) | [`Download XML Data`](EGCG_plip.xml)

Structural & Biological Explanation:

Epigallocatechin Gallate (EGCG), a major green tea catechin, demonstrated the highest binding stability among all tested compounds, subtly outperforming Osimertinib. PLIP profiling reveals a multi-anchored hydrogen-bonding network:

Tripartite Catalytic Anchor: EGCG utilizes its multiple hydroxyl (−OH) functional groups on the B-ring and gallate moiety to establish simultaneous polar contacts with Met790 (gatekeeper residue), Lys745 (catalytic lysine), and Glu762 (αC-helix residue).

Salt-Bridge Disruption: By directly engaging both Lys745 and Glu762, EGCG perturbs the active-state salt bridge necessary for phosphotransfer, functionally locking the kinase domain in an inactive conformation.

Aromatic Stabilization: Hydrophobic interactions with Leu718 and Phe723 wrap around the polyphenolic chromane ring, stabilizing its spatial pose within the pocket.
![EGCG Interactions](EGCG_interaction.png)

# 3. Phytochemical Lead 2: Curcumin

Vina Binding Affinity: −8.213 kcal/mol

Key Hydrogen Bonds: Met790

Hydrophobic Contacts: Val726, Leu844

Raw Files:[`View TXT Report`](Curcumin_report.txt) | [`Download XML Data`](Curcumin_plip.xml)

Structural & Biological Explanation:

Curcumin, a natural diferuloylmethane polyphenol from Curcuma longa, demonstrates competitive thermodynamic binding to the resistant target.

Gatekeeper Targeting: Forms a direct hydrogen bond via its terminal phenolic hydroxyl group with the mutated gatekeeper residue Met790, confirming targeted entry into the steric-hindrance region.

Linear Hydrophobic Channel Fit: The flexible, conjugated heptadienone chain allows Curcumin to extend along the hydrophobic binding cleft, establishing strong non-covalent hydrophobic contacts with Val726 and Leu844.

Binding Limitation: While highly stable, Curcumin lacks the multi-dentate hydroxyl array of EGCG, resulting in fewer polar anchors and a slightly lower overall affinity score than EGCG and Osimertinib.
![Curcumin Interactions](Curcumin_interaction.png)

## 💡 Key Interaction Observations

Gatekeeper Targeting (Met790): All three test molecules successfully form target hydrogen-bonding interactions with the mutated gatekeeper residue Met790, confirming catalytic pocket localization despite steric hindrance.

Anchor Residue Engagement (EGCG): EGCG establishes additional polar contacts with catalytic site residues Lys745 and Glu762, explaining its superior thermodynamic binding affinity.

Covalency/H-Bonding Shift (Osimertinib): Osimertinib exhibits dual polar anchoring to Met790 and key hinge residue Cys797, supplemented by an extensive hydrophobic contact network across Leu718 and Val726.
