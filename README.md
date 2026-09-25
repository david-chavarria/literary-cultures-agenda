# La agenda de *Literary Cultures of Latin America*
### The working agenda of *Literary Cultures of Latin America* — a data-driven reading

> Lectura estadística y bilingüe de la agenda historiográfica de la historia comparada dirigida por **Mario J. Valdés y Djelal Kadir** (Oxford University Press, 2004, 3 vols.).
> A bilingual, statistical reading of the historiographic agenda of the comparative history edited by **Mario J. Valdés and Djelal Kadir** (Oxford University Press, 2004, 3 vols.).

🔗 **Reporte interactivo / Interactive report:** `https://david-chavarria.github.io/literary-cultures-agenda/`
*(se activa al habilitar GitHub Pages — ver más abajo / becomes live once GitHub Pages is enabled — see below)*

---

## 🇪🇸 Español

### Qué es esto
Una base de datos y un reporte analítico construidos a partir del **índice** de la obra. No reproduce el texto de los capítulos: sistematiza sus **metadatos** (volumen, parte, sección, capítulo, título, autoría, página) y les añade **etiquetas analíticas derivadas** para permitir un análisis cuantitativo de la "agenda de trabajo" del proyecto: qué se eligió estudiar, sobre qué regiones, con qué temas, en qué periodos y desde qué disciplinas.

Fue elaborado como **insumo docente** para un seminario de doctorado en *Historiografía de la literatura*.

### Contenido del repositorio
```
literary-cultures-agenda/
├── index.html                     Reporte interactivo (10 + 1 secciones, figuras, bilingüe)
├── data/
│   ├── literary_cultures_db.xlsx  Base de datos (27 variables, 9 hojas de análisis)
│   ├── literary_cultures_db.csv   La misma tabla, texto plano (UTF-8)
│   └── literary_cultures_db.json  Versión legible por máquina
├── scripts/
│   ├── build_db.py                Genera el CSV/JSON desde los datos del índice
│   └── build_xlsx.py              Genera el libro de Excel con hojas de análisis
├── README.md
└── LICENSE
```

### Alcance de los datos
- **N = 176** capítulos y documentos (censo completo; se excluyen introducciones firmadas y aparato crítico).
- Distribución: Vol. I = 65 · Vol. II = 57 · Vol. III = 54.
- **27 variables** por registro. Las columnas *Región, Tema, Periodo* y sus derivados (*Macro_region, Macro_tema, Siglo_foco, Eje_Brasil, Enfoque_disciplinar, Escala_geografica, Eje_alteridad, Tipo_alteridad, Formato_texto, N_autores_grupo, Periodo_ordinal, Ambito_ling_prob*) son **codificación analítica propuesta, no datos del original**: son hipótesis de lectura revisables. El diccionario completo está en la hoja *Diccionario variables* del `.xlsx`.

### Advertencias de fiabilidad
- Los datos se extrajeron por **OCR** del índice y se reconstruyeron a mano; los valores dudosos fueron verificados y corregidos.
- La variable `Ambito_ling_prob` (lengua original probable) es una **estimación de baja fiabilidad** basada en la región, no un dato del original.

### Reproducir la base
Requiere Python 3 y `openpyxl`:
```bash
pip install openpyxl
cd scripts
python3 build_db.py      # regenera data/*.csv y *.json
python3 build_xlsx.py    # regenera data/*.xlsx
```

### Cómo citar
> David Chavarría (2026). *La agenda de Literary Cultures of Latin America: base de datos y reporte analítico* [conjunto de datos y reporte]. GitHub. https://github.com/david-chavarria/literary-cultures-agenda

Para una cita con **DOI**, conecta el repositorio a [Zenodo](https://zenodo.org) y publica una *release*: Zenodo generará un DOI citable de esa versión.

**Obra analizada:** Valdés, Mario J. y Djelal Kadir (eds.). *Literary Cultures of Latin America: A Comparative History*. New York: Oxford University Press, 2004. 3 vols.

---

## 🇬🇧 English

### What this is
A dataset and an analytical report built from the **table of contents** of the work. It does not reproduce the chapters' text: it systematizes their **metadata** (volume, part, section, chapter, title, authorship, page) and adds **derived analytical labels** to enable a quantitative reading of the project's "working agenda" — what it chose to study, over which regions, with which themes, in which periods, and from which disciplines.

It was produced as **teaching material** for a doctoral seminar in *Literary Historiography*.

### Data scope
- **N = 176** chapters and documents (full census; signed introductions and critical apparatus excluded).
- **27 variables** per record. The fields *Region, Theme, Period* and their derivatives are **proposed analytical coding, not original data** — revisable reading hypotheses. Full data dictionary in the `Diccionario variables` sheet of the `.xlsx`.
- `Ambito_ling_prob` (likely original language) is a **low-reliability estimate** based on region.

### Reproduce
```bash
pip install openpyxl
cd scripts && python3 build_db.py && python3 build_xlsx.py
```

---

## 🚀 Publicar en GitHub Pages / Publish on GitHub Pages
1. Sube el repositorio a GitHub (ver comandos abajo).
2. En GitHub: **Settings → Pages**.
3. En *Build and deployment → Source*, elige **Deploy from a branch**.
4. *Branch*: `main` · carpeta `/ (root)` → **Save**.
5. En 1–2 minutos el reporte estará en `https://david-chavarria.github.io/literary-cultures-agenda/`.

## 📄 Licencia / License
- **Reporte y datos / Report and data:** [Creative Commons Attribution 4.0 (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) — ver `LICENSE`.
- **Código de `scripts/` / Code in `scripts/`:** MIT.

Puedes reutilizar y adaptar todo con atribución. / You may reuse and adapt everything with attribution.
