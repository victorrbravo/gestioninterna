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
-- Name: publications_log; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE publications_log (
    id integer NOT NULL,
    publicaciones_id integer,
    status text,
    currentdatetime integer,
    owner text,
    buyer text,
    obs text,
    last_notification integer DEFAULT 0
);


ALTER TABLE public.publications_log OWNER TO vbravo;

--
-- Name: publications_log_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE publications_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.publications_log_id_seq OWNER TO vbravo;

--
-- Name: publications_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE publications_log_id_seq OWNED BY publications_log.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY publications_log ALTER COLUMN id SET DEFAULT nextval('publications_log_id_seq'::regclass);


--
-- Data for Name: publications_log; Type: TABLE DATA; Schema: public; Owner: vbravo
--

COPY publications_log (id, publicaciones_id, status, currentdatetime, owner, buyer, obs, last_notification) FROM stdin;
5	20	Sold	1427905291	aaraujo	vbravo	\N	\N
6	19	Sold	1428328671	aaraujo	vbravo	\N	\N
7	20	Scored	1428329121	aaraujo	vbravo	\N	\N
8	17	Sold	1428332521	vbravo	aaraujo	\N	\N
9	17	Scored	1428332533	vbravo	aaraujo	\N	\N
10	21	Published	1428352455	aaraujo	aaraujo	\N	\N
11	23	Published	1428438984	vbravo	vbravo	\N	\N
12	26	Published	1428441869	vbravo	vbravo	\N	\N
13	26	Sold	1429105522	vbravo	jbakhos	\N	\N
14	26	Scored	1429105534	vbravo	jbakhos	\N	\N
16	38	Borrador	1432254117	vbravo	vbravo	\N	\N
17	38	Borrador	1432254130	vbravo	vbravo	\N	\N
18	38	Published	1432254478	vbravo	vbravo	\N	\N
19	38	Draft	1432254484	vbravo	vbravo	\N	\N
20	38	Published	1432254490	vbravo	vbravo	\N	\N
21	38	Draft	1432260047	vbravo	vbravo	\N	\N
22	50	Sold	1433547052	slee	vbravo	\N	\N
23	52	Draft	1433791589	vbravo	vbravo	\N	\N
24	52	Published	1433791723	vbravo	vbravo	\N	\N
25	52	Draft	1433792370	vbravo	vbravo	\N	\N
26	52	Published	1433792636	vbravo	vbravo	\N	\N
27	52	Draft	1433792822	vbravo	vbravo	\N	\N
28	52	Published	1433793859	vbravo	vbravo	\N	\N
29	52	Draft	1433793986	vbravo	vbravo	\N	\N
30	52	Published	1433794055	vbravo	vbravo	\N	\N
31	52	Draft	1433794184	vbravo	vbravo	\N	\N
32	27	Sold	1433809735	vbravo	jbakhos	\N	\N
33	52	Published	1433810034	vbravo	vbravo	\N	\N
34	52	Draft	1433810384	vbravo	vbravo	\N	\N
35	52	Published	1433811539	vbravo	vbravo	\N	\N
36	52	Draft	1433812477	vbravo	vbravo	\N	\N
37	52	Published	1433812960	vbravo	vbravo	\N	\N
38	52	Draft	1433856556	vbravo	vbravo	\N	\N
39	52	Published	1433861609	vbravo	vbravo	\N	\N
40	52	Draft	1433861683	vbravo	vbravo	\N	\N
41	52	Published	1433861903	vbravo	vbravo	\N	\N
42	52	Draft	1433862602	vbravo	vbravo	\N	\N
43	52	Published	1433862950	vbravo	vbravo	\N	\N
44	52	Draft	1433863195	vbravo	vbravo	\N	\N
45	52	Published	1433876692	vbravo	vbravo	\N	\N
46	52	Draft	1433876983	vbravo	vbravo	\N	\N
47	52	Published	1433878238	vbravo	vbravo	\N	\N
48	52	Draft	1433879193	vbravo	vbravo	\N	\N
49	52	Published	1433879387	vbravo	vbravo	\N	\N
50	52	Draft	1433879462	vbravo	vbravo	\N	\N
51	52	Published	1433879529	vbravo	vbravo	\N	\N
52	52	Draft	1433879726	vbravo	vbravo	\N	\N
53	52	Published	1433880431	vbravo	vbravo	\N	\N
54	52	Draft	1433880527	vbravo	vbravo	\N	\N
55	52	Published	1433880669	vbravo	vbravo	\N	\N
56	52	Draft	1433945838	vbravo	vbravo	\N	\N
57	52	Published	1433948053	vbravo	vbravo	\N	\N
58	39	Sold	1433948078	aaraujo	vbravo	\N	\N
59	30	Sold	1433948287	solazver	vbravo	\N	\N
60	29	Sold	1433949054	solazver	vbravo	\N	\N
61	39	Sold	1433953382	aaraujo	vbravo	\N	\N
62	30	Sold	1433953690	solazver	vbravo	\N	\N
63	19	Sold	1433954045	aaraujo	vbravo	\N	\N
64	50	Sold	1433964136	slee	vbravo	\N	\N
65	39	Sold	1433964566	aaraujo	vbravo	\N	\N
66	50	Sold	1433965348	slee	vbravo	\N	\N
67	39	Sold	1433965430	aaraujo	vbravo	\N	\N
68	30	Sold	1433965685	solazver	vbravo	\N	\N
69	39	Sold	1433966053	aaraujo	vbravo	\N	\N
70	30	Draft	1433980854	solazver	vbravo	\N	\N
71	30	Published	1433980865	solazver	vbravo	\N	\N
72	39	Sold	1434055273	aaraujo	vbravo	\N	\N
73	39	Sold	1434055568	aaraujo	vbravo	\N	\N
74	39	Sold	1434055891	aaraujo	vbravo	\N	\N
75	39	Sold	1434056081	aaraujo	vbravo	\N	\N
76	38	Published	1437423444	vbravo	vbravo	\N	\N
77	68	Sold	1437423763	vbravo	solazver	\N	\N
78	68	Scored	1437423777	vbravo	solazver	\N	\N
79	67	Sold	1437424880	vbravo	solazver	\N	\N
80	30	Sold	1437488723	solazver	vbravo	\N	\N
81	30	Scored	1437488735	solazver	vbravo	\N	\N
82	69	Sold	1438012665	solazver	vbravo	\N	\N
83	69	Scored	1438012672	solazver	vbravo	\N	\N
84	69	Delivered	1438012678	solazver	vbravo	\N	\N
85	69	Draft	1438012774	solazver	vbravo	\N	\N
86	69	Published	1438012780	solazver	vbravo	\N	\N
87	29	Sold	1438024326	solazver	vbravo	\N	\N
88	29	Scored	1438026531	solazver	vbravo	\N	\N
89	29	Delivered	1438026577	solazver	vbravo	\N	\N
90	29	Draft	1438026586	solazver	vbravo	\N	\N
91	29	Published	1438026593	solazver	vbravo	\N	\N
92	29	Sold	1438026627	solazver	vbravo	\N	\N
93	29	Scored	1438026739	solazver	vbravo	\N	\N
94	29	Delivered	1438026746	solazver	vbravo	\N	\N
95	29	Draft	1438026756	solazver	vbravo	\N	\N
96	29	Published	1438026763	solazver	vbravo	\N	\N
97	29	Sold	1438027278	solazver	vbravo	\N	\N
98	29	Scored	1438032521	solazver	vbravo	\N	\N
99	29	Delivered	1438032528	solazver	vbravo	\N	\N
100	29	Draft	1438032535	solazver	vbravo	\N	\N
101	29	Published	1438032542	solazver	vbravo	\N	\N
102	29	Sold	1438032579	solazver	vbravo	\N	\N
103	29	Scored	1438032652	solazver	vbravo	\N	\N
104	29	Delivered	1438032658	solazver	vbravo	\N	\N
105	29	Draft	1438032664	solazver	vbravo	\N	\N
106	29	Published	1438032670	solazver	vbravo	\N	\N
107	29	Sold	1438033057	solazver	vbravo	\N	\N
108	50	Sold	1438033537	slee	vbravo	\N	\N
109	29	NoScored	1438092834	solazver	vbravo	\N	\N
110	50	NoScored	1438092911	slee	vbravo	\N	\N
111	50	Delivered	1438093002	slee	vbravo	\N	\N
112	50	Draft	1438093010	slee	vbravo	\N	\N
113	50	NoScored	1438093131	slee	vbravo	\N	\N
114	29	NoScored	1438093159	solazver	vbravo	\N	\N
115	50	NoScored	1438093273	slee	vbravo	\N	\N
116	50	NoScored	1438094579	slee	vbravo	\N	\N
117	50	NoScored	1438094579	slee	vbravo	\N	\N
118	50	NoScored	1438094911	slee	vbravo	\N	\N
119	50	NoScored	1438094911	slee	vbravo	\N	\N
120	50	NoScored	1438095142	slee	vbravo	\N	\N
121	29	NoScored	1438095142	solazver	vbravo	\N	\N
122	61	Draft	1438097598	vbravo	vbravo	\N	\N
123	61	Published	1438097604	vbravo	vbravo	\N	\N
124	32	Draft	1438097686	vbravo	vbravo	\N	\N
125	32	Published	1438097695	vbravo	vbravo	\N	\N
126	23	Draft	1438097702	vbravo	vbravo	\N	\N
127	23	Published	1438097712	vbravo	vbravo	\N	\N
128	50	NoScored	1438098181	slee	vbravo	\N	\N
129	29	NoScored	1438098181	solazver	vbravo	\N	\N
130	38	NoSold	1438098181	vbravo	vbravo	\N	\N
131	27	NoSold	1438098182	vbravo	vbravo	\N	\N
132	22	NoSold	1438098182	vbravo	vbravo	\N	\N
133	18	NoSold	1438098182	vbravo	vbravo	\N	\N
134	16	NoSold	1438098183	vbravo	vbravo	\N	\N
135	69	NoSold	1438099541	solazver	vbravo	\N	\N
136	69	Draft	1438100245	solazver	vbravo	\N	\N
137	69	Published	1438100251	solazver	vbravo	\N	\N
138	50	Scored	1438115793	slee	vbravo	\N	\N
139	30	Delivered	1438119924	solazver	vbravo	\N	\N
140	30	Draft	1438119934	solazver	vbravo	\N	\N
141	30	Published	1438119954	solazver	vbravo	\N	\N
142	69	Draft	1438120616	solazver	vbravo	\N	\N
143	69	Published	1438120621	solazver	vbravo	\N	\N
144	50	Delivered	1438120981	slee	vbravo	\N	\N
145	50	Draft	1438120989	slee	vbravo	\N	\N
146	50	Published	1438120997	slee	vbravo	\N	\N
147	50	Sold	1438121006	slee	vbravo	\N	\N
148	72	Published	1438198193	vbravo	vbravo	\N	\N
149	30	Sold	1438288398	solazver	vbravo	\N	\N
150	72	Published	1438611547	vbravo	vbravo	\N	\N
151	72	Draft	1438611571	vbravo	vbravo	\N	\N
152	72	Published	1438611592	vbravo	vbravo	\N	\N
153	71	Sold	1438721403	solazver	vbravo	\N	\N
154	72	Draft	1438721430	vbravo	vbravo	\N	\N
155	72	Published	1438721436	vbravo	vbravo	\N	\N
156	71	Sold	1438721540	solazver	vbravo	\N	\N
157	72	Draft	1438721556	vbravo	vbravo	\N	\N
158	72	Published	1438721561	vbravo	vbravo	\N	\N
159	71	Sold	1438721585	solazver	vbravo	\N	\N
160	72	Draft	1438722355	vbravo	vbravo	\N	\N
161	72	Published	1438722363	vbravo	vbravo	\N	\N
162	71	Sold	1438722433	solazver	vbravo	\N	\N
163	72	Draft	1438722480	vbravo	vbravo	\N	\N
164	72	Published	1438722489	vbravo	vbravo	\N	\N
165	71	Sold	1438724650	solazver	vbravo	\N	\N
166	71	Sold	1438724710	solazver	vbravo	\N	\N
167	71	Sold	1438725061	solazver	vbravo	\N	\N
168	71	Sold	1438725136	solazver	vbravo	\N	\N
169	71	Sold	1438726032	solazver	vbravo	\N	\N
170	72	Sold	1438791464	solazver	vbravo	\N	\N
171	73	Published	1438810077	vbravo	vbravo	\N	\N
172	76	Published	1438869038	vbravo	vbravo	\N	\N
173	78	Published	1438871965	vbravo	vbravo	\N	\N
174	79	Published	1438895470	vbravo	vbravo	\N	\N
175	18	Draft	1439175508	vbravo	vbravo	\N	\N
176	80	Published	1439215042	vbravo	vbravo	\N	\N
177	81	Published	1439215434	vbravo	vbravo	\N	\N
178	82	Published	1439216324	vbravo	vbravo	\N	\N
179	82	Published	1439216346	vbravo	vbravo	\N	\N
180	60	Sold	1439240384	vbravo	aadeva	\N	\N
181	82	Sold	1439240712	vbravo	aadeva	\N	\N
182	69	Sold	1439256467	solazver	aadeva	\N	\N
183	61	Sold	1439256907	vbravo	aadeva	\N	\N
184	85	Published	1439258747	aadeva	aadeva	\N	\N
185	85	Sold	1439295845	aadeva	jbakhos	\N	\N
186	23	Sold	1439301915	vbravo	jbakhos	\N	\N
187	38	Draft	1439304596	vbravo	vbravo	\N	\N
188	38	Published	1439304620	vbravo	vbravo	\N	\N
189	27	Draft	1439304830	vbravo	vbravo	\N	\N
190	27	Published	1439304852	vbravo	vbravo	\N	\N
191	18	Published	1439306407	vbravo	vbravo	\N	\N
192	86	Published	1439306920	vbravo	vbravo	\N	\N
193	92	Published	1439328546	vbravo	vbravo	\N	\N
194	38	Sold	1439328781	vbravo	aadeva	\N	\N
195	38	Sold	1439328786	vbravo	aadeva	\N	\N
196	93	Published	1439333997	adri77	adri77	\N	\N
197	92	Sold	1439430167	vbravo	adri77	\N	\N
198	95	Published	1439472923	solazver	solazver	\N	\N
199	96	Published	1439513684	aadeva	joseph	\N	\N
200	94	Published	1439513688	vbravo	joseph	\N	\N
201	91	Published	1439513691	aadeva	joseph	\N	\N
202	93	Sold	1439657173	adri77	joseph	\N	\N
203	96	Sold	1439694767	aadeva	vbravo	\N	\N
204	91	Sold	1439765183	aadeva	vbravo	\N	\N
205	97	Published	1439953067	vbravo	vbravo	\N	\N
206	98	Published	1440002584	joseph	joseph	\N	\N
207	100	Published	1440030858	joseph	vbravo	\N	\N
208	101	Published	1440106046	vbravo	vbravo	\N	\N
209	102	Published	1440172217	vbravo	vbravo	\N	\N
210	103	Published	1440172776	vbravo	vbravo	\N	\N
211	104	Published	1440173039	vbravo	vbravo	\N	\N
212	105	Published	1440173251	vbravo	vbravo	\N	\N
213	106	Published	1440174834	vbravo	vbravo	\N	\N
214	109	Published	1440175387	vbravo	vbravo	\N	\N
215	110	Published	1440448221	solazver	solazver	\N	\N
216	110	Sold	1440448386	solazver	vbravo	\N	\N
217	112	Published	1440448887	solazver	vbravo	\N	\N
218	112	Sold	1440448980	solazver	vbravo	\N	\N
219	113	Published	1440449787	solazver	solazver	\N	\N
220	113	Sold	1440449820	solazver	vbravo	\N	\N
221	114	Published	1440588850	joseph	joseph	\N	\N
222	105	Sold	1440589409	vbravo	joseph	\N	\N
223	115	Published	1441033690	vbravo	vbravo	\N	\N
224	117	Published	1441058533	ssuarez	vbravo	\N	\N
225	116	Published	1441058536	ssuarez	vbravo	\N	\N
226	18	Sold	1441066673	vbravo	joseph	\N	\N
227	117	Sold	1441122813	ssuarez	vbravo	\N	\N
228	115	Sold	1441124667	vbravo	ssuarez	\N	\N
229	104	Sold	1441124809	vbravo	ssuarez	\N	\N
230	102	Sold	1441143365	vbravo	ssuarez	\N	\N
231	118	Published	1441927214	maria	joseph	\N	\N
232	116	Sold	1442030904	ssuarez	vbravo	\N	\N
233	95	Sold	1442031120	solazver	vbravo	\N	\N
234	109	Sold	1442031397	vbravo	aaraujo	\N	\N
235	116	Sold	1442108882	ssuarez	vbravo	\N	\N
236	116	Sold	1442110144	ssuarez	vbravo	\N	0
237	116	Sold	1442111419	ssuarez	vbravo	\N	0
238	116	Sold	1442112301	ssuarez	vbravo	\N	0
239	116	Sold	1442112573	ssuarez	vbravo	\N	0
240	116	Sold	1442282166	ssuarez	vbravo	\N	0
241	116	Sold	1442282541	ssuarez	vbravo	\N	0
242	116	Sold	1442285216	ssuarez	vbravo	\N	0
243	116	Sold	1442286147	ssuarez	vbravo	\N	0
244	116	Sold	1442286449	ssuarez	vbravo	\N	0
245	116	Sold	1442287106	ssuarez	vbravo	\N	0
246	116	Sold	1442287282	ssuarez	vbravo	\N	0
247	116	Sold	1442356915	ssuarez	vbravo	\N	0
248	116	Sold	1442357134	ssuarez	vbravo	\N	0
249	116	Sold	1442602404	ssuarez	vbravo	\N	0
250	116	Sold	1442604196	ssuarez	joseph	\N	0
251	118	Sold	1442607382	maria	joseph	\N	0
252	114	Sold	1442607944	joseph	maria	\N	0
253	119	Published	1443059930	joseph	joseph	\N	0
254	116	Sold	1443059958	ssuarez	joseph	\N	0
255	120	Published	1443203778	vbravo	vbravo	\N	0
256	121	Published	1443203882	vbravo	vbravo	\N	0
257	122	Published	1443204088	vbravo	vbravo	\N	0
258	101	Sold	1443453393	vbravo	gsamir	\N	0
259	122	Draft	1443544489	vbravo	vbravo	\N	0
260	123	Published	1443559469	vbravo	solazver	\N	0
261	122	Published	1443648613	vbravo	joseph	\N	0
262	124	Published	1443650190	maria	joseph	\N	0
263	125	Published	1443720930	vbravo	vbravo	\N	0
264	126	Published	1443721339	gsamir	vbravo	\N	0
265	126	Sold	1443837286	gsamir	vbravo	\N	0
266	127	Published	1444080041	vbravo	vbravo	\N	0
267	125	Sold	1444921884	vbravo	aaraujo	\N	0
268	122	Sold	1444939382	vbravo	aaraujo	\N	0
269	122	Delivered	1444940170	vbravo	vbravo	\N	0
270	122	Draft	1444940178	vbravo	vbravo	\N	0
271	122	Published	1444940284	vbravo	vbravo	\N	0
272	122	Sold	1444940446	vbravo	aaraujo	\N	0
273	122	Delivered	1444940652	vbravo	vbravo	\N	0
274	122	Draft	1444940714	vbravo	vbravo	\N	0
275	122	Published	1444940760	vbravo	vbravo	\N	0
276	122	Sold	1444940826	vbravo	aaraujo	\N	0
277	122	Sold	1444940949	vbravo	aaraujo	\N	0
278	128	Published	1444942358	aaraujo	aaraujo	\N	0
279	129	Published	1445454741	vbravo	vbravo	\N	0
280	97	Draft	1446218735	vbravo	vbravo	\N	0
281	97	Published	1446218779	vbravo	vbravo	\N	0
282	18	Delivered	1446218868	vbravo	vbravo	\N	0
283	18	Draft	1446218889	vbravo	vbravo	\N	0
284	18	Published	1446218925	vbravo	vbravo	\N	0
285	130	Published	1446340325	joseph	joseph	\N	0
286	18	Sold	1448456132	vbravo	joseph	\N	0
287	97	Sold	1448588411	vbravo	joseph	\N	0
288	131	Published	1449696186	joseph	joseph	\N	0
289	131	Sold	1449696427	joseph	maria	\N	0
290	130	Sold	1450457323	joseph	maria	\N	0
291	134	Published	1452275474	mviloria	vbravo	\N	0
292	133	Published	1452275480	joseph	vbravo	\N	0
293	134	Sold	1452879102	mviloria	vbravo	\N	0
294	138	Published	1453908884	joseph	vbravo	\N	0
295	139	Published	1453908886	joseph	vbravo	\N	0
296	137	Published	1454441112	joseph	vbravo	\N	0
297	135	Published	1454441118	joseph	vbravo	\N	0
298	124	Sold	1455108509	maria	joseph	\N	0
299	143	Published	1458307910	vbravo	vbravo	\N	0
300	110	Sold	1458774945	solazver	vbravo	\N	0
301	119	Sold	1462399302	joseph	vbravo	\N	0
302	133	Sold	1462399777	joseph	vbravo	\N	0
303	101	Delivered	1464012732	vbravo	vbravo	\N	0
304	101	Draft	1464012746	vbravo	vbravo	\N	0
305	101	Published	1464012755	vbravo	vbravo	\N	0
306	144	Published	1464021380	vbravo	vbravo	\N	0
307	142	Published	1464806869	vbravo	vbravo	\N	0
308	158	Published	1465310424	vbravo	vbravo	\N	0
309	160	Published	1465313257	vbravo	vbravo	\N	0
310	162	Published	1465349534	solazver	solazver	\N	0
311	163	Published	1467128411	vbravo	vbravo	\N	0
312	164	Published	1467129882	vbravo	vbravo	\N	0
313	167	Published	1467212079	vbravo	vbravo	\N	0
314	171	Published	1467215073	vbravo	vbravo	\N	0
315	170	Published	1467215078	vbravo	vbravo	\N	0
316	172	Published	1467327672	vbravo	vbravo	\N	0
317	169	Published	1467369684	vbravo	joseph	\N	0
318	166	Published	1467369689	vbravo	joseph	\N	0
319	161	Published	1467369692	vbravo	joseph	\N	0
320	157	Published	1467369695	vbravo	joseph	\N	0
321	141	Published	1467369702	joseph	joseph	\N	0
322	140	Published	1467369705	joseph	joseph	\N	0
323	136	Published	1467369707	joseph	joseph	\N	0
324	132	Published	1467369710	joseph	joseph	\N	0
325	173	Published	1467385316	vbravo	vbravo	\N	0
\.


--
-- Name: publications_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vbravo
--

SELECT pg_catalog.setval('publications_log_id_seq', 325, true);


--
-- Name: registro_pkey; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY publications_log
    ADD CONSTRAINT registro_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

