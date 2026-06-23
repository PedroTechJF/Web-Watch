import subprocess
import yaml
import pyinstaller_versionfile
import os
import shutil
import time

def read_metadata():
    with open("metadata.yml", "r", encoding="utf-8") as f:
        meta = yaml.safe_load(f)
    return meta

def update_version(meta):
    if "version" not in meta:
        meta["version"] = "0.0.0.0"
    
    while True:
        print("Escolha o tipo de atualização: ")
        update_types = ["patch", "minor", "major"]
        for i, type in enumerate(update_types):
            print(f"{i}: {type}")
        update_type = input(">")
        match update_type:
            case "0":
                new_version = ".".join(meta["version"].split(".")[:-1] + [str(int(meta["version"].split(".")[-1]) + 1)])
                break
            case "1":
                new_version = ".".join(meta["version"].split(".")[:-2] + [str(int(meta["version"].split(".")[-2] + 1), "0")])
                break
            case "2":
                new_version = ".".join(meta["version"].split(".")[:-3] + ["0", "0", "0"])
                break
            case _:
                print("Opção inválida. Tente novamente.")
                continue

    meta["version"] = new_version

    with open("metadata.yml", "w", encoding="utf-8") as f:
        yaml.dump(meta, f)
    
    os.makedirs(f"v{meta["version"]}", exist_ok=True)
    os.makedirs(f"latest", exist_ok=True)
    time.sleep(1)
    return read_metadata()

meta = update_version(read_metadata())
version_file_path = "version_info_generated.txt"
pyinstaller_versionfile.create_versionfile(
    output_file=version_file_path,
    version=meta["version"],
    company_name=meta.get("company_name"),
    product_name=meta.get("product_name"),
    file_description=meta.get("file_description"),
    internal_name=meta.get("internal_name"),
    original_filename=meta.get("original_filename"),
    legal_copyright=meta.get("legal_copyright")
)

version = f"v{meta["version"]}"
name = f"{meta['internal_name']} v{meta['version']}"
pyinstaller_command = [
    r"c:\Users\pedro\AppData\Local\Programs\Python\Python38-32\Scripts\pyinstaller.exe",
    "--clean",
    r"--icon=..\icon.ico",
    f"--name={name}",
    "--add-data",
    r"..\web_watch.bat;.",
    "--add-data",
    r"..\web_watch - autorun.bat;.",
    "--onefile",
    "--noconfirm",
    f"--version-file=..\\{version_file_path}",
    f"--distpath={version}/dist",
    f"--workpath={version}/build",
    f"--specpath={version}",
    "web_watch.pyw"
]

print(f"Compilando a {version}...")
subprocess.run(pyinstaller_command, check=True, capture_output=False)
shutil.copy(f"./{version}/dist/{name}.exe", f"latest/{meta['internal_name']}.exe")
print("Compilado com sucesso!")