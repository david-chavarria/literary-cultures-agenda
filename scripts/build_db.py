# -*- coding: utf-8 -*-
"""
Base de datos analitica del indice de:
  Valdes, Mario J. & Djelal Kadir (eds.),
  "Literary Cultures of Latin America: A Comparative History"
  (Oxford University Press, 2004), 3 vols.

Campos por registro:
  volumen, vol_titulo, parte, parte_titulo, seccion, seccion_titulo,
  tipo (Introduccion/Capitulo/Documento/Front matter/Back matter),
  n_cap (numero de capitulo dentro del volumen), titulo, autores (lista),
  pagina, region, tema, periodo

Notas de fiabilidad:
 - Vol. I trae numeros de pagina en el indice OCR; Vols. II y III no.
 - region / tema / periodo son etiquetas DERIVADAS (clasificacion analitica
   propuesta), no aparecen en el original: revisables.
 - Algunos nombres/paginas tienen ruido de OCR; los inciertos se marcan con (?).
"""
import csv, json

VT = {
 1: "Configurations of Literary Culture",
 2: "Institutional Modes and Cultural Modalities",
 3: "Latin American Literary Culture: Subject to History",
}

# Cada registro:
# (vol, parte, parte_tit, seccion, seccion_tit, tipo, ncap, titulo, [autores], pagina, region, tema, periodo)
R = []
def add(*a): R.append(a)

# ============================ VOLUMEN I ============================
# --- Front matter Vol I ---
add(1,0,"","","","Front matter","","Introduction: Beyond Literary History",["Mario J. Valdes"],"xvii","Pan-latinoamericana","Historiografia/Teoria","N/A")
add(1,0,"","","","Front matter","","Series Overview: Rethinking Literary History—Comparatively",["Mario J. Valdes","Linda Hutcheon"],"xxvii","Pan-latinoamericana","Historiografia/Teoria","N/A")
add(1,0,"","","","Front matter","","Coeditor's Introduction: History after History",["Djelal Kadir"],"xxxi","Pan-latinoamericana","Historiografia/Teoria","N/A")
add(1,0,"","","","Front matter","","Introduction to Volume I: For a More Inclusive Literary History of Latin America",["Luisa Campuzano"],"xxxvii","Pan-latinoamericana","Historiografia/Teoria","N/A")

# --- Parte 1 ---
P1="Parameters of Literary Culture"
add(1,1,P1,0,"","Introduccion","","Introduction: Parameters of Literary Culture",["Mario J. Valdes"],"1","Pan-latinoamericana","Historiografia/Teoria","N/A")
S="Geographic Factors and the Formation of Cultural Terrain for Literary Production"
add(1,1,P1,1,S,"Capitulo",1,"The Formation of a Cultural Territory",["Herve Thery"],"3","Pan-latinoamericana","Geografia/Territorio","Multiple")
add(1,1,P1,1,S,"Capitulo",2,"From the New Spain of Cortes to the Mexican, Central American, and Caribbean Mosaic",["Alain Musset"],"18","Mexico/Centroamerica/Caribe","Geografia/Territorio","Multiple")
add(1,1,P1,1,S,"Capitulo",3,"The Andean Countries",["Jean-Paul Deler"],"28","Andes","Geografia/Territorio","Multiple")
add(1,1,P1,1,S,"Capitulo",4,"Brazil: A Continent, An Archipelago",["Herve Thery"],"37","Brasil","Geografia/Territorio","Multiple")
add(1,1,P1,1,S,"Capitulo",5,"The Southern Cone",["Sebastian Velut"],"48","Cono Sur","Geografia/Territorio","Multiple")
add(1,1,P1,1,S,"Capitulo",6,"The Amazon: The Forgotten Heart",["Emmanuel Lezy"],"56","Amazonia","Geografia/Territorio","Multiple")
S="Demographics and the Formation of Cultural Centers"
add(1,1,P1,2,S,"Capitulo",7,"Demography, Language, and Cultural Centers",["Nicolas Sanchez Albornoz"],"61","Pan-latinoamericana","Demografia/Lengua","Multiple")
S="Linguistic Diversity of Latin American Literary Cultures"
add(1,1,P1,3,S,"Capitulo",8,"Linguistic Diversity in Mexico",["Beatriz Garza Cuaron"],"69","Mexico","Lenguas/Linguistica","Multiple")
add(1,1,P1,3,S,"Documento",9,"Document: Tzotzil Text",["Juan Gonzalez Hernandez"],"82","Mexico","Lenguas indigenas","Contemporaneo")
add(1,1,P1,3,S,"Documento",10,"Document: Zapotec Text",["Santiago Fabian"],"83","Mexico","Lenguas indigenas","Contemporaneo")
add(1,1,P1,3,S,"Capitulo",11,"Linguistic Diversity in Venezuela",["Marie-Claude Mattei Muller"],"85","Andes","Lenguas/Linguistica","Multiple")
add(1,1,P1,3,S,"Capitulo",12,"Linguistic Diversity in Colombia",["Jon Landaburu"],"90","Andes","Lenguas/Linguistica","Multiple")
add(1,1,P1,3,S,"Capitulo",13,"Linguistic Diversity in the Andean Countries (Argentina, Bolivia, Chile, Ecuador, Peru) and Paraguay",["Willem F. H. Adelaar"],"96","Andes/Cono Sur","Lenguas/Linguistica","Multiple")
add(1,1,P1,3,S,"Capitulo",14,"The Portuguese Language in Brazil",["Marianne Akerberg"],"104","Brasil","Lenguas/Linguistica","Multiple")
S="History of the Production of Literary Cultures in Colonial Latin America"
add(1,1,P1,4,S,"Capitulo",15,"The Production of Literary Culture in New Spain",["Jose Joaquin Blanco"],"109","Mexico","Cultura letrada colonial","Colonial")
add(1,1,P1,4,S,"Capitulo",16,"The Context of Literary Culture in the Caribbean",["Jorge Luis Camacho"],"120","Caribe","Cultura letrada colonial","Colonial")
add(1,1,P1,4,S,"Capitulo",17,"The Foundations of Brazilian Literary Culture",["Tania Franco Carvalhal"],"126","Brasil","Cultura letrada colonial","Colonial")
add(1,1,P1,4,S,"Capitulo",18,"Literary Culture during the Peruvian Viceroyalty",["Luis Millones"],"133","Andes","Cultura letrada colonial","Colonial")
S="Access and Participation in the Literary Cultures of Latin America"
add(1,1,P1,5,S,"Capitulo",19,"Social History of the Latin American Writer",["Mario J. Valdes"],"155","Pan-latinoamericana","Autoria/Campo literario","Multiple")
add(1,1,P1,5,S,"Capitulo",20,"Reading as a Historical Practice in Latin America: The First Colonial Period to the Nineteenth Century",["Juan Poblete"],"178","Pan-latinoamericana","Lectura/Publico","Colonial/s.XIX")
add(1,1,P1,5,S,"Capitulo",21,"Literary Nationalism in Latin America",["Leyla Perrone-Moises"],"193","Pan-latinoamericana","Nacionalismo/Identidad","s.XIX-XX")

# --- Parte 2 ---
P2="From the Margins of Literary History"
add(1,2,P2,0,"","Introduccion","","Introduction",["Cynthia Steele","Heloisa Buarque de Hollanda","Marlyse Meyer","Beatriz Resende"],"201","Pan-latinoamericana","Alteridad/Margenes","N/A")
S="Configurations of Socioeconomic, Racial, and Ethnic Alterity in Literary History"
add(1,2,P2,1,S,"Capitulo",22,"Poverty in the History of Literary Cultures",["Kathleen Newman"],"209","Pan-latinoamericana","Clase/Pobreza","Multiple")
add(1,2,P2,1,S,"Capitulo",23,"First Nations, First Writers: Indigenous Mexican Literary History",["Cynthia Steele"],"212","Mexico","Indigena","Multiple")
add(1,2,P2,1,S,"Capitulo",24,"Recent Mayan Incursions into Guatemalan Literary Historiography",["Gail Ament"],"216","Centroamerica","Indigena","Contemporaneo")
add(1,2,P2,1,S,"Capitulo",25,"Andean Indigenous Expression: Resisting Marginality",["Regina Harrison"],"224","Andes","Indigena","Multiple")
add(1,2,P2,1,S,"Capitulo",26,"Brazil's Indigenous Textualities",["Claudia Neiva de Matos"],"231","Brasil","Indigena","Multiple")
add(1,2,P2,1,S,"Capitulo",27,"Afro-Hispanic Writers in Latin American Literary History",["Rosemary Geisdorfer Feal"],"240","Pan-latinoamericana","Afrodescendiente","Multiple")
add(1,2,P2,1,S,"Capitulo",28,"Black Presence in Brazilian Literature: From the Colonial Period to the Twentieth Century",["Heloisa Toller Gomes","Gizelda Melo do Nascimento","Leda Maria Martins"],"246","Brasil","Afrodescendiente","Colonial/s.XX")
add(1,2,P2,1,S,"Capitulo",29,"Jewish Literary Culture in Spanish America",["Saul Sosnowski"],"264","Hispanoamerica","Judia","Multiple")
add(1,2,P2,1,S,"Capitulo",30,"Displacement and Disregard: Brazilian-Jewish Writing and the Search for Narrative Identity",["Nelson H. Vieira"],"273","Brasil","Judia","s.XX")
S="Gender and Sexual Orientation in the Historical Formation of the Cultural Imaginary"
add(1,2,P2,2,S,"Capitulo",31,"Women Writers during the Viceroyalty",["Josefina Muriel"],"279","Hispanoamerica","Genero/Mujeres","Colonial")
add(1,2,P2,2,S,"Capitulo",32,"Saints or Sinners? Life Writings and Colonial Latin American Women",["Kathleen Ann Myers"],"289","Pan-latinoamericana","Genero/Mujeres","Colonial")
add(1,2,P2,2,S,"Capitulo",33,"Mystics and Visionaries: Women's Writing in Eighteenth-Century Portuguese America",["Leila Mezan Algranti"],"303","Brasil","Genero/Mujeres","Colonial")
add(1,2,P2,2,S,"Capitulo",34,"Exclusions in Latin American Literary History",["Debra A. Castillo"],"307","Pan-latinoamericana","Genero/Mujeres","Multiple")
add(1,2,P2,2,S,"Capitulo",35,"Women Writing in Nontraditional Genres",["Maria Elena de Valdes"],"315","Pan-latinoamericana","Genero/Mujeres","s.XX")
add(1,2,P2,2,S,"Capitulo",36,"Brazilian Women: Literature from the Nineteenth to the Twentieth Centuries",["Lucia Helena","Sylvia Oroz","Sylvia Paixao"],"328","Brasil","Genero/Mujeres","s.XIX-XX")
add(1,2,P2,2,S,"Capitulo",37,"Constructing the Place of Woman in Brazil's Northeastern Region",["Luzila Goncalves Ferreira"],"338","Brasil","Genero/Mujeres","Multiple")
add(1,2,P2,2,S,"Capitulo",38,"Writing against the Grain: An Overview of Twentieth-Century Lesbian Literature in Latin America",["Elena M. Martinez"],"341","Pan-latinoamericana","Genero/Sexualidad","s.XX")
add(1,2,P2,2,S,"Capitulo",39,"Secrets and Truths",["Daniel Balderston"],"349","Pan-latinoamericana","Genero/Sexualidad","s.XX")
add(1,2,P2,2,S,"Capitulo",40,"Notes toward a History of Homotextuality in Brazilian Literature",["Denilson Lopes"],"356","Brasil","Genero/Sexualidad","s.XX")

# --- Parte 3 ---
P3="Plurality of Discourse in Latin American Culture"
S="Political, Scientific, and Religious Discourses"
add(1,3,P3,1,S,"Introduccion","","Introduction",["Eneida Maria de Souza","Raul Antelo"],"367","Pan-latinoamericana","Discurso politico/religioso","N/A")
add(1,3,P3,1,S,"Capitulo",41,"The Rhetoric of Latin American Nationalism from the Colonial Period to Independence",["Silvia Delfino"],"370","Pan-latinoamericana","Nacionalismo/Identidad","Colonial/Independencia")
add(1,3,P3,1,S,"Capitulo",42,"The Rhetoric of Citizenship in Modernity",["Adriana Rodriguez Persico"],"384","Pan-latinoamericana","Ciudadania/Modernidad","s.XIX-XX")
add(1,3,P3,1,S,"Capitulo",43,"The Struggle Over the Printed Word: The Catholic Church in Brazil and Social Discourse",["Aparecida Paiva"],"401","Brasil","Discurso religioso","Multiple")
add(1,3,P3,1,S,"Capitulo",44,"Scientific Discourse in Brazil and Intellectual Exchange",["Rachel Esteves Lima"],"410","Brasil","Discurso cientifico","Multiple")
add(1,3,P3,1,S,"Capitulo",45,"Bio-Policies Undergoing Transformation: Bodies and Ideas of American Identity",["Claudia Gilman"],"418","Pan-latinoamericana","Cuerpo/Identidad","s.XX")
S="Orality and Literature"
add(1,3,P3,2,S,"Introduccion","","Introduction",["Eugenia Meyer"],"431","Pan-latinoamericana","Oralidad","N/A")
add(1,3,P3,2,S,"Capitulo",46,"The History of Oral Literature in Mexico",["Leonardo Manrique Castaneda"],"436","Mexico","Oralidad","Multiple")
add(1,3,P3,2,S,"Capitulo",47,"African Orality in the Literary Culture of the Caribbean",["Luz Maria Martinez Montiel"],"460","Caribe","Oralidad/Afrodescendiente","Multiple")
add(1,3,P3,2,S,"Capitulo",48,"Orality and Literature in the Peruvian Andean Zone",["Jose Antonio Gimenez Mico"],"471","Andes","Oralidad","Multiple")
add(1,3,P3,2,S,"Capitulo",49,"Argentina, Chile, and Uruguay: A History of Literary Orality",["Eva Grosser Lerner","Eduardo Lucio Molina y Vedia"],"483","Cono Sur","Oralidad","Multiple")
add(1,3,P3,2,S,"Capitulo",50,"Oral Literature in Brazil",["Jerusa Pires Ferreira"],"496","Brasil","Oralidad","Multiple")
add(1,3,P3,2,S,"Capitulo",51,"Textuality and Territoriality in Brazilian Oral Discourse",["Ivete Lara Camargos Walty"],"504","Brasil","Oralidad","Multiple")
S="The Multiplicity and Diversity of Discourses and Theatricalities"
add(1,3,P3,3,S,"Introduccion","","Introduction",["Juan Villegas"],"513","Pan-latinoamericana","Teatro","N/A")
add(1,3,P3,3,S,"Capitulo",52,"The Theater in Pre-Hispanic America",["Juan Villegas"],"515","Pan-latinoamericana","Teatro","Prehispanico")
add(1,3,P3,3,S,"Capitulo",53,"Contemporary Mayan Theater",["Tamara Underiner"],"525","Centroamerica","Teatro","Contemporaneo")
add(1,3,P3,3,S,"Capitulo",54,"Plurality and Diversity of Theater Discourse",["Juan Villegas"],"532","Pan-latinoamericana","Teatro","Multiple")
add(1,3,P3,3,S,"Capitulo",55,"Afro-Latin American Theater",["Juan Villegas"],"548","Pan-latinoamericana","Teatro/Afrodescendiente","Multiple")
add(1,3,P3,3,S,"Capitulo",56,"Theatrical Forms and Their Social Dimensions in Nineteenth-Century Brazil",["Joao Roberto Faria"],"555","Brasil","Teatro","s.XIX")
add(1,3,P3,3,S,"Capitulo",57,"Dramaturgies and Theatricalities: Aspects of the Twentieth-Century Brazilian Literary Scene",["Maria Helena Werneck","Victor Hugo Adler Pereira"],"562","Brasil","Teatro","s.XX")
S="Transformations in Popular Culture"
add(1,3,P3,4,S,"Introduccion","","Introduction",["Mario J. Valdes"],"575","Pan-latinoamericana","Cultura popular","N/A")
add(1,3,P3,4,S,"Capitulo",58,"Laughing through One's Tears: Popular Culture in Mexico",["Carlos Monsivais"],"576","Mexico","Cultura popular","s.XX")
add(1,3,P3,4,S,"Capitulo",59,"Mass Culture and Literature in Latin America",["Ana Maria Amar Sanchez"],"598","Pan-latinoamericana","Cultura de masas","s.XX")
add(1,3,P3,4,S,"Capitulo",60,"Literatura de Cordel: Literature for Market and Voice",["Idelette Muzart Fonseca dos Santos"],"614","Brasil","Cultura popular/Oralidad","Multiple")
add(1,3,P3,4,S,"Capitulo",61,"Religious Celebrations in Brazilian Cultural History",["Marlyse Meyer"],"620","Brasil","Cultura popular/Religion","Multiple")
add(1,3,P3,4,S,"Capitulo",62,"Carnival",["Felix Coluccio","Marta Isabel Coluccio"],"625","Pan-latinoamericana","Cultura popular","Multiple")
add(1,3,P3,4,S,"Capitulo",63,"Popular Memory and the Collective Imagination in Latin American Soap Operas",["Jesus Martin-Barbero"],"630","Pan-latinoamericana","Cultura de masas/Medios","s.XX")
add(1,3,P3,4,S,"Capitulo",64,"The Popular in the Confused Republics?",["Carlos Monsivais"],"640","Pan-latinoamericana","Cultura popular","s.XX")
S="Cinema: Cultural Dialogues and the Process of Modernity"
add(1,3,P3,5,S,"Capitulo",65,"Cultural Dialogues and the Process of Modernity",["Julianne Burton-Carvajal","Zuzana M. Pick"],"651","Pan-latinoamericana","Cine","s.XX")

# ============================ VOLUMEN II ============================
add(2,0,"","","","Front matter","","Introduction",["Walter D. Mignolo"],"","Pan-latinoamericana","Instituciones/Teoria","N/A")

P1="Cultural Institutions"
add(2,1,P1,0,"","Introduccion","","Introduction",["Lisa Block de Behar","Tania Franco Carvalhal"],"","Pan-latinoamericana","Instituciones culturales","N/A")
S="Books and Readers in Latin America"
add(2,1,P1,1,S,"Capitulo",1,"Books, Myths, and the Reading Public in Spanish America during the Sixteenth Century",["Luigi Avonto"],"","Hispanoamerica","Libro/Lectura","Colonial")
add(2,1,P1,1,S,"Capitulo",2,"The Book in Brazil: Libraries and Presses",["Jose Mindlin"],"","Brasil","Libro/Bibliotecas","Multiple")
add(2,1,P1,1,S,"Documento",3,"Document: Oswald: Free Book",["Augusto de Campos"],"","Brasil","Libro","s.XX")
S="Cultural Institutions"
add(2,1,P1,2,S,"Capitulo",4,"Cultural Institutions in Latin America",["K. Alfons Knauth"],"","Pan-latinoamericana","Instituciones culturales","Multiple")
add(2,1,P1,2,S,"Capitulo",5,"Cultural Institutions and Intellectual Life in Brazil",["Luiz Roberto Cairo"],"","Brasil","Instituciones culturales","Multiple")
add(2,1,P1,2,S,"Capitulo",6,"Cultural Models of Representation in Seventeenth-Century Brazil",["Joao Adolfo Hansen"],"","Brasil","Instituciones culturales","Colonial")
add(2,1,P1,2,S,"Capitulo",7,"Museums in Latin America",["Maria de Lourdes Parreiras-Horta"],"","Pan-latinoamericana","Museos/Patrimonio","Multiple")
add(2,1,P1,2,S,"Capitulo",8,"Education in Brazil: Omissions, Advances, and Future Perspectives",["Celio da Cunha"],"","Brasil","Educacion","Multiple")
add(2,1,P1,2,S,"Capitulo",9,"Brazilian Literature in the 1970s: Censorship and the Culture Industry",["Cintia Schwantes","Rildo Cosson"],"","Brasil","Censura/Industria cultural","s.XX")
add(2,1,P1,2,S,"Capitulo",10,"State Sponsorship and Control of Publishing in Brazil",["Fabio Lucas"],"","Brasil","Editorial/Estado","s.XX")
S="Cultural Journalism"
add(2,1,P1,3,S,"Capitulo",11,"Cultural Journalism in Spanish America: An Overview",["Anibal Gonzalez-Perez"],"","Hispanoamerica","Periodismo cultural","Multiple")
add(2,1,P1,3,S,"Capitulo",12,"Criticism and Literature in Brazilian Periodicals of the Romantic Period",["Luiz Roberto Cairo"],"","Brasil","Periodismo cultural","s.XIX")
add(2,1,P1,3,S,"Capitulo",13,"From Journalism to Foundational Text: Os Sertoes [Rebellion in the Backlands]",["Jorge Coli"],"","Brasil","Periodismo/Ensayo","s.XIX-XX")
add(2,1,P1,3,S,"Capitulo",14,"Literary Journalism in Brazil during the First Half of the Twentieth Century",["Ivia Alves"],"","Brasil","Periodismo cultural","s.XX")
add(2,1,P1,3,S,"Capitulo",15,"Literary Periodicals of the 1960s: Proposals for Re-reading",["Luz Rodriguez-Carranza"],"","Pan-latinoamericana","Periodismo cultural","s.XX")
add(2,1,P1,3,S,"Capitulo",16,"Criticism and Cultural Journalism in Contemporary Brazil",["Maria Lucia de Barros Camargo"],"","Brasil","Periodismo/Critica","s.XX")
S="Translation as a Cultural Institution"
add(2,1,P1,4,S,"Capitulo",17,"Translation as a Literary Institution",["Laszlo Scholz"],"","Pan-latinoamericana","Traduccion","Multiple")
add(2,1,P1,4,S,"Capitulo",18,"The Development of a Translation Paideuma and Poetics in Brazil: The Campos Brothers",["Else Ribeiro Pires Vieira"],"","Brasil","Traduccion","s.XX")

P2="Textual Models and Their Transformations"
add(2,2,P2,0,"","Introduccion","","Introduction",["Randolph D. Pope","Flora Sussekind"],"","Pan-latinoamericana","Generos/Modelos textuales","N/A")
S="Form and Figuration"
add(2,2,P2,1,S,"Capitulo",19,"The Book and the Format of the Novel",["Jussara Menezes Quadros"],"","Pan-latinoamericana","Novela/Forma","Multiple")
add(2,2,P2,1,S,"Capitulo",20,"The Representation of Nature in Nineteenth-Century Narrative and Iconography",["Luz Aurora Pimentel"],"","Pan-latinoamericana","Naturaleza/Representacion","s.XIX")
S="Poetic Models and the Cultural Imaginary"
add(2,2,P2,2,S,"Capitulo",21,"Poetic Exchange and Epic Landscapes",["Gwen Kirkpatrick"],"","Pan-latinoamericana","Poesia","Multiple")
add(2,2,P2,2,S,"Capitulo",22,"An Emerging Poetry",["Noe Jitrik"],"","Pan-latinoamericana","Poesia","Multiple")
S="Forms of Discourse in Testimonio, Autobiography, and Letter Writing"
add(2,2,P2,3,S,"Capitulo",23,"In the Web of Reality: Latin American Testimonio",["Elzbieta Sklodowska"],"","Pan-latinoamericana","Testimonio","s.XX")
add(2,2,P2,3,S,"Documento",24,"Document: From the Spoken to the Written Word",["Elena Poniatowska"],"","Mexico","Testimonio","s.XX")
add(2,2,P2,3,S,"Capitulo",25,"The Epistolary Genre and Brazilian Modernism",["Julio Castanon Guimaraes"],"","Brasil","Epistolar/Modernismo","s.XX")
S="The Essay and Its Corollaries"
add(2,2,P2,4,S,"Capitulo",26,"The Comparative Drive in the Latin American Essay",["Randolph D. Pope"],"","Pan-latinoamericana","Ensayo","Multiple")
add(2,2,P2,4,S,"Capitulo",27,"Satire and Temporal Heterogeneity",["Flora Sussekind"],"","Pan-latinoamericana","Satira","Multiple")
add(2,2,P2,4,S,"Capitulo",28,"The Sermon in the Seventeenth Century",["Alcir Pecora"],"","Brasil","Sermon/Retorica","Colonial")
S="The Novel"
add(2,2,P2,5,S,"Capitulo",29,"The Feuilleton and European Models in the Making of the Brazilian Novel",["Marlyse Meyer"],"","Brasil","Novela/Folletin","s.XIX")
add(2,2,P2,5,S,"Capitulo",30,"Novel and Journalism: Strategic Interchanges",["Anibal Gonzalez Perez"],"","Pan-latinoamericana","Novela/Periodismo","s.XIX-XX")
add(2,2,P2,5,S,"Capitulo",31,"The Making of the Latin American Novel",["Roberto Gonzalez Echevarria"],"","Pan-latinoamericana","Novela","Multiple")

P3="The Cultural Centers of Latin America"
add(2,3,P3,0,"","Introduccion","","Introduction",["Eduardo F. Coutinho","Victoria Peralta"],"","Pan-latinoamericana","Centros culturales/Ciudades","N/A")
S="Northern Mexico and the Border"
add(2,3,P3,1,S,"Capitulo",32,"Threshold without Frontier: Cultural Limits and Cultural Intervals on the Mexico-U.S. Border",["Jose Manuel Valenzuela Arce"],"","Mexico/EE.UU.","Frontera/Ciudades","Multiple")
S="Mesoamerica"
add(2,3,P3,2,S,"Capitulo",33,"Enlightened Neighborhood: Mexico City as a Cultural Center",["Carlos Monsivais"],"","Mexico","Ciudades/Centros culturales","Multiple")
add(2,3,P3,2,S,"Capitulo",34,"The Cultural Centers of Central America",["Nicasio Urbina","Laura Barbas Rhoden"],"","Centroamerica","Ciudades/Centros culturales","Multiple")
S="The Caribbean"
add(2,3,P3,3,S,"Introduccion","","Introduction",["Marcelino Juan Canino Salgado"],"","Caribe","Ciudades/Centros culturales","N/A")
add(2,3,P3,3,S,"Capitulo",35,"Havana",["Luisa Campuzano"],"","Caribe","Ciudades/Centros culturales","Multiple")
add(2,3,P3,3,S,"Capitulo",36,"Santo Domingo: Center of Innovation, Transition, and Change",["William Luis"],"","Caribe","Ciudades/Centros culturales","Multiple")
add(2,3,P3,3,S,"Capitulo",37,"Puerto Rico: Caribbean Cultural Center",["Marcelino Juan Canino Salgado"],"","Caribe","Ciudades/Centros culturales","Multiple")
S="Andean Region"
add(2,3,P3,4,S,"Introduccion","","Introduction",["Consuelo Trivino Anzola"],"","Andes","Ciudades/Centros culturales","N/A")
add(2,3,P3,4,S,"Capitulo",38,"Caracas",["Alexis Marquez Rodriguez"],"","Andes","Ciudades/Centros culturales","Multiple")
add(2,3,P3,4,S,"Capitulo",39,"Lima: A Blurred Centrality",["Sara Castro-Klaren"],"","Andes","Ciudades/Centros culturales","Multiple")
add(2,3,P3,4,S,"Capitulo",40,"Bogota: From Colonial Hamlet to Cosmopolitan Metropolis",["Victoria Peralta"],"","Andes","Ciudades/Centros culturales","Multiple")
add(2,3,P3,4,S,"Capitulo",41,"Convent in the Clouds: Quito as a Cultural Center",["Regina Harrison"],"","Andes","Ciudades/Centros culturales","Multiple")
add(2,3,P3,4,S,"Capitulo",42,"La Paz—Chukiyawu Marka",["Elizabeth Monasterios"],"","Andes","Ciudades/Centros culturales","Multiple")
S="Amazonia"
add(2,3,P3,5,S,"Introduccion","","Introduction",["Nicomedes Suarez Arauz"],"","Amazonia","Ciudades/Centros culturales","N/A")
add(2,3,P3,5,S,"Capitulo",43,"Belem: Cultural Center",["Benedito Nunes"],"","Amazonia","Ciudades/Centros culturales","Multiple")
add(2,3,P3,5,S,"Documento",44,"Document: The View from Manaus",["Milton Hatoum"],"","Amazonia","Ciudades/Centros culturales","s.XX")
add(2,3,P3,5,S,"Capitulo",45,"Amazonian Cultural Centers of Bolivia",["Nicomedes Suarez Arauz"],"","Amazonia","Ciudades/Centros culturales","Multiple")
S="East and Central Brazil"
add(2,3,P3,6,S,"Introduccion","","Introduction",["Angela Maria Dias"],"","Brasil","Ciudades/Centros culturales","N/A")
add(2,3,P3,6,S,"Capitulo",46,"Recife as a Cultural Center",["Cesar Leal"],"","Brasil","Ciudades/Centros culturales","Multiple")
add(2,3,P3,6,S,"Capitulo",47,"Bahia: Colonization and Cultures",["Eneida Leal Cunha","Jeferson Bacelar","Lizir Arcanjo Alves"],"","Brasil","Ciudades/Centros culturales","Multiple")
add(2,3,P3,6,S,"Capitulo",48,"Rio de Janeiro: Capital City",["Renato Cordeiro Gomes","Margarida de Souza Neves","Monica Pimenta Velloso"],"","Brasil","Ciudades/Centros culturales","Multiple")
add(2,3,P3,6,S,"Capitulo",49,"Sao Paulo: The Cultural Laboratory and Its Close",["Nicolau Sevcenko"],"","Brasil","Ciudades/Centros culturales","Multiple")
add(2,3,P3,6,S,"Capitulo",50,"Ouro Preto, Belo Horizonte, Brasilia: The Utopia of Modernity",["Maria Zilda Ferreira Cury"],"","Brasil","Ciudades/Centros culturales","Multiple")
S="The Pampas, the Southern Borderlands"
add(2,3,P3,7,S,"Introduccion","","Introduction",["Mario J. Valdes"],"","Cono Sur","Ciudades/Centros culturales","N/A")
add(2,3,P3,7,S,"Capitulo",51,"Asuncion as a Cultural Center",["Olga V. Araujo-Mendieta"],"","Cono Sur","Ciudades/Centros culturales","Multiple")
add(2,3,P3,7,S,"Capitulo",52,"Porto Alegre: Cultural Center of Southern Brazil",["Rita Terezinha Schmidt"],"","Brasil","Ciudades/Centros culturales","Multiple")
S="Rio de la Plata and Chile"
add(2,3,P3,8,S,"Introduccion","","Introduction",["Richard J. Walter"],"","Cono Sur","Ciudades/Centros culturales","N/A")
add(2,3,P3,8,S,"Capitulo",53,"Montevideo: From Frontier City to Mercosur",["Hugo Achugar"],"","Cono Sur","Ciudades/Centros culturales","Multiple")
add(2,3,P3,8,S,"Capitulo",54,"Buenos Aires: Cultural Center of River Plate",["Noemi Ulla"],"","Cono Sur","Ciudades/Centros culturales","Multiple")
add(2,3,P3,8,S,"Capitulo",55,"Santiago",["Marcela Orellana"],"","Cono Sur","Ciudades/Centros culturales","Multiple")
S="Latin American Culture in New York and Paris"
add(2,3,P3,9,S,"Capitulo",56,"New York City: Center and Transit Point for Hispanic Cultural Nomadism",["Dionisio Canas","Orlando Hernandez","Doris Schnabel","Luisa Garcia Conde"],"","EE.UU.","Ciudades/Diaspora","s.XX")
add(2,3,P3,9,S,"Capitulo",57,"Paris and Latin Americans, Nineteenth and Twentieth Centuries: From Cultural Metropolis to Cultural Museum?",["Denis Rolland"],"","Europa","Ciudades/Diaspora","s.XIX-XX")

# ============================ VOLUMEN III ============================
add(3,0,"","","","Front matter","","Introduction",["Wander Melo Miranda"],"","Pan-latinoamericana","Historia/Sujeto","N/A")

P1="Fissured Foundations: Nostalgia and New Beginnings"
add(3,1,P1,0,"","Introduccion","","Introduction",["Doris Sommer","Maria Consuelo Cunha Campos"],"","Pan-latinoamericana","Fundaciones/Nostalgia","N/A")
S="Epic Voices: Encounters and Foundations"
add(3,1,P1,1,S,"Capitulo",1,"Epic Voices: Non-encounters and Foundation Myths",["Jose Antonio Mazzotti"],"","Pan-latinoamericana","Epica/Mitos fundacionales","Colonial")
add(3,1,P1,1,S,"Capitulo",2,"Fragment and Totality: Narrating Colonial Encounters",["Guillermo Giucci","Marcelo Rocha Wanderley"],"","Pan-latinoamericana","Encuentro colonial","Colonial")
S="The Discourse of Melancholy: A Culture of Loss"
add(3,1,P1,2,S,"Capitulo",3,"Spectacular Cityscapes of Baroque Spanish America",["Stephanie Merrim"],"","Hispanoamerica","Barroco","Colonial")
add(3,1,P1,2,S,"Capitulo",4,"The Discourse of Melancholy in a Culture of Loss",["Maria Consuelo Cunha Campos"],"","Pan-latinoamericana","Melancolia/Perdida","Multiple")
S="Narratives of Legitimation: The Discourse of Hegemony and the Hermeneutics of Globalization"
add(3,1,P1,3,S,"Capitulo",5,"Narratives of Legitimation: The Invention of History-Monument and the Nation-State",["Beatriz Gonzalez Stephan"],"","Pan-latinoamericana","Nacion/Legitimacion","s.XIX")
add(3,1,P1,3,S,"Capitulo",6,"Creating the National Imaginary",["Vera Follain de Figueiredo"],"","Pan-latinoamericana","Nacion/Imaginario","s.XIX-XX")
S="Discourses of Modernity"
add(3,1,P1,4,S,"Capitulo",7,"National Installments: The Erotics of Modernity in Spanish America",["Doris Sommer"],"","Hispanoamerica","Modernidad/Nacion","s.XIX")
add(3,1,P1,4,S,"Capitulo",8,"In the Public Eye: Naturalism and Brazilian Letters",["Victor Hugo Adler Pereira"],"","Brasil","Naturalismo","s.XIX-XX")

P2="Internal Borders: Cultural Conflicts and State Discourse"
add(3,2,P2,0,"","Introduccion","","Introduction",["Alberto Moreiras"],"","Pan-latinoamericana","Fronteras internas/Estado","N/A")
S="Lettered Mediations"
add(3,2,P2,1,S,"Capitulo",9,"Documents of the First Encounter of Europeans with the New World: Lexicons, Missions, Voyages, and Resistances",["Ettore Finazzi-Agro"],"","Pan-latinoamericana","Encuentro colonial","Colonial")
add(3,2,P2,1,S,"Capitulo",10,"Indigenous, Mestizo, and Imperial Reason",["Marco Luis Dorfsman","Lori Hopkins"],"","Pan-latinoamericana","Mestizaje/Colonial","Colonial")
add(3,2,P2,1,S,"Capitulo",11,'"A Very Subtle Idolatry": Estanislao de Vega Bazan\'s Authentic Testimony of Colonial Andean Religion',["Kenneth Mills"],"","Andes","Religion colonial/Indigena","Colonial")
add(3,2,P2,1,S,"Capitulo",12,"The Three Faces of the Baroque in Mexico and the Caribbean",["Iris M. Zavala"],"","Mexico/Caribe","Barroco","Colonial")
add(3,2,P2,1,S,"Capitulo",13,"The Baroque and Transculturation",["Mabel Morana"],"","Pan-latinoamericana","Barroco/Transculturacion","Colonial")
add(3,2,P2,1,S,"Capitulo",14,"The Baroque Gaze",["Raul Antelo"],"","Pan-latinoamericana","Barroco","Colonial")
add(3,2,P2,1,S,"Capitulo",15,"Francisco Xavier Clavijero and the Enlightenment in Mexico",["Jose Emilio Pacheco"],"","Mexico","Ilustracion","Colonial")
add(3,2,P2,1,S,"Capitulo",16,"New Thinking: From the Enlightenment to Independence",["Susana Rotker"],"","Pan-latinoamericana","Ilustracion/Independencia","Colonial/Independencia")
add(3,2,P2,1,S,"Capitulo",17,"Literary Criollismo and Indigenism",["Horacio Legras"],"","Pan-latinoamericana","Criollismo/Indigenismo","s.XIX-XX")
S="Peoples, Communities, and Nation Building"
add(3,2,P2,2,S,"Capitulo",18,"Projects of Latin American Emancipation: The Caribbean, 1800-1850",["Sibylle Fischer"],"","Caribe","Emancipacion/Nacion","s.XIX")
add(3,2,P2,2,S,"Capitulo",19,"Transculturation and the Discourse of Liberation",["Graciela Montaldo"],"","Pan-latinoamericana","Transculturacion","s.XIX-XX")
add(3,2,P2,2,S,"Capitulo",20,"Transculturation and Nationhood",["Idelber Avelar"],"","Pan-latinoamericana","Transculturacion/Nacion","s.XX")
add(3,2,P2,2,S,"Capitulo",21,"The Brazilian Construction of Nationalism",["Adriana Romeiro"],"","Brasil","Nacionalismo","s.XIX-XX")
S="The Inversion of Social Darwinism"
add(3,2,P2,3,S,"Capitulo",22,'Negrismo: The American "Real"',["Elzbieta Sklodowska"],"","Pan-latinoamericana","Afrodescendiente/Raza","s.XX")
add(3,2,P2,3,S,"Capitulo",23,'The Literary Culture of the "New Order": Mexico 1867-1910',["Leopoldo Zea"],"","Mexico","Positivismo/Estado","s.XIX")
add(3,2,P2,3,S,"Capitulo",24,"The Transcultural Mirror of Science: Race and Self-Representation in Latin America",["Gabriela Nouzeilles"],"","Pan-latinoamericana","Ciencia/Raza","s.XIX-XX")
add(3,2,P2,3,S,"Capitulo",25,"Literary Education and the Making of State Knowledge",["Juan Poblete"],"","Pan-latinoamericana","Educacion/Estado","s.XIX")
add(3,2,P2,3,S,"Capitulo",26,"Mestizaje and the Inversion of Social Darwinism in Spanish American Fiction",["Julie Taylor","George Yudice"],"","Hispanoamerica","Mestizaje/Raza","s.XX")
S="Modernization and the Formation of Cultural Identities"
add(3,2,P2,4,S,"Capitulo",27,"Mexico-U.S. Border Transculturation and State Discourses: Nineteenth and Twentieth Centuries",["Marcus Embry"],"","Mexico/EE.UU.","Frontera/Transculturacion","s.XIX-XX")
add(3,2,P2,4,S,"Capitulo",28,"A Paradigm for Modernity: The Concept of Crisis in Modernismo",["Jorge Luis Camacho"],"","Hispanoamerica","Modernismo","s.XIX-XX")
add(3,2,P2,4,S,"Capitulo",29,"Textual Transcultural Mediations and the Formation of Regional Identity",["Ileana Rodriguez"],"","Pan-latinoamericana","Transculturacion/Identidad","s.XX")
add(3,2,P2,4,S,"Capitulo",30,'Anatomy of the Latin American "Boom" Novel',["Brett Levinson"],"","Pan-latinoamericana","Novela/Boom","s.XX")
add(3,2,P2,4,S,"Capitulo",31,"The Modern Imaginary and Transculturation",["Eneida Maria de Souza"],"","Pan-latinoamericana","Transculturacion/Modernidad","s.XX")

P3="Liminality and Centrality of Literary Cultures in the Twentieth Century"
S="Amerindian Literary Cultures"
add(3,3,P3,1,S,"Introduccion","","Introduction",["Elizabeth Monasterios"],"","Pan-latinoamericana","Indigena","N/A")
add(3,3,P3,1,S,"Capitulo",32,"Literatures of Mesoamerica",["Miguel Leon Portilla"],"","Mexico/Centroamerica","Indigena","Multiple")
add(3,3,P3,1,S,"Capitulo",33,"The Nature of Indigenous Literatures in the Andes",["Denise Y. Arnold","Juan de Dios Yapita"],"","Andes","Indigena","Multiple")
S="Hispanic Cultures in the United States: Diversity, Hybridism, and Constant Transformation"
add(3,3,P3,2,S,"Introduccion","","Introduction",["Juan Villegas"],"","EE.UU.","Latino/EE.UU.","N/A")
add(3,3,P3,2,S,"Capitulo",34,"Reinventing America: The Chicano Literary Tradition",["Maria Herrera-Sobek"],"","EE.UU.","Chicano/Latino","s.XX")
add(3,3,P3,2,S,"Capitulo",35,"Chicano/Latino Theater Today",["Claudia Villegas-Silva"],"","EE.UU.","Chicano/Teatro","s.XX")
add(3,3,P3,2,S,"Capitulo",36,"Puerto Rican Literature in the United States",["Carmen Dolores Hernandez"],"","EE.UU.","Puertorriqueno/Latino","s.XX")
add(3,3,P3,2,S,"Capitulo",37,"Construction of New Cultural Identities: Puerto Rican Theater in New York",["Grace Davila-Lopez"],"","EE.UU.","Puertorriqueno/Teatro","s.XX")
add(3,3,P3,2,S,"Capitulo",38,"Colonial Figures in Motion: Translocality, Tropicalism, and Translation in Contemporary Puerto Rican Literature in the United States",["Arnaldo Cruz Malave"],"","EE.UU.","Puertorriqueno/Latino","s.XX")
add(3,3,P3,2,S,"Capitulo",39,"Cuban Theater in the United States",["Jose A. Escarpanter"],"","EE.UU.","Cubano/Teatro","s.XX")
add(3,3,P3,2,S,"Capitulo",40,"Cuban American Prose: 1975-2000",["Maria Cristina Garcia"],"","EE.UU.","Cubano/Latino","s.XX")

P4="Literary Culture in the Twentieth Century"
add(3,4,P4,0,"","Introduccion","","Introduction",["Renato Cordeiro Gomes","Djelal Kadir","Marilia Rothier Cardoso"],"","Pan-latinoamericana","Siglo XX","N/A")
S="Historic Displacements"
add(3,4,P4,1,S,"Capitulo",41,"Historic Displacements in Twentieth-Century Brazilian Literary Culture",["Renato Cordeiro Gomes","Ana Lucia Almeida Gazolla","Ana Maria de Alencar","Antonio Arnoni Prado","Edson Rosa da Silva","Eneida Leal Cunha","Everardo Rocha","Joao Cezar de Castro Rocha","Marilia Rothier Cardoso","Nadia Battella Gotlib"],"","Brasil","Desplazamientos/s.XX","s.XX")
add(3,4,P4,1,S,"Capitulo",42,"Signs of Identity: Latin American Immigration and Exile",["Clara E. Lida","Francisco Zapata"],"","Pan-latinoamericana","Inmigracion/Exilio","s.XX")
add(3,4,P4,1,S,"Capitulo",43,"Exile in the Narrative of the Spanish American Diaspora in the Twentieth Century",["Ivan Almeida","Cristina Parodi"],"","Hispanoamerica","Exilio/Diaspora","s.XX")
add(3,4,P4,1,S,"Capitulo",44,"Political Exclusion / Literary Inclusion: Argentine and Uruguayan Writers",["Saul Sosnowski"],"","Cono Sur","Exilio/Dictadura","s.XX")
add(3,4,P4,1,S,"Capitulo",45,"Writers under (and after) the Chilean Military Dictatorship",["Javier Campos"],"","Cono Sur","Dictadura","s.XX")
S="Modernity, Modernisms, and Their Avatars"
add(3,4,P4,2,S,"Capitulo",46,"Nations of Modernity",["Javier Lasarte Valcarcel"],"","Pan-latinoamericana","Modernidad","s.XX")
add(3,4,P4,2,S,"Capitulo",47,"Aesthetics of Rupture",["Eneida Maria de Souza"],"","Pan-latinoamericana","Vanguardias/Ruptura","s.XX")
add(3,4,P4,2,S,"Capitulo",48,"The Postmodern in Brazilian Literary Theory and Criticism",["Italo Moriconi"],"","Brasil","Posmodernidad/Critica","s.XX")
S="Ideologies and Imaginaries"
add(3,4,P4,3,S,"Capitulo",49,"Literature and Revolution in Latin America",["Hermann Herlinghaus"],"","Pan-latinoamericana","Revolucion/Politica","s.XX")
add(3,4,P4,3,S,"Capitulo",50,"Imagining Narrative Territories",["Lucille Kerr"],"","Pan-latinoamericana","Narrativa/Imaginario","s.XX")
add(3,4,P4,3,S,"Capitulo",51,"Utopic Theories in Brazil",["Vera Follain de Figueiredo"],"","Brasil","Utopia","s.XX")
add(3,4,P4,3,S,"Capitulo",52,"Conservatism and Modernization in Brazil",["Victor Hugo Adler Pereira"],"","Brasil","Modernizacion/Politica","s.XX")
add(3,4,P4,3,S,"Capitulo",53,"Post-Utopian Imaginaries",["Flavio Carneiro"],"","Brasil","Posutopia","s.XX")
S="By Way of Coda: In Anticipation"
add(3,4,P4,4,S,"Capitulo",54,"Scenes of the Twenty-first Century: The Routes of the New",["Julio Ortega"],"","Pan-latinoamericana","Siglo XXI/Prospectiva","s.XXI")

# --- Back matter ---
add(3,0,"","","","Back matter","","List of Contributors",[],"","","Aparato critico","N/A")
add(3,0,"","","","Back matter","","List of Persons Included in Literary Cultures of Latin America with Birth and Death Dates",[],"","","Aparato critico","N/A")
add(3,0,"","","","Back matter","","Index: Volumes I, II, and III",[],"","","Aparato critico","N/A")

# ============================================================
# RESTAURACION DE ACENTOS (los nombres se habian normalizado a ASCII)
# ============================================================
# Mapa autor ASCII -> forma acentuada correcta. Solo se listan los que cambian.
AUTHOR_ACCENTS = {
 "Adriana Rodriguez Persico":"Adriana Rodríguez Pérsico",
 "Alcir Pecora":"Alcir Pécora",
 "Alexis Marquez Rodriguez":"Alexis Márquez Rodríguez",
 "Ana Lucia Almeida Gazolla":"Ana Lúcia Almeida Gazolla",
 "Ana Maria Amar Sanchez":"Ana María Amar Sánchez",
 "Angela Maria Dias":"Ângela Maria Dias",
 "Anibal Gonzalez Perez":"Aníbal González Pérez",
 "Anibal Gonzalez-Perez":"Aníbal González-Pérez",
 "Antonio Arnoni Prado":"Antônio Arnoni Prado",
 "Arnaldo Cruz Malave":"Arnaldo Cruz Malavé",
 "Beatriz Garza Cuaron":"Beatriz Garza Cuarón",
 "Beatriz Gonzalez Stephan":"Beatriz González Stephan",
 "Carlos Monsivais":"Carlos Monsiváis",
 "Carmen Dolores Hernandez":"Carmen Dolores Hernández",
 "Celio da Cunha":"Célio da Cunha",
 "Cesar Leal":"César Leal",
 "Cintia Schwantes":"Cíntia Schwantes",
 "Consuelo Trivino Anzola":"Consuelo Triviño Anzola",
 "Dionisio Canas":"Dionisio Cañas",
 "Elena M. Martinez":"Elena M. Martínez",
 "Elzbieta Sklodowska":"Elżbieta Sklodowska",
 "Emmanuel Lezy":"Emmanuel Lézy",
 "Ettore Finazzi-Agro":"Ettore Finazzi-Agrò",
 "Fabio Lucas":"Fábio Lucas",
 "Felix Coluccio":"Félix Coluccio",
 "Flavio Carneiro":"Flávio Carneiro",
 "Flora Sussekind":"Flora Süssekind",
 "George Yudice":"George Yúdice",
 "Grace Davila-Lopez":"Grace Dávila-López",
 "Heloisa Buarque de Hollanda":"Heloísa Buarque de Hollanda",
 "Heloisa Toller Gomes":"Heloísa Toller Gomes",
 "Herve Thery":"Hervé Théry",
 "Ileana Rodriguez":"Ileana Rodríguez",
 "Italo Moriconi":"Ítalo Moriconi",
 "Ivan Almeida":"Iván Almeida",
 "Ivia Alves":"Ívia Alves",
 "Javier Lasarte Valcarcel":"Javier Lasarte Valcárcel",
 "Jesus Martin-Barbero":"Jesús Martín-Barbero",
 "Joao Adolfo Hansen":"João Adolfo Hansen",
 "Joao Cezar de Castro Rocha":"João Cezar de Castro Rocha",
 "Joao Roberto Faria":"João Roberto Faria",
 "Jose A. Escarpanter":"José A. Escarpanter",
 "Jose Antonio Gimenez Mico":"José Antonio Giménez Micó",
 "Jose Antonio Mazzotti":"José Antonio Mazzotti",
 "Jose Emilio Pacheco":"José Emilio Pacheco",
 "Jose Joaquin Blanco":"José Joaquín Blanco",
 "Jose Manuel Valenzuela Arce":"José Manuel Valenzuela Arce",
 "Jose Mindlin":"José Mindlin",
 "Juan Gonzalez Hernandez":"Juan González Hernández",
 "Julio Castanon Guimaraes":"Julio Castañón Guimarães",
 "Laszlo Scholz":"László Scholz",
 "Leonardo Manrique Castaneda":"Leonardo Manrique Castañeda",
 "Leyla Perrone-Moises":"Leyla Perrone-Moisés",
 "Lucia Helena":"Lúcia Helena",
 "Luisa Garcia Conde":"Luisa García Conde",
 "Luz Maria Martinez Montiel":"Luz María Martínez Montiel",
 "Luz Rodriguez-Carranza":"Luz Rodríguez-Carranza",
 "Luzila Goncalves Ferreira":"Luzila Gonçalves Ferreira",
 "Mabel Morana":"Mabel Moraña",
 "Maria Cristina Garcia":"María Cristina García",
 "Maria Elena de Valdes":"María Elena de Valdés",
 "Maria Herrera-Sobek":"María Herrera-Sobek",
 "Maria Lucia de Barros Camargo":"Maria Lúcia de Barros Camargo",
 "Marie-Claude Mattei Muller":"Marie-Claude Mattéi Muller",
 "Marilia Rothier Cardoso":"Marília Rothier Cardoso",
 "Mario J. Valdes":"Mario J. Valdés",
 "Miguel Leon Portilla":"Miguel León Portilla",
 "Monica Pimenta Velloso":"Mônica Pimenta Velloso",
 "Nadia Battella Gotlib":"Nádia Battella Gotlib",
 "Nicolas Sanchez Albornoz":"Nicolás Sánchez Albornoz",
 "Nicomedes Suarez Arauz":"Nicomedes Suárez Araúz",
 "Noe Jitrik":"Noé Jitrik",
 "Noemi Ulla":"Noemí Ulla",
 "Olga V. Araujo-Mendieta":"Olga V. Araújo-Mendieta",
 "Orlando Hernandez":"Orlando Hernández",
 "Raul Antelo":"Raúl Antelo",
 "Roberto Gonzalez Echevarria":"Roberto González Echevarría",
 "Santiago Fabian":"Santiago Fabián",
 "Sara Castro-Klaren":"Sara Castro-Klarén",
 "Saul Sosnowski":"Saúl Sosnowski",
 "Sebastian Velut":"Sébastian Velut",
 "Sylvia Paixao":"Sylvia Paixão",
 "Tania Franco Carvalhal":"Tânia Franco Carvalhal",
}
# Toponimos / nombres propios en titulos (subcadena -> acentuada)
TITLE_ACCENTS = {
 "New Spain of Cortes":"New Spain of Cortés",
 "Os Sertoes":"Os Sertões",
 "Belem: Cultural Center":"Belém: Cultural Center",
 "Sao Paulo":"São Paulo",
 "Bogota: From Colonial Hamlet":"Bogotá: From Colonial Hamlet",
 "Belo Horizonte, Brasilia":"Belo Horizonte, Brasília",
 "Asuncion as a Cultural Center":"Asunción as a Cultural Center",
 "Estanislao de Vega Bazan":"Estanislao de Vega Bazán",
}

def restore_accents(rec):
    au = rec[8]  # lista de autores
    rec = list(rec)
    rec[8] = [AUTHOR_ACCENTS.get(a, a) for a in au]
    tit = rec[7]
    for k,v in TITLE_ACCENTS.items():
        if k in tit: tit = tit.replace(k,v)
    rec[7] = tit
    return tuple(rec)

R = [restore_accents(r) for r in R]

# ---------------------------------------------------------------
COLS = ["Volumen","Volumen_titulo","Parte","Parte_titulo","Seccion","Seccion_titulo",
        "Tipo","N_capitulo","Titulo","Autores","N_autores","Pagina","Region","Tema","Periodo",
        "Macro_region","Eje_Brasil","Escala_geografica","Macro_tema","Enfoque_disciplinar",
        "Eje_alteridad","Tipo_alteridad","Formato_texto","Siglo_foco","Periodo_ordinal",
        "N_autores_grupo","Ambito_ling_prob"]

# ============================================================
# ETIQUETAS DERIVADAS ADICIONALES (ejes analiticos para cruces)
# Todas se deducen de Region / Tema / Periodo / Titulo / Tipo / autores.
# ============================================================
def macro_region(reg):
    if "/" in reg: return "Multirregional (2+ areas)"
    m={"Brasil":"Brasil","Mexico":"Mexico","Centroamerica":"Centroamerica",
       "Caribe":"Caribe","Andes":"Andes","Amazonia":"Amazonia","Cono Sur":"Cono Sur",
       "EE.UU.":"EE.UU. (Latino)","Europa":"Europa",
       "Hispanoamerica":"Hispanoamerica (transnac.)","Pan-latinoamericana":"Pan-latinoamericano"}
    return m.get(reg, reg)

def eje_brasil(reg):
    if "Brasil" in reg: return "Brasil"
    if reg in ("Pan-latinoamericana","Europa","Amazonia") or "/" in reg: return "Transversal"
    return "Hispanoamerica"

def escala_geografica(reg, tema, tit):
    if "Diaspora" in tema or reg in ("EE.UU.","Europa") or "EE.UU." in reg: return "Transnacional / Diaspora"
    if "Ciudades" in tema or "Centros culturales" in tema: return "Ciudad / local"
    if reg in ("Pan-latinoamericana","Hispanoamerica"): return "Pan-latinoamericano"
    if "/" in reg: return "Multirregional"
    if reg in ("Andes","Cono Sur","Caribe","Centroamerica","Amazonia"): return "Subregional"
    return "Nacional"

def macro_tema(t):
    t=t.lower()
    rules=[
     (("geografia","territorio"),"Geografia y territorio"),
     (("lengua","linguistica"),"Lenguas y linguistica"),
     (("indigena",),"Mundo indigena"),
     (("afro",),"Afrodescendencia"),
     (("genero",),"Genero y sexualidad"),
     (("judia","clase","pobreza"),"Otras alteridades (judia, clase)"),
     (("oralidad","cultura popular","cultura de masas","medios"),"Oralidad, cultura popular y medios"),
     (("teatro",),"Teatro y artes escenicas"),
     (("cine",),"Cine y audiovisual"),
     (("chicano","latino","puertorriqueno","cubano"),"Literatura latina en EE.UU."),
     (("periodismo","critica","traduccion"),"Prensa, critica y traduccion"),
     (("instituciones","libro","museos","educacion","editorial","bibliotecas","industria","censura"),"Instituciones, libro y educacion"),
     (("ciudades","centros culturales"),"Ciudades y centros culturales"),
     (("novela","poesia","ensayo","testimonio","epistolar","satira","sermon","forma","representacion","folletin","boom","modelos textuales","generos"),"Generos y modelos literarios"),
     (("barroco","ilustracion","letrada colonial","encuentro colonial","religion colonial","mitos fundacionales","epica","independencia"),"Colonial, barroco e Ilustracion"),
     (("transculturacion","nacion","modernid","modernismo","ciudadania","mestizaje","positivismo","criollismo","indigenismo","raza","ciencia","cuerpo","naturalismo"),"Nacion, modernidad y transculturacion"),
     (("exilio","dictadura","revolucion","politica","desplazamientos","inmigracion"),"Exilio, dictadura y politica"),
     (("historiografia","teoria","sujeto","melancolia","utopia","posutopia","posmodernidad","vanguardias","ruptura","imaginario","prospectiva","siglo","fundaciones","legitimacion","perdida","nostalgia"),"Historiografia, teoria y estetica"),
     (("religios","discurso cientifico"),"Discurso religioso y cientifico"),
     (("autoria","campo literario","lectura","publico"),"Autoria, lectura y publico"),
     (("demografia",),"Lenguas y linguistica"),
    ]
    for keys,lab in rules:
        for k in keys:
            if k in t: return lab
    return "Otros / mixto"

def enfoque_disciplinar(mt):
    d={"Teatro y artes escenicas":"Artes escenicas",
       "Cine y audiovisual":"Cine y medios",
       "Lenguas y linguistica":"Linguistica",
       "Oralidad, cultura popular y medios":"Antropologia cultural / est. culturales",
       "Instituciones, libro y educacion":"Historia cultural e institucional",
       "Prensa, critica y traduccion":"Historia cultural e institucional",
       "Ciudades y centros culturales":"Historia cultural e institucional",
       "Geografia y territorio":"Geografia cultural",
       "Historiografia, teoria y estetica":"Teoria e historiografia",
       "Discurso religioso y cientifico":"Historia intelectual"}
    return d.get(mt,"Critica e historia literaria")

def eje_alteridad(mt, t):
    tl=t.lower()
    if mt=="Mundo indigena": return ("Si","Etnico-racial (indigena)")
    if mt=="Afrodescendencia": return ("Si","Etnico-racial (afro)")
    if mt=="Genero y sexualidad": return ("Si","Genero y sexualidad")
    if mt=="Literatura latina en EE.UU.": return ("Si","Migratorio / diasporico")
    if "judia" in tl: return ("Si","Etnico-religioso (judia)")
    if "clase" in tl or "pobreza" in tl: return ("Si","Socioeconomico")
    return ("No","Ninguno")

PANOR_KEYS=("overview","history of","a history","the making of","panorama","toward a history",
            "the nature of","forms of","models","the making","introduction")
def formato_texto(tipo, tit):
    if tipo=="Documento" or tit.lower().startswith("document"): return "Documento primario"
    tl=tit.lower()
    for k in PANOR_KEYS:
        if k in tl: return "Panoramico / sintesis"
    return "Caso de estudio"

def siglo_foco(per):
    m={"Prehispanico":("Prehispanico",1),
       "Colonial":("Colonial",2),"Colonial/Independencia":("Colonial",2),"Colonial/s.XIX":("Colonial",2),
       "s.XIX":("Siglo XIX",3),"s.XIX-XX":("Siglos XIX-XX",3.5),
       "s.XX":("Siglo XX",4),"Contemporaneo":("Siglo XX",4),
       "s.XXI":("Siglo XXI",5),
       "Multiple":("Transversal",""),"N/A":("N/A","")}
    return m.get(per,("Otros",""))

def ambito_ling(reg):  # baja fiabilidad
    if "Brasil" in reg or reg=="Amazonia": return "Portugues (prob.)"
    if reg=="EE.UU." or "EE.UU." in reg: return "Ingles/Espanol (prob.)"
    if reg=="Europa": return "Frances/Espanol (prob.)"
    return "Espanol (prob.)"

rows = []
for (vol, parte, ptit, sec, stit, tipo, ncap, tit, autores, pag, reg, tema, per) in R:
    mr=macro_region(reg); mt=macro_tema(tema)
    alt,talt=eje_alteridad(mt,tema)
    sf,ord_=siglo_foco(per)
    rows.append({
        "Volumen": vol,
        "Volumen_titulo": VT[vol],
        "Parte": parte if parte else "",
        "Parte_titulo": ptit,
        "Seccion": sec if sec else "",
        "Seccion_titulo": stit,
        "Tipo": tipo,
        "N_capitulo": ncap,
        "Titulo": tit,
        "Autores": "; ".join(autores),
        "N_autores": len(autores),
        "Pagina": pag,
        "Region": reg,
        "Tema": tema,
        "Periodo": per,
        # --- nuevas etiquetas derivadas ---
        "Macro_region": mr,
        "Eje_Brasil": eje_brasil(reg),
        "Escala_geografica": escala_geografica(reg,tema,tit),
        "Macro_tema": mt,
        "Enfoque_disciplinar": enfoque_disciplinar(mt),
        "Eje_alteridad": alt,
        "Tipo_alteridad": talt,
        "Formato_texto": formato_texto(tipo,tit),
        "Siglo_foco": sf,
        "Periodo_ordinal": ord_,
        "N_autores_grupo": ("Individual" if len(autores)==1 else ("Coautoria (2-3)" if 2<=len(autores)<=3 else ("Colectivo (4+)" if len(autores)>=4 else "s/d"))),
        "Ambito_ling_prob": ambito_ling(reg),
    })

# CSV
import os
base = os.path.join(os.path.dirname(__file__), "..", "data")
with open(base+"/literary_cultures_db.csv","w",newline="",encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=COLS); w.writeheader()
    for r in rows: w.writerow(r)

with open(base+"/literary_cultures_db.json","w",encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)

# --- estadisticas rapidas ---
from collections import Counter
caps = [r for r in rows if r["Tipo"] in ("Capitulo","Documento")]
print("Total registros:", len(rows))
print("Capitulos+Documentos:", len(caps))
print("  - Capitulos:", sum(1 for r in rows if r["Tipo"]=="Capitulo"))
print("  - Documentos:", sum(1 for r in rows if r["Tipo"]=="Documento"))
print("  - Introducciones:", sum(1 for r in rows if r["Tipo"]=="Introduccion"))
print("Por volumen (caps+docs):", dict(Counter(r["Volumen"] for r in caps)))
print("\nTop regiones (caps+docs):")
for k,v in Counter(r["Region"] for r in caps).most_common(): print(f"   {v:3d}  {k}")
print("\nTop temas (caps+docs):")
for k,v in Counter(r["Tema"] for r in caps).most_common(15): print(f"   {v:3d}  {k}")
print("\nAutores mas frecuentes:")
allau=[]
for r in caps:
    if r["Autores"]:
        for a in r["Autores"].split("; "):
            if "incierto" not in a and "cortado" not in a: allau.append(a)
for k,v in Counter(allau).most_common(12): print(f"   {v:3d}  {k}")
print("\nArchivos: CSV y JSON escritos.")
