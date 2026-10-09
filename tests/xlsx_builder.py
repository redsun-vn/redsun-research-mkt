"""Build tiny .xlsx workbooks with the standard library for validator tests."""

import zipfile
from xml.sax.saxutils import escape


def _col(n):
    s = ""
    n += 1
    while n:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s


def build_xlsx(path, tabs):
    """tabs: {title: [[cell, ...], ...]} written as inline strings."""
    sheets_xml, rels_xml, ctypes = [], [], []
    with zipfile.ZipFile(path, "w") as z:
        for i, (title, rows) in enumerate(tabs.items(), start=1):
            body = []
            for r, row in enumerate(rows, start=1):
                cells = "".join(
                    f'<c r="{_col(c)}{r}" t="inlineStr"><is><t>{escape(str(v))}</t></is></c>'
                    for c, v in enumerate(row) if v != ""
                )
                body.append(f'<row r="{r}">{cells}</row>')
            z.writestr(f"xl/worksheets/sheet{i}.xml",
                       '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
                       f'<sheetData>{"".join(body)}</sheetData></worksheet>')
            sheets_xml.append(f'<sheet name="{escape(title)}" sheetId="{i}" r:id="rId{i}"/>')
            rels_xml.append(f'<Relationship Id="rId{i}" Type="http://schemas.openxmlformats.org/'
                            f'officeDocument/2006/relationships/worksheet" Target="worksheets/sheet{i}.xml"/>')
            ctypes.append(f'<Override PartName="/xl/worksheets/sheet{i}.xml" ContentType="application/'
                          'vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>')
        z.writestr("xl/workbook.xml",
                   '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
                   'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
                   f'<sheets>{"".join(sheets_xml)}</sheets></workbook>')
        z.writestr("xl/_rels/workbook.xml.rels",
                   '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                   f'{"".join(rels_xml)}</Relationships>')
        z.writestr("[Content_Types].xml",
                   '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
                   f'{"".join(ctypes)}</Types>')
