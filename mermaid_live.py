# mermaid_live.py
import base64
import json
import zlib

def url(mermaid_code):
    """
    Génère un lien vers l'éditeur en ligne mermaid.live prérempli avec le code Mermaid fourni.

    Args:
        mermaid_code (str): Le code Mermaid du diagramme.

    Returns:
        str: L'URL du diagramme dans mermaid.live.
    """
    jGraph = {"code": mermaid_code, "mermaid": {"theme": "standard"}}
    byteStr = json.dumps(jGraph).encode('utf-8')
    deflated = _pako_deflate(byteStr)
    dEncode = _js_btoa(deflated)
    link_code = dEncode.decode('ascii')
    return 'http://mermaid.live/edit#pako:' + link_code

def _js_btoa(data):
    return base64.b64encode(data)

def _pako_deflate(data):
    compress = zlib.compressobj(9, zlib.DEFLATED, 15, 8, zlib.Z_DEFAULT_STRATEGY)
    compressed_data = compress.compress(data)
    compressed_data += compress.flush()
    return compressed_data