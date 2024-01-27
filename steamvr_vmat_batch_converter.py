import os


def create_vmat_files(directory, relative_path_prefix, lighting_choice):
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tga', '.bmp')):
                relative_path = os.path.join(relative_path_prefix, filename).replace('\\', '/')

                if lighting_choice == "1":
                    light_code = lit.replace("{relative_path}", relative_path)
                else:
                    light_code = unlit.replace("{relative_path}", relative_path)

                vmat_content = light_code
                vmat_filename = os.path.splitext(filename)[0] + '.vmat'
                vmat_file_path = os.path.join(root, vmat_filename)

                with open(vmat_file_path, 'w') as vmat_file:
                    vmat_file.write(vmat_content)


# Global templates with placeholder for relative_path
lit = """Layer0
{{
    shader "vr_standard.vfx"

    //---- Color ----
    g_vColorTint "[1.000000 1.000000 1.000000 0.000000]"
    g_vTexCoordOffset "[0.000 0.000]"
    g_vTexCoordScale "[1.000 1.000]"
    g_vTexCoordScrollSpeed "[0.000 0.000]"
    TextureColor "{relative_path}"

    //---- Lighting ----
    g_flDirectionalLightmapMinZ "0.050"
    g_flDirectionalLightmapStrength "1.000"
    TextureGlossiness "materials/default/default_gloss.tga"

    //---- Normal Map ----
    TextureNormal "materials/default/default_normal.tga"
}}
"""

unlit = """Layer0
{{
    shader "vr_standard.vfx"

    //---- Lighting ----
    F_UNLIT 1

    //---- Color ----
    g_vColorTint "[1.000000 1.000000 1.000000 0.000000]"
    g_vTexCoordOffset "[0.000 0.000]"
    g_vTexCoordScale "[1.000 1.000]"
    g_vTexCoordScrollSpeed "[0.000 0.000]"
    TextureColor "{relative_path}"
}}
"""

# Get inputs from user
relative_path_prefix = input(r"Please input the relative path prefix (e.g., 'models\textures'): ")
lighting_choice = input(
    "Please type 1 if you want to generate normal .vmats, type 2 if you wish to generate unlit .vmats.")

# Run the function
create_vmat_files(os.getcwd(), relative_path_prefix, lighting_choice)
