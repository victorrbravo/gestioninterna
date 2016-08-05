--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: publicaciones; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE publicaciones (
    type text DEFAULT 'Nuevo'::text,
    publishtime integer,
    changetime integer,
    priority text,
    owner text,
    reporter text,
    version text,
    status text DEFAULT 'Draft'::text,
    summary text,
    description text,
    keywords text,
    parenttask text,
    flowfilepath text,
    id integer NOT NULL,
    foto1 text DEFAULT '/static/media/nophoto_small.png'::text,
    foto2 text DEFAULT '/static/media/nophoto_small.png'::text,
    foto3 text DEFAULT '/static/media/nophoto_small.png'::text,
    foto4 text DEFAULT '/static/media/nophoto_small.png'::text,
    category integer,
    subcategory integer,
    price money DEFAULT 'Bs.0,00'::money,
    buyer text,
    score integer DEFAULT (-1),
    solddatetime integer DEFAULT 0,
    nosold boolean DEFAULT false,
    noscored boolean DEFAULT false,
    shippingtype text DEFAULT 'A convenir'::text,
    shipping_price money DEFAULT 'Bs.0,00'::money,
    number_products integer DEFAULT 0,
    detailsubcategory integer DEFAULT 0,
    last_notification_buyer integer DEFAULT 0,
    last_notification_seller integer DEFAULT 0,
    approved text,
    comments integer DEFAULT 0,
    buyeremail text,
    buyerphone text,
    buyeraddress text,
    ciudad text,
    detalle_marca text DEFAULT ''::text,
    detalle_color text DEFAULT ''::text,
    detalle_pantalla text DEFAULT ''::text,
    detalle_procesador text DEFAULT ''::text,
    detalle_tipo text DEFAULT ''::text,
    detalle_capacidad text DEFAULT ''::text,
    detalle_modelo text,
    detalle_raza text DEFAULT ''::text,
    detalle_subtipo text DEFAULT ''::text,
    detalle_tamano text DEFAULT ''::text,
    detalle_serie text DEFAULT ''::text,
    detalle_objeto text DEFAULT ''::text
);


ALTER TABLE public.publicaciones OWNER TO vbravo;

--
-- Name: publicaciones_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE publicaciones_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.publicaciones_id_seq OWNER TO vbravo;

--
-- Name: publicaciones_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE publicaciones_id_seq OWNED BY publicaciones.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY publicaciones ALTER COLUMN id SET DEFAULT nextval('publicaciones_id_seq'::regclass);


--
-- Data for Name: publicaciones; Type: TABLE DATA; Schema: public; Owner: vbravo
--

COPY publicaciones (type, publishtime, changetime, priority, owner, reporter, version, status, summary, description, keywords, parenttask, flowfilepath, id, foto1, foto2, foto3, foto4, category, subcategory, price, buyer, score, solddatetime, nosold, noscored, shippingtype, shipping_price, number_products, detailsubcategory, last_notification_buyer, last_notification_seller, approved, comments, buyeremail, buyerphone, buyeraddress, ciudad, detalle_marca, detalle_color, detalle_pantalla, detalle_procesador, detalle_tipo, detalle_capacidad, detalle_modelo, detalle_raza, detalle_subtipo, detalle_tamano, detalle_serie, detalle_objeto) FROM stdin;
Nuevo	1438119953	\N	\N	solazver	\N	\N	Sold	Tremenda playera o camisa con la mejor calidad	<p>Lo mejor de la playera</p>	\N	\N	\N	30	/static/media/sh1.png	\N	\N	\N	9	17	Bs.24.000,00	vbravo	-1	1438288398	f	f	A convenir	Bs.0,00	0	0	\N	\N	vbravo	0	\N	\N	\N	Bolívar							\N					
Nuevo	1428441630	\N	\N	vbravo	\N	\N	Sold	Audífonos Beats	<p>Geniales audifonos</p>	\N	\N	\N	26	/static/media/audifono.jpg	\N	\N	\N	2	19	Bs.30.000,00	jbakhos	2	\N	f	f	A convenir	Bs.0,00	0	0	\N	\N	vbravo	0	\N	\N	\N	Mérida							\N					
Nuevo	1441058533	\N	\N	ssuarez	\N	\N	Sold	Computadora nueva de paquete i7	\N	\N	\N	\N	117	/static/media/compu2.jpg	/static/media/compu3.jpg	/static/media/nophoto_small.png	/static/media/nophoto_small.png	8	81	Bs.560.000,00	vbravo	-1	1441122813	f	f	A convenir	Bs.0,00	1	0	\N	\N	vbravo	0	\N	\N	\N	\N							\N					
Nuevo	1438120997	\N	\N	slee	\N	\N	Sold	Tremenda *Tabletas	<p>Muy Buena tableta</p>	\N	\N	\N	50	/static/media/tabla2.jpg	/static/media/tabla3.jpg	/static/media/tabla4.jpg	/static/media/tabletawindow.jpg	1	8	Bs.52.000,00	vbravo	2	1438121005	f	f	A convenir	Bs.0,00	0	0	\N	\N	vbravo	0	\N	\N	\N	\N							\N					
Nuevo	1429326936	\N	\N	solazver	\N	\N	Sold	Pulsera	<p>Pulsera</p>	\N	\N	\N	29	/static/media/pulsera.jpg	\N	\N	\N	9	18	Bs.5.000,00	vbravo	2	1434663456	f	t	A convenir	Bs.0,00	0	0	\N	\N	vbravo	0	\N	\N	\N	Bolívar							\N					
Nuevo	1438122300	\N	\N	solazver	\N	\N	Sold	Excelente <a href=/gopanel/Published/17/Camisas > Camisas </a> resistentes y de amplios colores	<p>Camisas en todos los tama	\N	\N	\N	71	/static/media/franela4.jpg	/static/media/franela3.jpg	/static/media/franela2.jpg	/static/media/franela1.jpg	9	17	Bs.12.000,00	vbravo	-1	1438726032	f	f	A convenir	Bs.0,00	0	0	\N	\N	vbravo	0	\N	\N	\N	Bolívar							\N					
Usado	1439333997	\N	\N	adri77	\N	\N	Sold	vendo <a href='/gopanel/Published/23/Computadora' > Computadora </a> Escritorio marca Lenovo	\N	\N	\N	\N	93	/static/media/nophoto_small.png	/static/media/nophoto_small.png	/static/media/nophoto_small.png	/static/media/nophoto_small.png	10	23	Bs.35.000,00	joseph	2	1439657172	f	f	A convenir	Bs.0,00	1	0	\N	\N	vbravo	0	\N	\N	\N	\N							\N					
Nuevo	1441058536	\N	\N	ssuarez	\N	\N	Sold	Tremenda computadora	\N	\N	\N	\N	116	/static/media/compu2.jpg	/static/media/compu3.jpg	/static/media/compu4.jpg	/static/media/nophoto_small.png	8	81	Bs.350.000,00	joseph	-1	1443059958	f	f	A convenir	Bs.0,00	1	0	77	78	vbravo	0	\N	\N	\N	\N							\N					
Nuevo	1441927213	\N	\N	maria	\N	\N	Sold	Engrapadora Marca Eagle	\N	\N	\N	\N	118	/static/media/nophoto_small.png	/static/media/nophoto_small.png	/static/media/nophoto_small.png	/static/media/nophoto_small.png	15	215	Bs.1.500,00	joseph	1	1442607382	f	f	A convenir	Bs.0,00	1	668	57	58	vbravo	2	\N	\N	\N	\N							\N					
Usado	1444942357	\N	\N	aaraujo	\N	\N	Published	Super multifuerza de gran impacto	\N	\N	\N	\N	128	/static/media/multifuerza1.jpg	/static/media/multifuerza2.jpg	/static/media/multifuerza3.jpg	/static/media/multifuerza4.jpg	10	288	Bs.250.000,00	aaraujo	-1	0	f	f	A convenir	Bs.0,00	1	507	0	0	aaraujo	3	\N	\N	\N	\N							\N					
Nuevo	1440588850	\N	\N	joseph	\N	\N	Sold	Pendrive kingston de 32gb - Sellados	\N	\N	\N	\N	114	/static/media/dtse9h.jpg	/static/media/nophoto_small.png	/static/media/nophoto_small.png	/static/media/nophoto_small.png	8	281	Bs.7.500,00	maria	-1	1442607943	f	f	A convenir	Bs.0,00	1	301	59	60	vbravo	0	\N	\N	\N	Caracas							\N					
Nuevo	1440030858	\N	\N	joseph	\N	\N	Published	Pendrive Kingstong de 32 gb Nuevos sellados	\N	\N	\N	\N	100	/static/media/nophoto_small.png	/static/media/nophoto_small.png	/static/media/nophoto_small.png	/static/media/nophoto_small.png	8	281	Bs.5.000,00	vbravo	-1	0	f	f	A convenir	Bs.0,00	1	0	\N	\N	vbravo	1	\N	\N	\N	Caracas							\N					
Usado	1446340324	\N	\N	joseph	\N	\N	Sold	Vendo moto como nueva poco kilometraje	\N	\N	\N	\N	130	/static/media/bici1.jpg	/static/media/bici2.jpg	/static/media/bici3.jpg	/static/media/nophoto_small.png	23	\N	Bs.50.000,00	maria	-1	1450457322	f	f	A convenir	Bs.0,00	1	0	221	222	joseph	3	sleiman60@hotmail.com	4142393040	Residencias el parque	Caracas							\N					
Nuevo	1440449786	\N	\N	solazver	\N	\N	Sold	Nuevo Pendrive 128Gb	\N	\N	\N	\N	113	/static/media/pendrive1.jpg	/static/media/pendrive2.jpg	/static/media/pendrive3.jpg	/static/media/pendrive4.jpg	8	281	Bs.54.000,00	vbravo	-1	1440449820	f	f	A convenir	Bs.0,00	1	0	\N	\N	vbravo	0	\N	\N	\N	Bolívar							\N					
Nuevo	1439472923	\N	\N	solazver	\N	\N	Sold	Nuevo <a href='/gopanel/Published/25/Multifuerza' > Multifuerza </a> rin 10	\N	\N	\N	\N	95	/static/media/multifuerza1.jpg	/static/media/multifuerza2.jpg	/static/media/multifuerza3.jpg	/static/media/multifuerza4.jpg	3	25	Bs.67.000,00	vbravo	-1	1442031120	f	f	A convenir	Bs.0,00	1	0	\N	\N	vbravo	0	\N	\N	\N	Bolívar							\N					
Nuevo	1443650190	\N	\N	maria	\N	\N	Sold	Cupecakes decorados por docenas	\N	\N	\N	\N	124	/static/media/nophoto_small.png	/static/media/nophoto_small.png	/static/media/nophoto_small.png	/static/media/nophoto_small.png	29	\N	Bs.600,00	joseph	-1	1455108509	f	f	A convenir	Bs.0,00	1	0	237	238	joseph	1	josephbakhos@hotmail.com	4242748346	mhjghjg	\N							\N					
Nuevo	1445454740	\N	\N	vbravo	\N	\N	Sold	Blackberry Celular Q10	\N	\N	\N	\N	129	/static/media/celuar.jpg	/static/media/celular1.jpg	/static/media/celular2.jpg	/static/media/celular3.jpg	6	255	Bs.129.000,00	joseph	0	1445956001	f	f	A convenir	Bs.0,00	1	144	204	205	vbravo	0	josephbakhos@hotmail.com	4242748346	mhjghjg	Mérida							\N					
Nuevo	1446218925	\N	\N	vbravo	\N	\N	Sold	Kindle último Gran modelo Teléfono listo	<p>Lector de <strong>libros</strong> y tableta. Genial<img alt="" src="http://www.eltiempo.com/contenido/bogota/IMAGEN/IMAGEN-16418735-1.png" style="height:273px; width:546px" /></p> <p>	\N	\N	\N	18	/static/media/kindle.jpg	\N	\N	\N	8	89	Bs.20.000,00	joseph	-1	1448456132	f	f	A convenir	Bs.0,00	1	362	209	210	vbravo	0	josephbakhos@hotmail.com	4242748346	mhjghjg	Mérida							\N					
Nuevo	1449696185	\N	\N	joseph	\N	\N	Sold	Vendo moto marca yamaha 400hp	\N	\N	\N	\N	131	/static/media/Chrysanthemum.jpg	/static/media/nophoto_small.png	/static/media/nophoto_small.png	/static/media/nophoto_small.png	11	125	Bs.0,00	maria	-1	1449696426	f	f	A convenir	Bs.0,00	1	532	219	220	joseph	1	sleiman60@hotmail.com	4142393040	Residencias el parque	Caracas							\N					
Nuevo	1453908884	\N	\N	joseph	\N	\N	Published	Cupcake para fiestas y eventos	\N	\N	\N	\N	138	/static/media/strawberry-lemonade-cupcake2.jpg	/static/media/nophoto_small.png	/static/media/nophoto_small.png	/static/media/nophoto_small.png	29	\N	Bs.85,00	vbravo	-1	0	f	f	A convenir	Bs.0,00	50	0	0	0	vbravo	0	\N	\N	\N	Caracas							\N					
Nuevo	1454441117	\N	\N	joseph	\N	\N	Published	Vendo televisor LED marca Samsung 32 nuevo en su caja	\N	\N	\N	\N	135	/static/media/TV-SAMSUNG-32UN4003.jpg	/static/media/nophoto_small.png	/static/media/nophoto_small.png	/static/media/nophoto_small.png	12	177	Bs.147.000,00	vbravo	-1	0	f	f	A convenir	Bs.0,00	1	0	0	0	vbravo	0	\N	\N	\N	Caracas							\N					
Nuevo	1438097712	\N	\N	vbravo	\N	\N	Sold	Tremendo Bolso extragrande para laptop	<p>Verlo es <em>comprar</em> este bolso de gran tama</p>	\N	\N	\N	23	/static/media/bolso.jpg	\N	\N	\N	9	16	Bs.14.000,00	jbakhos	-1	1439301915	f	f	A convenir	Bs.2.000,00	5	0	\N	\N	vbravo	0	\N	\N	\N	Mérida							\N					
Nuevo	1441033689	\N	\N	vbravo	\N	\N	Sold	Gran computadora de escritorio 21 pulgadas	\N	\N	\N	\N	115	/static/media/compu1.jpg	/static/media/compu2.jpg	/static/media/compu3.jpg	/static/media/nophoto_small.png	8	81	Bs.230.000,00	ssuarez	-1	1441124666	f	f	A convenir	Bs.0,00	1	0	\N	\N	vbravo	0	\N	\N	\N	Mérida							\N					
Nuevo	1436459244	\N	\N	vbravo	\N	\N	Sold	Vendo <a href=/gopanel/Published/24/Bicicleta > Bicicleta </a> de grandes prestaciones	\N	\N	\N	\N	68	/static/media/bici1.jpg	/static/media/bici2.jpg	/static/media/bici3.jpg	/static/media/bici4.jpg	7	24	Bs.0,00	solazver	2	\N	f	f	A convenir	Bs.0,00	0	0	\N	\N	vbravo	0	\N	\N	\N	Mérida							\N					
Usado	1427810389	\N	\N	vbravo	\N	\N	Sold	Carro Clío 2006 en perfectas condiciones	<p>Excelente <em>Vehiculo para marcha</em></p>	\N	\N	\N	17	/static/media/clio2.jpg	\N	\N	\N	7	6	Bs.450.000,00	aaraujo	2	\N	f	f	A convenir	Bs.0,00	0	0	\N	\N	vbravo	0	\N	\N	\N	Mérida							\N					
Nuevo	1440173039	\N	\N	vbravo	\N	\N	Sold	Camisa muy bonita	\N	\N	\N	\N	104	/static/media/sh1.png	/static/media/sh1_tb.png	/static/media/sh.png	/static/media/sh_tb.png	5	60	Bs.2.000,00	ssuarez	-1	1441124808	f	f	A convenir	Bs.0,00	1	107	\N	\N	vbravo	0	\N	\N	\N	Mérida							\N					
Nuevo	1434385631	\N	\N	vbravo	\N	\N	Sold	Tremenda <a href= /gopanel/Published/24/Bicicleta >Bicicleta</a> rin 20 grande	\N	\N	\N	\N	60	/static/media/bici1.jpg	/static/media/bici2.jpg	/static/media/bici3.jpg	/static/media/bici4.jpg	7	24	Bs.27.000,00	aadeva	-1	1439240383	f	f	A convenir	Bs.0,00	0	0	\N	\N	vbravo	0	\N	\N	\N	Mérida							\N					
Usado	1440172775	\N	\N	vbravo	\N	\N	Published	Nuevo Multifuerza	\N	\N	\N	\N	103	/static/media/multifuerza1_tb.jpg	/static/media/multifuerza2.jpg	/static/media/multifuerza2_tb.jpg	/static/media/multifuerza3.jpg	10	288	Bs.60.000,00	vbravo	-1	0	f	f	A convenir	Bs.0,00	1	0	\N	\N	vbravo	0	\N	\N	\N	Mérida							\N					
Nuevo	1438097604	\N	\N	vbravo	\N	\N	Sold	Tremenda <a href= /gopanel/Published/8/Tabletas >Tabletas</a> grande 10 pulgadas Marca Samsung	\N	\N	\N	\N	61	/static/media/tabla2.jpg	/static/media/tabla3.jpg	/static/media/tabla4.jpg	/static/media/raspberrypi.jpg	1	8	Bs.0,00	aadeva	-1	1439256906	f	f	A convenir	Bs.2.000,00	2	0	\N	\N	vbravo	0	\N	\N	\N	Mérida							\N					
Nuevo	1439304620	\N	\N	vbravo	\N	\N	Sold	Tremendo *Televisores pantalla grande	<p>Un gran TV cómo usted lo quería</p>	\N	\N	\N	38	/static/media/tv.jpg	\N	\N	\N	2	11	Bs.52.000,00	aadeva	-1	1439328786	f	f	A convenir	Bs.0,00	0	0	\N	\N	vbravo	0	\N	\N	\N	Mérida							\N					
Nuevo	1440173251	\N	\N	vbravo	\N	\N	Sold	Nueva camisa	\N	\N	\N	\N	105	/static/media/franela1.jpg	/static/media/franela2.jpg	/static/media/franela3.jpg	/static/media/franela4.jpg	21	252	Bs.2.000,00	joseph	2	1440589409	f	f	A convenir	Bs.0,00	2	798	\N	\N	vbravo	0	\N	\N	\N	Mérida							\N					
Nuevo	1443559468	\N	\N	vbravo	\N	\N	Published	Cable especializado coaxial tipo 2 tamaño	<p><em>Tremendo</em> cable para todo tipo tamaño de gran prestación</p>	\N	\N	\N	123	/static/media/cable1.jpg	/static/media/cable2.jpg	/static/media/cable3.jpg	/static/media/nophoto_small.png	8	87	Bs.1.500,00	solazver	-1	0	f	f	A convenir	Bs.0,00	1	0	0	0	solazver	0	\N	\N	\N	Mérida							\N					
Usado	1440175387	\N	\N	vbravo	\N	\N	Sold	Tremendo Mueble	\N	\N	\N	\N	109	/static/media/mueble1.jpg	/static/media/mueble2.jpg	/static/media/mueble3.jpg	/static/media/mueble4.jpg	14	199	Bs.240.000,00	aaraujo	-1	1442031397	f	f	A convenir	Bs.0,00	1	613	\N	\N	vbravo	0	\N	\N	\N	Mérida							\N					
Nuevo	1443720929	\N	\N	vbravo	\N	\N	Sold	Nuevo bolso marca miracase	\N	\N	\N	\N	125	/static/media/bolso1.jpg	/static/media/bolso2.jpg	/static/media/bolso3.jpg	/static/media/bolso4.jpg	8	79	Bs.23.290,00	aaraujo	-1	1444921884	f	f	A convenir	Bs.0,00	1	229	183	184	vbravo	1	\N	\N	\N	Mérida							\N					
Nuevo	1443203881	\N	\N	vbravo	\N	\N	Published	Tremendo teléfono iphone 6s	<p>Compre este <strong>IPHONE. </strong>Aproveche esta oferta. No te la puedes perder.</p> <p>Un gran telefono</p> <p>Grande</p> <p>	\N	\N	\N	121	/static/media/tlf3.jpg	/static/media/tlf2.jpg	/static/media/tlf1.jpg	/static/media/nophoto_small.png	6	255	Bs.250.000,00	vbravo	-1	0	f	f	A convenir	Bs.0,00	1	149	0	0	vbravo	0	\N	\N	\N	Mérida							\N					
Nuevo	1444940760	\N	\N	vbravo	\N	\N	Sold	Franela de talla única	<p>Camisas en todos los <strong>colores</strong>, de tama</p>	\N	\N	\N	122	/static/media/franela1.jpg	/static/media/franela2.jpg	/static/media/franela3.jpg	/static/media/franela4.jpg	21	252	Bs.10.000,00	aaraujo	-1	1444940949	f	f	Gratis	Bs.0,00	2	0	191	192	vbravo	0	vbravo@cenditel.gob.ve	2742447261	Av. Alberto Carnevalli	Mérida							\N					
Usado	1446218779	\N	\N	vbravo	\N	\N	Sold	Tremenda Computadora i5 1TB	<p>Hola<img alt="" src="/static/media/bici5_tb.jpg" style="height:64px; width:64px" />que tal</p>	\N	\N	\N	97	/static/media/tabla4.jpg	/static/media/tabla3.jpg	/static/media/tabla2.jpg	/static/media/nophoto_small.png	8	81	Bs.320.000,00	joseph	-1	1448588410	f	f	A convenir	Bs.0,00	1	257	211	212	vbravo	0	josephbakhos@hotmail.com	4242748346	mhjghjg	Mérida							\N					
Nuevo	1438722489	\N	\N	solazver	\N	\N	Sold	Chemise grande	<p>Gran Chamise</p>	\N	\N	\N	72	/static/media/franela1.jpg	/static/media/nophoto_small.png	/static/media/nophoto_small.png	/static/media/nophoto_small.png	9	17	Bs.17.000,00	vbravo	-1	1438791464	f	f	A convenir	Bs.0,00	0	0	\N	\N	vbravo	0	\N	\N	\N	Bolívar							\N					
Nuevo	1438120621	\N	\N	solazver	\N	\N	Sold	Tremendo <a href=/gopanel/Published/25/Multifuerza > Multifuerza </a> de 30 kilos	\N	\N	\N	\N	69	/static/media/multifuerza1.jpg	/static/media/multifuerza2.jpg	/static/media/multifuerza3.jpg	/static/media/multifuerza4.jpg	3	25	Bs.180.000,00	aadeva	2	1439256467	f	f	A convenir	Bs.0,00	1	0	\N	\N	vbravo	0	\N	\N	\N	Bolívar							\N					
Nuevo	1453908886	\N	\N	joseph	\N	\N	Published	Tablet Samsung Galaxy Tab 3	\N	\N	\N	\N	139	/static/media/Galaxy-Tab-3.jpg	/static/media/nophoto_small.png	/static/media/nophoto_small.png	/static/media/nophoto_small.png	8	89	Bs.75.000,00	vbravo	-1	0	f	f	A convenir	Bs.0,00	1	362	0	0	vbravo	0	\N	\N	\N	Caracas							\N					
Usado	1454441111	\N	\N	joseph	\N	\N	Published	Samsung Galaxy S3 Mini	\N	\N	\N	\N	137	/static/media/s3mini.jpeg	/static/media/nophoto_small.png	/static/media/nophoto_small.png	/static/media/nophoto_small.png	6	255	Bs.100.000,00	vbravo	-1	0	f	f	A convenir	Bs.0,00	1	156	0	0	vbravo	0	\N	\N	\N	Caracas							\N					
Usado	1444080040	\N	\N	vbravo	\N	\N	Published	Mueble de extraordinario tamaño	\N	\N	\N	\N	127	/static/media/mueble1.jpg	/static/media/mueble2.jpg	/static/media/mueble3.jpg	/static/media/mueble4.jpg	14	199	Bs.250.000,00	vbravo	127	0	f	f	A convenir	Bs.0,00	1	613	0	0	vbravo	9	\N	\N	\N	Mérida							\N					
Nuevo	1440448221	\N	\N	solazver	\N	\N	Sold	Vendo Pendrive de 16Gb marca wau	\N	\N	\N	\N	110	/static/media/pendrive1.jpg	/static/media/pendrive2.jpg	/static/media/pendrive3.jpg	/static/media/pendrive4.jpg	8	281	Bs.6.000,00	vbravo	-1	1458774945	f	f	A convenir	Bs.0,00	1	302	245	246	vbravo	0	victorrbravo@gmail.com	584166741838	Av. Alberto Carnevalli. Res. Terrazas de Campo Neblina	Bolívar							\N					
Usado	1467369705	\N	\N	joseph	\N	\N	Published	Vendo bicicleta marca Giant Reve1 como nueva	\N	\N	\N	\N	140	/static/media/nophoto_small.png	/static/media/nophoto_small.png	/static/media/nophoto_small.png	/static/media/nophoto_small.png	10	273	Bs.150.000,00	joseph	-1	0	f	f	A convenir	Bs.0,00	1	0	0	0	joseph	0	\N	\N	\N	\N							\N					
Nuevo	1467369707	\N	\N	joseph	\N	\N	Published	Patineta Electrica, Scooter, Monociclo Tipo Io Hawk	\N	\N	\N	\N	136	/static/media/patineta-electrica-scooter-monociclo-tipo-io-hawk-278301-MLM20317166352_062015-F.jpg	/static/media/nophoto_small.png	/static/media/nophoto_small.png	/static/media/nophoto_small.png	10	118	Bs.50.000,00	joseph	-1	0	f	f	A convenir	Bs.0,00	10	0	0	0	joseph	0	\N	\N	\N	Caracas							\N					
Nuevo	1443059929	\N	\N	joseph	\N	\N	Sold	Vendo computadora marca dell core 3 duo	\N	\N	\N	\N	119	/static/media/computadora.jpg	/static/media/Facebook_icon-1024x1024.jpg	/static/media/nophoto_small.png	/static/media/nophoto_small.png	8	81	Bs.50.000,00	vbravo	-1	1462399301	f	f	A convenir	Bs.0,00	1	0	251	252	vbravo	1	victorrbravo@gmail.com	584166741838	Av. Alberto Carnevalli. Res. Terrazas de Campo Neblina	Caracas							\N					
Nuevo	1452275480	\N	\N	joseph	\N	\N	Sold	Prueba de publicacion test.	<p>Prueba de publicacion test.</p>	\N	\N	\N	133	/static/media/donamagica.png	/static/media/_30aLrIR.png	/static/media/jh0euMWn.png	/static/media/nophoto_small.png	2	28	Bs.200,00	vbravo	-1	1462399777	f	f	Fijo	Bs.100,00	1	708	253	254	vbravo	1	victorrbravo@gmail.com	584166741838	Av. Alberto Carnevalli. Res. Terrazas de Campo Neblina	Caracas							\N					
Nuevo	1464012754	\N	\N	vbravo	\N	\N	Published	Tremendo Pendrive de 8Gb	\N	\N	\N	\N	101	/static/media/pendrive1.jpg	/static/media/pendrive2.jpg	/static/media/pendrive3.jpg	/static/media/pendrive4.jpg	8	281	Bs.24.000,00	vbravo	-1	1443453393	f	f	A convenir	Bs.0,00	1	303	93	94	vbravo	0	\N	\N	\N	Mérida							\N					
Nuevo	1458307910	\N	\N	vbravo	\N	\N	Published	Pendrive marca ZIP de 32 GB	<p>Tremendo <strong>Pendrive</strong> vea los <em>datos</em>:</p><p>Gran Pendrive</p><p>de tamaño especial</p>	\N	\N	\N	143	/static/media/pendrive4.jpg	/static/media/nophoto_small.png	/static/media/nophoto_small.png	/static/media/nophoto_small.png	8	281	Bs.800,00	vbravo	-1	0	f	f	A convenir	Bs.0,00	1	301	0	0	vbravo	5	\N	\N	\N	Mérida							\N					
Nuevo	1464021380	\N	\N	vbravo	\N	\N	Published	Pendrive de 8Gb Blanco	<p>Muy buen pendrive, para la fuente.	\N	\N	\N	144	/static/media/pendrive4.jpg	/static/media/nophoto_small.png	/static/media/nophoto_small.png	/static/media/nophoto_small.png	8	281	Bs.27.000,00	vbravo	-1	0	f	f	A convenir	Bs.0,00	1	303	0	0	vbravo	0	\N	\N	\N	\N							\N					
Nuevo	1440448887	\N	\N	solazver	\N	\N	Published	Tremendo Pendrive de 32Gb	\N	\N	\N	\N	112	/static/media/pendrive1.jpg	/static/media/pendrive2.jpg	/static/media/pendrive3.jpg	/static/media/pendrive4.jpg	8	281	Bs.15.000,00	vbravo	-1	1440448980	f	f	A convenir	Bs.0,00	1	301	\N	\N	vbravo	1	\N	\N	\N	Bolívar							\N					
Nuevo	1467212078	\N	\N	vbravo	\N	\N	Published	Nuevo Mono de bebé muy duradero	\N	\N	\N	\N	167	/static/media/ropabebe3.jpg	/static/media/ropabebe2.jpg	/static/media/nophoto_small.png	/static/media/nophoto_small.png	21	360	Bs.30.000,00	vbravo	-1	0	f	f	A convenir	Bs.0,00	1	0	0	0	vbravo	0	\N	\N	\N	\N					Mangas Cortas		\N					
Nuevo	1464806869	\N	\N	vbravo	\N	\N	Published	Tremendo Computador Laptop de Gran medida	\N	\N	\N	\N	142	/static/media/laptop1.jpg	/static/media/nophoto_small.png	/static/media/nophoto_small.png	/static/media/nophoto_small.png	8	264	Bs.500.000,00	vbravo	-1	0	f	f	Gratis	Bs.0,00	1	279	0	0	vbravo	0	\N	\N	\N	Mérida						16GB	\N					
Nuevo	1467369688	\N	\N	vbravo	\N	\N	Published	Mono de bebé tipo manga corta	\N	\N	\N	\N	166	/static/media/ropabebe1.jpg	/static/media/ropabebe2.jpg	/static/media/nophoto_small.png	/static/media/nophoto_small.png	21	360	Bs.52.000,00	joseph	-1	0	f	f	A convenir	Bs.0,00	1	0	0	0	joseph	0	\N	\N	\N	\N	Shur				Mangas Largas		\N					
Usado	1467369694	\N	\N	vbravo	\N	\N	Published	Tremendo Laptop casi como nuevo i5	\N	\N	\N	\N	157	/static/media/laptop1.jpg	/static/media/nophoto_small.png	/static/media/nophoto_small.png	/static/media/nophoto_small.png	8	264	Bs.450.000,00	joseph	-1	0	f	f	A convenir	Bs.0,00	1	0	0	0	joseph	0	\N	\N	\N	\N	Acer	Verde	15.3 pulgadas	i5			\N					
Usado	1467369702	\N	\N	joseph	\N	\N	Published	Vendo bicicleta marca Giant Reve1 como nueva	\N	\N	\N	\N	141	/static/media/nophoto_small.png	/static/media/nophoto_small.png	/static/media/nophoto_small.png	/static/media/nophoto_small.png	10	273	Bs.150.000,00	joseph	-1	0	f	f	A convenir	Bs.0,00	1	0	0	0	joseph	0	\N	\N	\N	\N							\N					
Nuevo	1467369710	\N	\N	joseph	\N	\N	Published	Prueba de publicidad error 500	\N	\N	\N	\N	132	/static/media/donamagica.png	/static/media/nophoto_small.png	/static/media/nophoto_small.png	/static/media/nophoto_small.png	2	276	Bs.200,00	joseph	-1	0	f	f	A convenir	Bs.0,00	1	1	0	0	joseph	0	\N	\N	\N	Caracas							\N					
Nuevo	1467386121	\N	\N	vbravo	\N	\N	Draft	Otro Teléfono fijo de grandes prestaciones	\N	\N	\N	\N	175	/static/media/telephone3.jpg	/static/media/telephone2.jpg	/static/media/nophoto_small.png	/static/media/nophoto_small.png	6	66	Bs.85.000,00	\N	-1	0	f	f	A convenir	Bs.0,00	1	0	0	0	\N	0	\N	\N	\N	\N							\N					Teléfonos Fijos
Nuevo	1467386074	\N	\N	vbravo	\N	\N	Draft	Nuevo Telefono fijo de grandes prestaciones	\N	\N	\N	\N	174	/static/media/telephone2.jpg	/static/media/telephone3.jpg	/static/media/nophoto_small.png	/static/media/nophoto_small.png	6	66	Bs.32.000,00	\N	-1	0	f	f	A convenir	Bs.0,00	1	0	0	0	\N	0	\N	\N	\N	\N							\N					Teléfonos Fijos
Nuevo	1467215078	\N	\N	vbravo	\N	\N	Published	Nuevo Laptop Dell	\N	\N	\N	\N	170	/static/media/laptop4.jpg	/static/media/nophoto_small.png	/static/media/nophoto_small.png	/static/media/nophoto_small.png	8	264	Bs.350.000,00	vbravo	-1	0	f	f	A convenir	Bs.0,00	1	0	0	0	vbravo	0	\N	\N	\N	\N	Dell		14 a 14,9	Intel Core i5		4GB	x2000					
Nuevo	1467327671	\N	\N	vbravo	\N	\N	Published	Nuevo laptop i7 16GB	\N	\N	\N	\N	172	/static/media/laptop4.jpg	/static/media/laptop3.jpg	/static/media/nophoto_small.png	/static/media/nophoto_small.png	8	264	Bs.520.000,00	vbravo	-1	0	f	f	A convenir	Bs.0,00	1	0	0	0	vbravo	0	\N	\N	\N	\N	Asus		15 a 15,9	Intel Core i7		16GB	x2500					
Nuevo	1467369683	\N	\N	vbravo	\N	\N	Published	Nuevo Laptop Dell 1	\N	\N	\N	\N	169	/static/media/laptop4.jpg	/static/media/nophoto_small.png	/static/media/nophoto_small.png	/static/media/nophoto_small.png	8	264	Bs.350.000,00	joseph	-1	0	f	f	A convenir	Bs.0,00	1	0	0	0	joseph	0	\N	\N	\N	\N	Dell		4GB	Intel Core i5		8GB	Aspire					
Nuevo	1465310423	\N	\N	vbravo	\N	\N	Published	Un tremendo laptop del 7 de junio	\N	\N	\N	\N	158	/static/media/laptop1.jpg	/static/media/laptop2.jpg	/static/media/laptop3.jpg	/static/media/laptop4.jpg	8	264	Bs.220.000,00	vbravo	-1	0	f	f	Gratis	Bs.0,00	1	0	0	0	vbravo	0	\N	\N	\N	\N	Acer		14 pulgadas	i5		8GB	x2000					
Nuevo	1467215073	\N	\N	vbravo	\N	\N	Published	Otro Dell de grandes prestaciones	\N	\N	\N	\N	171	/static/media/laptop3.jpg	/static/media/nophoto_small.png	/static/media/nophoto_small.png	/static/media/nophoto_small.png	8	264	Bs.600.000,00	vbravo	-1	0	f	f	A convenir	Bs.0,00	1	0	0	0	vbravo	0	\N	\N	\N	\N	Dell		15 a 15,9	Intel Core i7		8GB	x2500					
Nuevo	1465349534	\N	\N	solazver	\N	\N	Published	Tremendo Laptop Acer de alta capacidad	\N	\N	\N	\N	162	/static/media/laptop1.jpg	/static/media/nophoto_small.png	/static/media/nophoto_small.png	/static/media/nophoto_small.png	8	264	Bs.120.000,00	solazver	-1	0	f	f	Gratis	Bs.0,00	1	0	0	0	solazver	0	\N	\N	\N	\N	Acer		14 pulgadas	i5			x2500					
Usado	1467369691	\N	\N	vbravo	\N	\N	Published	Tremendo laptop de segunda mano 7 de junio	\N	\N	\N	\N	161	/static/media/laptop1.jpg	/static/media/laptop2.jpg	/static/media/laptop3.jpg	/static/media/nophoto_small.png	8	264	Bs.230.000,00	joseph	-1	0	f	f	Gratis	Bs.0,00	1	0	0	0	joseph	0	\N	\N	\N	\N	Lenovo		14 pulgadas	i5		8GB	Aspire					
\.


--
-- Name: publicaciones_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vbravo
--

SELECT pg_catalog.setval('publicaciones_id_seq', 175, true);


--
-- Name: publicaciones_pkey; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY publicaciones
    ADD CONSTRAINT publicaciones_pkey PRIMARY KEY (id);


--
-- Name: index_publicaciones_id; Type: INDEX; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE INDEX index_publicaciones_id ON publicaciones USING btree (id);


--
-- Name: chequeo_usuarios; Type: FK CONSTRAINT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY publicaciones
    ADD CONSTRAINT chequeo_usuarios FOREIGN KEY (owner) REFERENCES usuarios(cuenta) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

