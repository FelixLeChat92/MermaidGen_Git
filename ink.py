# ink.py
import base64
import requests

def _mermaid_ink_string(graph):
    graphbytes = graph.encode("utf-8")
    base64_bytes = base64.b64encode(graphbytes)
    base64_string = base64_bytes.decode("utf-8")
    return base64_string

def url_svg(mermaid_code):
    """
    Génère un lien vers une image SVG du diagramme en utilisant le service mermaid.ink.

    Args:
        mermaid_code (str): Le code Mermaid du diagramme.

    Returns:
        str: L'URL de l'image SVG générée par mermaid.ink.
    """
    string = _mermaid_ink_string(mermaid_code)
    return "https://mermaid.ink/svg/" + string

def url_png(mermaid_code):
    """
    Génère un lien vers une image PNG du diagramme en utilisant le service mermaid.ink.

    Args:
        mermaid_code (str): Le code Mermaid du diagramme.

    Returns:
        str: L'URL de l'image PNG générée par mermaid.ink.
    """
    string = _mermaid_ink_string(mermaid_code)  
    return "https://mermaid.ink/img/" + string

def download_svg(url, filename):
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

def download_png(url, filename):
    """
    Télécharge une image PNG à partir d'une URL et l'enregistre dans un fichier.

    Args:
        url (str): L'URL de l'image PNG à télécharger.  
        filename (str): Le nom du fichier dans lequel enregistrer l'image.
    """
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as file:
            file.write(response.content)
        print(f"L'image PNG a été enregistrée sous le nom '{filename}'")
    else:
        print("Erreur lors du téléchargement de l'image PNG")

def display_svg(mermaid_code):
    """
    Génère une image SVG avec mermaid.ink et l'affiche dans un notebook Jupyter.

    Args:
        mermaid_code (str): Le code Mermaid du diagramme.
    """
    from IPython.display import SVG
    url = url_svg(mermaid_code)
    response = requests.get(url)
    if response.status_code == 200:
        return SVG(response.text)
    else:
        print("Erreur lors du chargement de l'image SVG")

def display_png(mermaid_code):
    """
    Génère une image PNG avec mermaid.ink et l'affiche dans un notebook Jupyter.

    Args:
        mermaid_code (str): Le code Mermaid du diagramme.
    """
    from IPython.display import Image
    url = url_png(mermaid_code)
    response = requests.get(url)
    if response.status_code == 200:
        return Image(url)
    else:
        print("Erreur lors du chargement de l'image PNG")