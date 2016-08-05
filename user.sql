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
-- Name: usuarios; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE usuarios (
    cuenta text,
    nombres text,
    apellidos text,
    pais text DEFAULT 'Venezuela'::text,
    ip_origen text,
    numero_accesos integer,
    cedula text,
    rif text,
    id integer NOT NULL,
    primer_acceso integer,
    ultimo_acceso integer,
    cuenta_twitter text,
    cuenta_facebook text,
    email text,
    foto text DEFAULT '/static/media/person.jpg'::text,
    genero text,
    followers integer DEFAULT 0,
    followings integer DEFAULT 0,
    ads integer DEFAULT 0,
    publications integer DEFAULT 0,
    direccion text,
    telefono text,
    estado integer DEFAULT 1,
    ciudad integer DEFAULT 0,
    es_empresa boolean DEFAULT false,
    nombre_empresa text,
    rif_empresa text,
    dir_empresa text,
    ci_nac character(1) DEFAULT 'V'::bpchar,
    rif_nac character(1) DEFAULT 'V'::bpchar,
    rif_empresa_nac character(1) DEFAULT 'J'::bpchar
);


ALTER TABLE public.usuarios OWNER TO vbravo;

--
-- Name: usuarios_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE usuarios_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.usuarios_id_seq OWNER TO vbravo;

--
-- Name: usuarios_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE usuarios_id_seq OWNED BY usuarios.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY usuarios ALTER COLUMN id SET DEFAULT nextval('usuarios_id_seq'::regclass);


--
-- Data for Name: usuarios; Type: TABLE DATA; Schema: public; Owner: vbravo
--

COPY usuarios (cuenta, nombres, apellidos, pais, ip_origen, numero_accesos, cedula, rif, id, primer_acceso, ultimo_acceso, cuenta_twitter, cuenta_facebook, email, foto, genero, followers, followings, ads, publications, direccion, telefono, estado, ciudad, es_empresa, nombre_empresa, rif_empresa, dir_empresa, ci_nac, rif_nac, rif_empresa_nac) FROM stdin;
lknolls	Lars	Knolls	1	127.0.0.1	\N	12797663	1210010	14	\N	\N	\N	\N	victorrbravo2@gmail.com	/static/media/person.jpg	Masculino	1	1	0	0	Av. Las Americas	2742401010	2	0	f	\N	\N	\N	V	V	J
slee	Steve	Lee	Venezuela	200.109.67.65	\N	323252	12797663	22	\N	\N	\N	\N	victorrbravo3@gmail.com	/static/media/person.jpg	Masculino	0	0	0	1	Av. Alberto Carnevalli.	584166740040	2	2778	f	\N	\N	\N	V	V	J
aaraujo	Antonio	Araujo	Venezuela	localhost	\N	12778889	232323	34	\N	\N	\N	\N	vbravo@cenditel.gob.ve	/static/media/antonio.jpg	Masculino	3	1	0	1	Av. Alberto Carnevalli	2742447430	2	3003	f	\N	\N	\N	V	V	J
mfedora	Mariana	Fedora	Venezuela	200.109.67.65	\N	20500100	34376734	42	\N	\N	\N	\N	victorrbravo4@gmail.com	/static/media/person.jpg	\N	0	0	0	0	\N	\N	6	3007	f	\N	\N	\N	V	V	J
slouis	Steve	Louis	Venezuela	200.109.67.65	\N	20100200	3434367	43	\N	\N	\N	\N	victorrbravo5@gmail.com	/static/media/person.jpg	Masculino	0	0	0	0	Av. Principal	2741010100	3	3004	f	\N	\N	\N	V	V	J
ssuarez	Sonia	Suarez	Venezuela	200.109.67.65	\N	20500200	34366	45	\N	\N	\N	\N	victorrbravo6@gmail.com	/static/media/person.jpg	Femenino	0	0	0	2	Av. Principal	2741010100	6	3007	f	\N	\N	\N	V	V	J
joe32	Joseph	Bakhos	Venezuela	201.242.85.179	\N	15148736	23232	70	\N	\N	\N	\N	josephbakhos2@hotmail.com	/static/media/person.jpg	\N	0	0	0	0	\N	\N	7	3008	f	\N	\N	\N	V	V	J
comprador	nuevo	comprador	Venezuela	\N	\N	\N	\N	13	\N	\N	\N	\N	info@weetup.com.ve	/static/media/nophoto_small.png	\N	0	0	0	0	\N	\N	8	0	f	\N	\N	\N	V	V	J
maria	Maria	SLeiman	Venezuela	201.242.85.179	\N	5539669	55396690	52	\N	\N	\N	\N	sleiman60@hotmail.com	/static/media/person.jpg	Femenino	1	3	0	2	Residencias el parque	4142393040	7	3008	f	\N	\N	\N	V	V	J
joe538	Joseph	Bakhos	Venezuela	201.242.85.179	\N	15148738	\N	73	\N	\N	\N	\N	aa@123.com	/static/media/person.jpg	\N	0	0	0	0	\N	\N	7	3008	f	\N	\N	\N	V	V	J
joe532	Joseph	Bakhos	Venezuela	201.242.85.179	\N	15148735	\N	72	\N	\N	\N	\N	josephbakhos3@hotmail.com	/static/media/person.jpg	\N	0	0	0	0	\N	\N	7	3008	f	\N	\N	\N	V	V	J
pflores	Patricia	Flores	Venezuela	200.109.67.65	\N	12100233	121002330	55	\N	\N	\N	\N	victorrbravo7@gmail.com	/static/media/person.jpg	Femenino	0	0	0	0	Av. Los Caobos	2741010100	8	3009	f	\N	\N	\N	V	V	J
willie	Willie	Zayas Esquivel	Venezuela	200.109.67.65	\N	1256334	21002320	63	\N	\N	\N	\N	victorrbravo8@gmail.com	/static/media/person.jpg	\N	0	0	0	0	\N	\N	6	3007	f	\N	\N	\N	V	V	J
selman	Selman	Bakhos	Venezuela	190.74.194.48	\N	11935339	\N	92	\N	\N	\N	\N	selmanbakos@hotmail.com	/static/media/person.jpg	\N	0	0	0	0	\N	\N	7	3008	f	\N	\N	\N	V	V	J
benbader	Ben	Bader	Venezuela	200.109.67.65	\N	12100200	\N	91	\N	\N	\N	\N	victorbravo@cantv.net	/static/media/person.jpg	\N	0	0	0	0	\N	\N	17	3018	f	\N	\N	\N	V	V	J
joseph	Joseph	Bakhos	Venezuela	201.209.237.97	\N	15148737	151487374	41	\N	\N	\N	\N	josephbakhos@hotmail.com	/static/media/person.jpg	Masculino	3	2	0	14	mhjghjg	4242748346	7	3008	f	\N	\N	\N	V	V	J
adri77	Adriana	Bakhos	Venezuela	190.72.151.241	\N	14610081	146100810	40	\N	\N	\N	\N	adrianabakhos4@gmail.com	/static/media/person.jpg	Femenino	2	1	0	1	Miranda	4242748346	7	3008	f	\N	\N	\N	V	V	J
solazver	Solazver	Sole	1	localhost	\N	12643114	12643114	10	\N	\N	\N	\N	solazver@gmail.com	/static/media/solazver.jpg	Femenino	3	3	0	7	Av. Alberto Carnevalli.	584166740040	15	3029	f	\N	\N	\N	V	V	J
vbravo	Víctor Rafael	Bravo Bravo	1	192.168.12.76	\N	12797664	12797664	6	\N	\N	\N	\N	victorrbravo@gmail.com	/static/media/VictorBravo.jpg	Masculino	3	5	0	53	Av. Alberto Carnevalli. Res. Terrazas de Campo Neblina	584166741838	14	3015	f	\N	\N	\N	V	V	J
\.


--
-- Name: usuarios_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vbravo
--

SELECT pg_catalog.setval('usuarios_id_seq', 93, true);


--
-- Name: El número de rif que ingreso ya existe.; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY usuarios
    ADD CONSTRAINT "El número de rif que ingreso ya existe." UNIQUE (rif_empresa);


--
-- Name: Ya existe el correo electrónico que ingresó. Utilice otro nom; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY usuarios
    ADD CONSTRAINT "Ya existe el correo electrónico que ingresó. Utilice otro nom" UNIQUE (email);


--
-- Name: cuenta_unica; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY usuarios
    ADD CONSTRAINT cuenta_unica UNIQUE (cuenta);


--
-- Name: usuarios_cedula_key; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY usuarios
    ADD CONSTRAINT usuarios_cedula_key UNIQUE (cedula);


--
-- Name: usuarios_pkey; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY usuarios
    ADD CONSTRAINT usuarios_pkey PRIMARY KEY (id);


--
-- Name: usuarios_rif_key; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY usuarios
    ADD CONSTRAINT usuarios_rif_key UNIQUE (rif);


--
-- Name: index_usuarios_cuenta; Type: INDEX; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE INDEX index_usuarios_cuenta ON usuarios USING btree (cuenta);


--
-- Name: index_usuarios_id; Type: INDEX; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE INDEX index_usuarios_id ON usuarios USING btree (id);


--
-- PostgreSQL database dump complete
--

