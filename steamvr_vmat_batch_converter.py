import os

def create_vmat_files(directory, relative_path_prefix):
    # Scan for images.
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tga', '.bmp')):
                # Get the correct path to use in the image source thing.
                relative_path = os.path.join(relative_path_prefix, filename)
                # Create the .vmat content
                vmat_content = f"""Layer0
{{
    shader "vr_standard.vfx"

    //---- Color ----
    g_vColorTint "[1.000000 1.000000 1.000000 0.000000]"
    g_vTexCoordOffset "[0.000 0.000]"
    g_vTexCoordScale "[1.000 1.000]"
    g_vTexCoordScrollSpeed "[0.000 0.000]"
    TextureColor "{relative_path.replace('\\\\', '/')}"

    //---- Lighting ----
    g_flDirectionalLightmapMinZ "0.050"
    g_flDirectionalLightmapStrength "1.000"
    TextureGlossiness "materials/default/default_gloss.tga"

    //---- Normal Map ----
    TextureNormal "materials/default/default_normal.tga"
}}
"""
                # Write the .vmat file
                vmat_filename = os.path.splitext(filename)[0] + '.vmat'
                #Splits the img file into name and extension, uses the name.
                vmat_file_path = os.path.join(root, vmat_filename)
                with open(vmat_file_path, 'w') as vmat_file:
                    vmat_file.write(vmat_content)

# This asks the user for the correct path. Relative to the location of the addons folder,
# The addons folder itself is not included in this.
relative_path_prefix = input("Please input the relative path prefix (e.g., 'materials/test'): ")

# Run the function for the specific directory where the script is located.
create_vmat_files(os.getcwd(), relative_path_prefix)

# https://www.youtube.com/watch?v=tso8iUBeuXM literaly me