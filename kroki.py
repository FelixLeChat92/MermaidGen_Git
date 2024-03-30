# kroki.py
import base64
import requests
import zlib

def url(mermaid_code):
    """
    Génère un lien vers une image SVG du diagramme en utilisant le service kroki.io.

    Args:
        mermaid_code (str): Le code Mermaid du diagramme.

    Returns:
        str: L'URL de l'image SVG générée par kroki.io.
    """
    mermaid_compressed = zlib.compress(mermaid_code.encode('utf-8'), 9)
    mermaid_base64 = base64.urlsafe_b64encode(mermaid_compressed).decode('utf-8')
    kroki_url = f"https://kroki.io/mermaid/svg/{mermaid_base64}"
    return kroki_url

def download(url, filename):
    """
    Télécharge une image SVG à partir d'une URL et l'enregistre dans un fichier.

    Args:
        url (str): L'URL de l'image SVG à télécharger.
        filename (str): Le nom du fichier dans lequel enregistrer l'image.
    """
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as file:
            file.write(response.content)
        print(f"L'image SVG a été enregistrée sous le nom '{filename}'")
    else:
        print("Erreur lors du téléchargement de l'image SVG")

def display(url):
    """
    Affiche une image SVG dans un notebook Jupyter à partir de son URL.

    Args:
        url (str): L'URL de l'image SVG à afficher.
    """
    from IPython.display import SVG
    response = requests.get(url)
    if response.status_code == 200:
        return SVG(response.text)
    else:
        print("Erreur lors du chargement de l'image SVG")