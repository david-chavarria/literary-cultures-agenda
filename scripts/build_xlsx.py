# -*- coding: utf-8 -*-
import json
from collections import Counter, defaultdict
import os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table, TableStyleInfo

base = os.path.join(os.path.dirname(__file__), "..", "data")
out = os.path.join(base, "literary_cultures_db.xlsx")
rows = json.load(open(base+"/literary_cultures_db.json", encoding="utf-8"))

COLS = ["Volumen","Volumen_titulo","Parte","Parte_titulo","Seccion","Seccion_titulo",
        "Tipo","N_capitulo","Titulo","Autores","N_autores","Pagina","Region","Tema","Periodo",
        "Macro_region","Eje_Brasil","Escala_geografica","Macro_tema","Enfoque_disciplinar",
        "Eje_alteridad","Tipo_alteridad","Formato_texto","Siglo_foco","Periodo_ordinal",
        "N_autores_grupo","Ambito_ling_prob"]

NAVY="1F3864"; BLUE="2E5496"; LTBLUE="D9E1F2"; GREY="F2F2F2"; GOLD="BF9000"
hdr_fill=PatternFill("solid",fgColor=NAVY)
hdr_font=Font(color="FFFFFF",bold=True,size=11)
title_font=Font(color=NAVY,bold=True,size=15)
sub_font=Font(color=BLUE,bold=True,size=12)
wrap=Alignment(vertical="top",wrap_text=True)
top=Alignment(vertical="top")
ctr=Alignment(horizontal="center",vertical="top")
thin=Side(style="thin",color="BFBFBF")
border=Border(left=thin,right=thin,top=thin,bottom=thin)

wb=Workbook()

# ---------- Hoja 1: Base de datos ----------
ws=wb.active; ws.title="Base de datos"
ws.append(COLS)
for c in range(1,len(COLS)+1):
    cell=ws.cell(1,c); cell.fill=hdr_fill; cell.font=hdr_font
    cell.alignment=Alignment(horizontal="center",vertical="center",wrap_text=True); cell.border=border
for r in rows:
    ws.append([r[c] for c in COLS])
widths=[8,26,7,30,8,34,13,10,52,34,10,9,22,26,18,
        22,15,22,32,32,12,24,20,16,14,18,20]
for i,w in enumerate(widths,1): ws.column_dimensions[get_column_letter(i)].width=w
nrow=len(rows)+1
for rr in range(2,nrow+1):
    for cc in range(1,len(COLS)+1):
        cell=ws.cell(rr,cc); cell.border=border
        cell.alignment=wrap if cc in (2,4,6,9,10) else top
        if rr%2==0: cell.fill=PatternFill("solid",fgColor=GREY)
tab=Table(displayName="BaseDatos",ref=f"A1:{get_column_letter(len(COLS))}{nrow}")
tab.tableStyleInfo=TableStyleInfo(name="TableStyleLight9",showRowStripes=False,showColumnStripes=False)
ws.add_table(tab)
ws.freeze_panes="A2"
ws.auto_filter.ref=f"A1:{get_column_letter(len(COLS))}{nrow}"

def style_summary(ws,title,subtitle=None):
    ws.sheet_view.showGridLines=False
    ws["A1"]=title; ws["A1"].font=title_font
    r=2
    if subtitle:
        ws["A2"]=subtitle; ws["A2"].font=Font(italic=True,color="808080",size=10); r=3
    return r+1

def write_table(ws,startrow,headers,data,widths=None,total_label="TOTAL"):
    hr=startrow
    for j,h in enumerate(headers,1):
        c=ws.cell(hr,j,h); c.fill=hdr_fill; c.font=hdr_font
        c.alignment=Alignment(horizontal="center",vertical="center",wrap_text=True); c.border=border
    rr=hr+1
    for drow in data:
        for j,v in enumerate(drow,1):
            c=ws.cell(rr,j,v); c.border=border
            c.alignment=ctr if j>1 else top
            if rr%2==0: c.fill=PatternFill("solid",fgColor=GREY)
        rr+=1
    if widths:
        for i,w in enumerate(widths,1): ws.column_dimensions[get_column_letter(i)].width=w
    return rr

caps=[r for r in rows if r["Tipo"] in ("Capitulo","Documento")]

# ---------- Hoja 2: Resumen estructura ----------
ws2=wb.create_sheet("Resumen estructura")
r=style_summary(ws2,"Estructura de la obra (3 volumenes / 10 partes)",
    "Conteo de capitulos y documentos por volumen y parte. Introducciones y aparato critico excluidos del conteo.")
# por volumen
vol_titles={1:"I. Configurations of Literary Culture",2:"II. Institutional Modes and Cultural Modalities",3:"III. Latin American Literary Culture: Subject to History"}
data=[]
for v in (1,2,3):
    data.append([vol_titles[v], sum(1 for x in caps if x["Volumen"]==v)])
data.append(["TOTAL", len(caps)])
r=write_table(ws2,r,["Volumen","Capitulos + Documentos"],data,widths=[52,24]); r+=2
# por parte
ws2.cell(r,1,"Detalle por parte"); ws2.cell(r,1).font=sub_font; r+=1
partkey=defaultdict(int); partname={}
for x in caps:
    k=(x["Volumen"],x["Parte"]); partkey[k]+=1
    partname[k]=f"Vol {x['Volumen']} - Parte {x['Parte']}: {x['Parte_titulo']}"
data=[[partname[k],partkey[k]] for k in sorted(partkey)]
write_table(ws2,r,["Parte","Capitulos + Documentos"],data,widths=[70,24])

# ---------- Hoja 3: Por region ----------
ws3=wb.create_sheet("Por region")
r=style_summary(ws3,"Distribucion geografica de los contenidos",
    "Region = etiqueta analitica derivada (no aparece en el original). Solo capitulos y documentos.")
cnt=Counter(x["Region"] for x in caps)
data=[[k,v,f"{v/len(caps)*100:.1f}%"] for k,v in cnt.most_common()]
data.append(["TOTAL",len(caps),"100%"])
write_table(ws3,r,["Region","N","%"],data,widths=[34,10,10])

# ---------- Hoja 4: Por tema ----------
ws4=wb.create_sheet("Por tema")
r=style_summary(ws4,"Distribucion tematica de los contenidos",
    "Tema = etiqueta analitica derivada (no aparece en el original). Solo capitulos y documentos.")
cnt=Counter(x["Tema"] for x in caps)
data=[[k,v,f"{v/len(caps)*100:.1f}%"] for k,v in cnt.most_common()]
data.append(["TOTAL",len(caps),"100%"])
write_table(ws4,r,["Tema","N","%"],data,widths=[36,10,10])

# ---------- Hoja 5: Por periodo ----------
ws5=wb.create_sheet("Por periodo")
r=style_summary(ws5,"Distribucion por periodo historico",
    "Periodo = etiqueta analitica derivada. Solo capitulos y documentos.")
cnt=Counter(x["Periodo"] for x in caps)
data=[[k,v,f"{v/len(caps)*100:.1f}%"] for k,v in cnt.most_common()]
data.append(["TOTAL",len(caps),"100%"])
write_table(ws5,r,["Periodo","N","%"],data,widths=[26,10,10])

# ---------- Hoja 6: Autores ----------
ws6=wb.create_sheet("Autores")
r=style_summary(ws6,"Autores por numero de contribuciones",
    "Incluye capitulos, documentos e introducciones firmadas. Coautorias contabilizadas individualmente.")
allrows=[x for x in rows if x["Tipo"] in ("Capitulo","Documento","Introduccion")]
au=Counter()
for x in allrows:
    if x["Autores"]:
        for a in x["Autores"].split("; "):
            if "incierto" in a or "cortado" in a: continue
            au[a]+=1
data=[[k,v] for k,v in au.most_common() if v>=1]
r=write_table(ws6,r,["Autor/a","N contribuciones"],data,widths=[42,18])

# ---------- Hoja 7: Cruce region x tema ----------
ws7=wb.create_sheet("Region x Tema")
r=style_summary(ws7,"Matriz Region x Tema (capitulos y documentos)",
    "Frecuencias cruzadas. Ambas dimensiones son etiquetas analiticas derivadas.")
temas=[t for t,_ in Counter(x["Tema"] for x in caps).most_common()]
regs=[rg for rg,_ in Counter(x["Region"] for x in caps).most_common()]
m=defaultdict(int)
for x in caps: m[(x["Region"],x["Tema"])]+=1
# header
hr=r
ws7.cell(hr,1,"Region \\ Tema").fill=hdr_fill; ws7.cell(hr,1).font=hdr_font; ws7.cell(hr,1).border=border
ws7.cell(hr,1).alignment=Alignment(horizontal="center",vertical="center",wrap_text=True)
for j,t in enumerate(temas,2):
    c=ws7.cell(hr,j,t); c.fill=hdr_fill; c.font=hdr_font; c.border=border
    c.alignment=Alignment(horizontal="center",vertical="bottom",wrap_text=True,text_rotation=90)
rr=hr+1
for rg in regs:
    ws7.cell(rr,1,rg).border=border; ws7.cell(rr,1).font=Font(bold=True,size=10)
    for j,t in enumerate(temas,2):
        v=m.get((rg,t),0)
        c=ws7.cell(rr,j, v if v else "")
        c.border=border; c.alignment=ctr
        if v: c.fill=PatternFill("solid",fgColor=LTBLUE)
    rr+=1
ws7.column_dimensions["A"].width=30
for j in range(2,len(temas)+2): ws7.column_dimensions[get_column_letter(j)].width=5
ws7.row_dimensions[hr].height=120

# ---------- Hoja: Diccionario de variables ----------
wsd=wb.create_sheet("Diccionario variables")
wsd.sheet_view.showGridLines=False
wsd["A1"]="Diccionario de variables"; wsd["A1"].font=title_font
wsd["A2"]="Columnas originales del indice + etiquetas derivadas (codificacion analitica propuesta, revisable)."
wsd["A2"].font=Font(italic=True,color="808080",size=10)
dic=[
 ("Variable","Origen","Descripcion / categorias"),
 ("Volumen / _titulo","Original","Tomo I-III."),
 ("Parte / Seccion (+titulo)","Original","Jerarquia editorial (10 partes)."),
 ("Tipo","Original","Capitulo / Documento / Introduccion / Front-Back matter."),
 ("N_capitulo","Original","Numeracion correlativa por volumen."),
 ("Titulo / Autores / N_autores","Original","Datos bibliograficos."),
 ("Pagina","Original","Solo Vol. I (indice de II y III sin paginacion)."),
 ("Region","Derivada","Foco geografico fino (16 valores)."),
 ("Tema","Derivada","Tema fino (102 valores; util para busqueda, no para cruces)."),
 ("Periodo","Derivada","Periodo historico fino."),
 ("Macro_region","Derivada (nueva)","Region agrupada en 12: Mexico, Centroamerica, Caribe, Andes, Amazonia, Cono Sur, Brasil, EE.UU.(Latino), Europa, Hispanoamerica(transnac.), Pan-latinoamericano, Multirregional."),
 ("Eje_Brasil","Derivada (nueva)","Dicotomia estructural: Brasil / Hispanoamerica / Transversal."),
 ("Escala_geografica","Derivada (nueva)","Ciudad-local / Nacional / Subregional / Pan-latinoamericano / Transnacional-Diaspora / Multirregional."),
 ("Macro_tema","Derivada (nueva)","Tema agrupado en ~20 macro-categorias (para cruces y graficos)."),
 ("Enfoque_disciplinar","Derivada (nueva)","Critica e hist. literaria / Historia cultural e institucional / Antropologia cultural / Linguistica / Artes escenicas / Cine y medios / Geografia cultural / Teoria e historiografia / Historia intelectual."),
 ("Eje_alteridad","Derivada (nueva)","Si / No: el texto trata un sujeto de alteridad o minoria."),
 ("Tipo_alteridad","Derivada (nueva)","Etnico-racial(indigena/afro), Genero y sexualidad, Etnico-religioso(judia), Migratorio/diasporico, Socioeconomico, Ninguno."),
 ("Formato_texto","Derivada (nueva)","Panoramico-sintesis / Caso de estudio / Documento primario (heuristica por titulo)."),
 ("Siglo_foco","Derivada (nueva)","Banda temporal: Prehispanico, Colonial, s.XIX, s.XIX-XX, s.XX, s.XXI, Transversal."),
 ("Periodo_ordinal","Derivada (nueva)","Codigo ordinal (1 Prehisp. -> 5 s.XXI) para analisis ordenado; vacio = transversal."),
 ("N_autores_grupo","Derivada (nueva)","Individual / Coautoria(2-3) / Colectivo(4+)."),
 ("Ambito_ling_prob","Derivada (nueva)","BAJA FIABILIDAD. Lengua original probable segun region (Portugues/Espanol/Ingles/Frances). Estimacion, no dato."),
]
r=4
for i,(a,b,c) in enumerate(dic):
    ra=wsd.cell(r,1,a); rb=wsd.cell(r,2,b); rc=wsd.cell(r,3,c)
    for cell in (ra,rb,rc): cell.border=border; cell.alignment=wrap
    if i==0:
        for cell in (ra,rb,rc): cell.fill=hdr_fill; cell.font=hdr_font
    else:
        ra.font=Font(bold=True,size=10)
        rb.font=Font(size=9,italic=True,color=("C00000" if "nueva" in b else "808080"))
        if r%2==0:
            for cell in (ra,rb,rc): cell.fill=PatternFill("solid",fgColor=GREY)
    r+=1
wsd.column_dimensions["A"].width=26; wsd.column_dimensions["B"].width=17; wsd.column_dimensions["C"].width=92

# ---------- Hoja 8: Notas ----------
ws8=wb.create_sheet("Notas metodologicas")
ws8.sheet_view.showGridLines=False
ws8.column_dimensions["A"].width=110
notas=[
 ("Literary Cultures of Latin America: A Comparative History","title"),
 ("Mario J. Valdes y Djelal Kadir (editores). Oxford University Press, 2004. 3 volumenes.","sub"),
 ("",""),
 ("QUE ES ESTE ARCHIVO","h"),
 ("Base de datos estructurada extraida del INDICE (tabla de contenidos) de la obra. No incluye el texto de los capitulos, solo sus metadatos: volumen, parte, seccion, numero de capitulo, titulo, autoria y pagina.","p"),
 ("A esos datos originales se anaden tres columnas de clasificacion analitica propuesta (Region, Tema, Periodo) para permitir el analisis cuantitativo y tematico.","p"),
 ("",""),
 ("FUENTE Y METODO","h"),
 ("Texto extraido del PDF del indice mediante OCR (pdftotext). Reconstruccion manual de la jerarquia Volumen > Parte > Seccion > Capitulo.","p"),
 ("Total de registros: 205. De ellos, 176 son capitulos (171) o documentos (5); 20 son introducciones firmadas de partes/secciones; el resto es aparato critico (indices, lista de colaboradores).","p"),
 ("Distribucion de capitulos+documentos: Vol. I = 65, Vol. II = 57, Vol. III = 54.","p"),
 ("",""),
 ("COLUMNAS","h"),
 ("Volumen / Volumen_titulo: numero (I-III) y titulo del tomo.","p"),
 ("Parte / Parte_titulo: division mayor dentro del volumen (10 partes en total).","p"),
 ("Seccion / Seccion_titulo: subdivision tematica dentro de la parte.","p"),
 ("Tipo: Capitulo, Documento, Introduccion, Front matter o Back matter.","p"),
 ("N_capitulo: numeracion correlativa de capitulos DENTRO de cada volumen.","p"),
 ("Titulo / Autores / N_autores: datos bibliograficos del texto.","p"),
 ("Pagina: solo disponible para el Vol. I (el indice de Vols. II y III no trae paginacion).","p"),
 ("Region / Tema / Periodo: ETIQUETAS DERIVADAS por clasificacion. No figuran en el original; son una propuesta revisable para el analisis.","p"),
 ("",""),
 ("ADVERTENCIAS DE FIABILIDAD (OCR)","h"),
 ("El texto provino de OCR. Datos que estaban ilegibles y fueron completados/corregidos por el usuario:","p"),
 ("  - Vol II, cap. 10 (State Sponsorship and Control of Publishing in Brazil): Fabio Lucas. [resuelto]","p"),
 ("  - Vol II, cap. 28 (The Sermon in the Seventeenth Century): Alcir Pecora. [confirmado]","p"),
 ("  - Vol II, cap. 30 (Novel and Journalism: Strategic Interchanges): Anibal Gonzalez Perez. [resuelto]","p"),
 ("  - Vol III, cap. 48 (The Postmodern in Brazilian Literary Theory and Criticism): Italo Moriconi. [resuelto]","p"),
 ("  - Vol I, cap. 23: pagina 212. Vol I, cap. 43: pagina 401. Vol I, cap. 53: pagina 525. [confirmadas]","p"),
 ("Todos los datos ilegibles del OCR fueron completados y verificados por el usuario. No quedan campos pendientes.","p"),
 ("",""),
 ("SUGERENCIAS DE ANALISIS","h"),
 ("- Filtrar la hoja 'Base de datos' por cualquier columna (autofiltro activado).","p"),
 ("- Crear tablas dinamicas cruzando Region/Tema/Periodo/Volumen.","p"),
 ("- Observar el peso de Brasil (46 textos) frente al resto: la obra integra explicitamente la tradicion luso-brasilena.","p"),
 ("- El eje 'Ciudades/Centros culturales' (todo el Vol. II Parte 3) es el mas numeroso: 23 textos.","p"),
 ("- Comparar la presencia de temas de alteridad (genero, indigena, afrodescendiente, judia) concentrados en Vol. I Parte 2.","p"),
]
rr=1
for txt,kind in notas:
    c=ws8.cell(rr,1,txt)
    if kind=="title": c.font=title_font
    elif kind=="sub": c.font=Font(italic=True,color="808080",size=11)
    elif kind=="h": c.font=Font(bold=True,color="FFFFFF",size=11); c.fill=PatternFill("solid",fgColor=BLUE)
    else: c.font=Font(size=10); c.alignment=Alignment(wrap_text=True,vertical="top")
    rr+=1

wb.save(out)
print("Guardado:", out)
print("Hojas:", wb.sheetnames)
