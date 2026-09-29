import os
import pymol

def render_pse_to_png(pymol_dir, images_dir):
    os.makedirs(images_dir, exist_ok=True)
    
    sessions = {
        "fig1_global_pocket.pse": "fig1_global_pocket.png",
        "fig2_EGCG_contacts.pse": "fig2_EGCG_contacts.png",
        "fig3_ligand_overlay.pse": "fig3_ligand_overlay.png",
        "fig4_surface_pocket.pse": "fig4_surface_pocket.png"
    }

    pymol.finish_launching(['pymol', '-qc'])

    for pse_file, png_file in sessions.items():
        pse_path = os.path.join(pymol_dir, pse_file)
        png_path = os.path.join(images_dir, png_file)

        if os.path.exists(pse_path):
            print(f"Loading {pse_file}...")
            pymol.cmd.reinitialize()
            pymol.cmd.load(pse_path)
            pymol.cmd.ray(1920, 1080)
            pymol.cmd.png(png_path)
            print(f"Saved: {png_path}")
        else:
            print(f"Skipped {pse_file} (not found).")

if __name__ == "__main__":
    BASE_DIR = os.getcwd()
    PSE_DIR = os.path.join(BASE_DIR, "pymol_sessions")
    IMG_DIR = os.path.join(BASE_DIR, "images")
    render_pse_to_png(PSE_DIR, IMG_DIR)
