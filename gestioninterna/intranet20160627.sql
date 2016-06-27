--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: accion_especifica; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE accion_especifica (
    id integer NOT NULL,
    id_proyecto_poa integer NOT NULL,
    nombre text,
    codigo_accion text
);


ALTER TABLE public.accion_especifica OWNER TO vbravo;

--
-- Name: accion_especifica_id_proyecto_poa_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE accion_especifica_id_proyecto_poa_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.accion_especifica_id_proyecto_poa_seq OWNER TO vbravo;

--
-- Name: accion_especifica_id_proyecto_poa_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE accion_especifica_id_proyecto_poa_seq OWNED BY accion_especifica.id_proyecto_poa;


--
-- Name: accion_especifica_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE accion_especifica_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.accion_especifica_id_seq OWNER TO vbravo;

--
-- Name: accion_especifica_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE accion_especifica_id_seq OWNED BY accion_especifica.id;


--
-- Name: actividad_por_accion; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE actividad_por_accion (
    id integer NOT NULL,
    nombre text,
    id_accion_especifica integer NOT NULL,
    id_equipo_responsable integer NOT NULL,
    producto text,
    fecha_entrega integer,
    status text,
    resolucion text,
    tipo text,
    fechaplaniteracion integer,
    porcentaje integer,
    id_persona_responsable integer,
    id_persona_presidencia integer,
    tipo_producto text,
    trimestre_entrega character(5),
    cuantos_productos integer,
    enlace text,
    laststatus text,
    completado boolean,
    id_codigo_accion text,
    flujo text,
    adjunto text
);


ALTER TABLE public.actividad_por_accion OWNER TO vbravo;

--
-- Name: actividad_por_accion_id_accion_especifica_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE actividad_por_accion_id_accion_especifica_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actividad_por_accion_id_accion_especifica_seq OWNER TO vbravo;

--
-- Name: actividad_por_accion_id_accion_especifica_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE actividad_por_accion_id_accion_especifica_seq OWNED BY actividad_por_accion.id_accion_especifica;


--
-- Name: actividad_por_accion_id_equipo_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE actividad_por_accion_id_equipo_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actividad_por_accion_id_equipo_seq OWNER TO vbravo;

--
-- Name: actividad_por_accion_id_equipo_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE actividad_por_accion_id_equipo_seq OWNED BY actividad_por_accion.id_equipo_responsable;


--
-- Name: actividad_por_accion_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE actividad_por_accion_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actividad_por_accion_id_seq OWNER TO vbravo;

--
-- Name: actividad_por_accion_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE actividad_por_accion_id_seq OWNED BY actividad_por_accion.id;


--
-- Name: actividad_registro; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE actividad_registro (
    id integer NOT NULL,
    estado character(100),
    propietario character(100),
    fechaaccion integer,
    id_actividad integer NOT NULL,
    porcentaje integer,
    enlace text,
    completado boolean
);


ALTER TABLE public.actividad_registro OWNER TO vbravo;

--
-- Name: actividad_registro_id_actividad_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE actividad_registro_id_actividad_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actividad_registro_id_actividad_seq OWNER TO vbravo;

--
-- Name: actividad_registro_id_actividad_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE actividad_registro_id_actividad_seq OWNED BY actividad_registro.id_actividad;


--
-- Name: actividad_registro_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE actividad_registro_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actividad_registro_id_seq OWNER TO vbravo;

--
-- Name: actividad_registro_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE actividad_registro_id_seq OWNED BY actividad_registro.id;


--
-- Name: actividad_registro_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE actividad_registro_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actividad_registro_seq OWNER TO vbravo;

--
-- Name: adjuntos; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE adjuntos (
    id integer NOT NULL,
    ruta text,
    id_reunion integer NOT NULL
);


ALTER TABLE public.adjuntos OWNER TO vbravo;

--
-- Name: adjuntos_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE adjuntos_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.adjuntos_id_seq OWNER TO vbravo;

--
-- Name: adjuntos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE adjuntos_id_seq OWNED BY adjuntos.id;


--
-- Name: architecture; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE architecture (
    id integer NOT NULL,
    name text,
    description text
);


ALTER TABLE public.architecture OWNER TO vbravo;

--
-- Name: architecture_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE architecture_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.architecture_id_seq OWNER TO vbravo;

--
-- Name: architecture_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE architecture_id_seq OWNED BY architecture.id;


--
-- Name: assessments; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE assessments (
    id integer NOT NULL,
    username text NOT NULL,
    value text,
    comments text,
    id_ticket integer NOT NULL,
    flowfilename text,
    parenttask text,
    "time" integer,
    iteration integer,
    optionalvalue character(30)
);


ALTER TABLE public.assessments OWNER TO vbravo;

--
-- Name: assessments_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE assessments_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.assessments_seq OWNER TO vbravo;

--
-- Name: ticket; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE ticket (
    id integer NOT NULL,
    type text,
    "time" bigint,
    changetime bigint,
    component text,
    severity text,
    priority text,
    owner text,
    reporter text,
    cc text,
    version text,
    milestone text,
    status text,
    resolution text,
    summary text,
    description text,
    keywords text,
    parenttask text,
    flowfilepath text
);


ALTER TABLE public.ticket OWNER TO vbravo;

--
-- Name: assessments_ticket; Type: VIEW; Schema: public; Owner: vbravo
--

CREATE VIEW assessments_ticket AS
    SELECT assessments.id, ticket.id AS ticketid, ticket.milestone, ticket.owner, ticket.reporter, ticket.status, ticket.summary, assessments.value, assessments.username FROM (assessments JOIN ticket ON ((ticket.id = assessments.id_ticket)));


ALTER TABLE public.assessments_ticket OWNER TO vbravo;

--
-- Name: attachment; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE attachment (
    type text NOT NULL,
    id text NOT NULL,
    filename text NOT NULL,
    size integer,
    "time" bigint,
    description text,
    author text,
    ipnr text
);


ALTER TABLE public.attachment OWNER TO vbravo;

--
-- Name: auth_cookie; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE auth_cookie (
    cookie text NOT NULL,
    name text NOT NULL,
    ipnr text NOT NULL,
    "time" integer
);


ALTER TABLE public.auth_cookie OWNER TO vbravo;

--
-- Name: cache; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE cache (
    id text NOT NULL,
    generation integer
);


ALTER TABLE public.cache OWNER TO vbravo;

--
-- Name: calendario; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE calendario (
    id integer NOT NULL,
    fechadia integer,
    nohabil boolean,
    proximohabil integer
);


ALTER TABLE public.calendario OWNER TO vbravo;

--
-- Name: component; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE component (
    name text NOT NULL,
    owner text,
    description text
);


ALTER TABLE public.component OWNER TO vbravo;

--
-- Name: confirmado_reunion; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE confirmado_reunion (
    id integer NOT NULL,
    id_reunion integer NOT NULL,
    id_personal text
);


ALTER TABLE public.confirmado_reunion OWNER TO vbravo;

--
-- Name: confirmado_reunion_id_reunion_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE confirmado_reunion_id_reunion_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.confirmado_reunion_id_reunion_seq OWNER TO vbravo;

--
-- Name: confirmado_reunion_id_reunion_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE confirmado_reunion_id_reunion_seq OWNED BY confirmado_reunion.id_reunion;


--
-- Name: confirmado_reunion_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE confirmado_reunion_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.confirmado_reunion_id_seq OWNER TO vbravo;

--
-- Name: confirmado_reunion_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE confirmado_reunion_id_seq OWNED BY confirmado_reunion.id;


--
-- Name: consejero_reunion; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE consejero_reunion (
    id integer NOT NULL,
    id_reunion integer NOT NULL,
    id_personal text
);


ALTER TABLE public.consejero_reunion OWNER TO vbravo;

--
-- Name: consejero_reunion_id_reunion_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE consejero_reunion_id_reunion_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.consejero_reunion_id_reunion_seq OWNER TO vbravo;

--
-- Name: consejero_reunion_id_reunion_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE consejero_reunion_id_reunion_seq OWNED BY consejero_reunion.id_reunion;


--
-- Name: consejero_reunion_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE consejero_reunion_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.consejero_reunion_id_seq OWNER TO vbravo;

--
-- Name: consejero_reunion_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE consejero_reunion_id_seq OWNED BY consejero_reunion.id;


--
-- Name: correspondencia; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE correspondencia (
    id integer NOT NULL,
    fecha_generada integer,
    fecha_recepcion integer,
    procedencia text,
    asunto text,
    para text,
    instrucciones text,
    instrucciones_adicionales text,
    respuesta text,
    fecha_respuesta integer,
    codigo_oficio_entrante text,
    status text,
    prioridad text,
    codigo_oficio_saliente text,
    tipo text,
    estado text,
    nombreciudadano text,
    cedulaciudadano text,
    correociudadano text,
    telefonociudadano text
);


ALTER TABLE public.correspondencia OWNER TO vbravo;

--
-- Name: correspondencia_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE correspondencia_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.correspondencia_id_seq OWNER TO vbravo;

--
-- Name: correspondencia_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE correspondencia_id_seq OWNED BY correspondencia.id;


--
-- Name: correspondencia_registro; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE correspondencia_registro (
    id integer NOT NULL,
    id_correspondencia integer NOT NULL,
    responsable text,
    status text,
    fecha_accion integer,
    respuesta text,
    tipo text,
    instrucciones text,
    instrucciones_adicionales text,
    para text,
    codigo_oficio_saliente text
);


ALTER TABLE public.correspondencia_registro OWNER TO vbravo;

--
-- Name: correspondencia_registro_id_correspondencia_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE correspondencia_registro_id_correspondencia_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.correspondencia_registro_id_correspondencia_seq OWNER TO vbravo;

--
-- Name: correspondencia_registro_id_correspondencia_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE correspondencia_registro_id_correspondencia_seq OWNED BY correspondencia_registro.id_correspondencia;


--
-- Name: correspondencia_registro_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE correspondencia_registro_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.correspondencia_registro_id_seq OWNER TO vbravo;

--
-- Name: correspondencia_registro_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE correspondencia_registro_id_seq OWNED BY correspondencia_registro.id;


--
-- Name: download; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE download (
    id integer NOT NULL,
    file text,
    description text,
    size integer,
    "time" integer,
    count integer,
    author text,
    tags text,
    component text,
    version text,
    architecture integer,
    platform integer,
    type integer
);


ALTER TABLE public.download OWNER TO vbravo;

--
-- Name: download_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE download_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.download_id_seq OWNER TO vbravo;

--
-- Name: download_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE download_id_seq OWNED BY download.id;


--
-- Name: download_type; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE download_type (
    id integer NOT NULL,
    name text,
    description text
);


ALTER TABLE public.download_type OWNER TO vbravo;

--
-- Name: download_type_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE download_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.download_type_id_seq OWNER TO vbravo;

--
-- Name: download_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE download_type_id_seq OWNED BY download_type.id;


--
-- Name: enum; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE enum (
    type text NOT NULL,
    name text NOT NULL,
    value text
);


ALTER TABLE public.enum OWNER TO vbravo;

--
-- Name: equipo_personal; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE equipo_personal (
    id integer NOT NULL,
    id_equipo integer NOT NULL,
    id_personal text
);


ALTER TABLE public.equipo_personal OWNER TO vbravo;

--
-- Name: equipo_personal_id_equipo_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE equipo_personal_id_equipo_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.equipo_personal_id_equipo_seq OWNER TO vbravo;

--
-- Name: equipo_personal_id_equipo_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE equipo_personal_id_equipo_seq OWNED BY equipo_personal.id_equipo;


--
-- Name: equipo_personal_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE equipo_personal_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.equipo_personal_id_seq OWNER TO vbravo;

--
-- Name: equipo_personal_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE equipo_personal_id_seq OWNED BY equipo_personal.id;


--
-- Name: equipo_responsable; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE equipo_responsable (
    id integer NOT NULL,
    grupo text,
    descripcion text,
    fecha_creacion integer,
    fecha_desincorporacion integer
);


ALTER TABLE public.equipo_responsable OWNER TO vbravo;

--
-- Name: equipo_responsable_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE equipo_responsable_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.equipo_responsable_id_seq OWNER TO vbravo;

--
-- Name: equipo_responsable_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE equipo_responsable_id_seq OWNED BY equipo_responsable.id;


--
-- Name: estado_actividad_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE estado_actividad_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.estado_actividad_id_seq OWNER TO vbravo;

--
-- Name: estado_de_actividad; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE estado_de_actividad (
    id integer NOT NULL,
    estado text,
    porcentaje_asignado integer,
    id_actividad integer NOT NULL
);


ALTER TABLE public.estado_de_actividad OWNER TO vbravo;

--
-- Name: estado_de_actividad_id_actividad_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE estado_de_actividad_id_actividad_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.estado_de_actividad_id_actividad_seq OWNER TO vbravo;

--
-- Name: estado_de_actividad_id_actividad_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE estado_de_actividad_id_actividad_seq OWNED BY estado_de_actividad.id_actividad;


--
-- Name: estado_de_actividad_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE estado_de_actividad_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.estado_de_actividad_id_seq OWNER TO vbravo;

--
-- Name: estado_de_actividad_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE estado_de_actividad_id_seq OWNED BY estado_de_actividad.id;


--
-- Name: forum; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE forum (
    id integer NOT NULL,
    name text,
    "time" integer,
    forum_group integer,
    author text,
    moderators text,
    subscribers text,
    subject text,
    description text
);


ALTER TABLE public.forum OWNER TO vbravo;

--
-- Name: forum_group; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE forum_group (
    id integer NOT NULL,
    name text,
    description text
);


ALTER TABLE public.forum_group OWNER TO vbravo;

--
-- Name: forum_group_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE forum_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.forum_group_id_seq OWNER TO vbravo;

--
-- Name: forum_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE forum_group_id_seq OWNED BY forum_group.id;


--
-- Name: forum_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE forum_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.forum_id_seq OWNER TO vbravo;

--
-- Name: forum_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE forum_id_seq OWNED BY forum.id;


--
-- Name: institucion; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE institucion (
    id integer NOT NULL,
    nombre_institucion character(60),
    acronimo character(20),
    ciudad character(30),
    estadp character(30),
    pais character(50)
);


ALTER TABLE public.institucion OWNER TO vbravo;

--
-- Name: message; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE message (
    id integer NOT NULL,
    forum integer,
    topic integer,
    replyto integer,
    "time" integer,
    author text,
    body text
);


ALTER TABLE public.message OWNER TO vbravo;

--
-- Name: message_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE message_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.message_id_seq OWNER TO vbravo;

--
-- Name: message_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE message_id_seq OWNED BY message.id;


--
-- Name: milestone; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE milestone (
    name text NOT NULL,
    due bigint,
    completed bigint,
    description text
);


ALTER TABLE public.milestone OWNER TO vbravo;

--
-- Name: node_change; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE node_change (
    repos integer NOT NULL,
    rev text NOT NULL,
    path text NOT NULL,
    node_type text,
    change_type text NOT NULL,
    base_path text,
    base_rev text
);


ALTER TABLE public.node_change OWNER TO vbravo;

--
-- Name: permission; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE permission (
    username text NOT NULL,
    action text NOT NULL
);


ALTER TABLE public.permission OWNER TO vbravo;

--
-- Name: personal; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE personal (
    nombres character(60),
    apellidos character(60),
    cargo character(30),
    cedula character(30) NOT NULL,
    estado character(30),
    nombre_cuenta_correo_electronico character(30),
    nombre_cuenta_intranet character(30),
    lista_servidores_acceso text,
    fecha_ingreso integer,
    fecha_retiro integer,
    fecha_reincorporacion integer,
    id integer NOT NULL,
    status character(10) DEFAULT 'activo'::bpchar,
    departamento character(20),
    usuario text,
    proyecto text,
    nombre_cuenta_correo_personal character(30),
    telefono_habitacion text,
    telefono_personal text,
    domicilio character(100),
    tipo text,
    representante text
);


ALTER TABLE public.personal OWNER TO vbravo;

--
-- Name: personal_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE personal_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.personal_id_seq OWNER TO vbravo;

--
-- Name: personal_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE personal_id_seq OWNED BY personal.id;


--
-- Name: platform; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE platform (
    id integer NOT NULL,
    name text,
    description text
);


ALTER TABLE public.platform OWNER TO vbravo;

--
-- Name: platform_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE platform_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.platform_id_seq OWNER TO vbravo;

--
-- Name: platform_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE platform_id_seq OWNED BY platform.id;


--
-- Name: porcentaje_producto; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE porcentaje_producto (
    id integer NOT NULL,
    id_producto_de_actividad bigint,
    status text,
    porcentaje numeric,
    nombre text
);


ALTER TABLE public.porcentaje_producto OWNER TO vbravo;

--
-- Name: porcentaje_producto_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE porcentaje_producto_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.porcentaje_producto_id_seq OWNER TO vbravo;

--
-- Name: porcentaje_producto_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE porcentaje_producto_id_seq OWNED BY porcentaje_producto.id;


--
-- Name: prestaciones; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE prestaciones (
    id integer NOT NULL,
    usuario text,
    anoservicios text,
    fechasolicitud integer,
    motivosolicitud text,
    observacion text,
    status text,
    fechaanterior integer,
    montoanterior real,
    motivoanterior text,
    numero_solicitud integer,
    informacion_usuario text,
    montosolicitado real
);


ALTER TABLE public.prestaciones OWNER TO vbravo;

--
-- Name: prestaciones_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE prestaciones_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.prestaciones_id_seq OWNER TO vbravo;

--
-- Name: prestaciones_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE prestaciones_id_seq OWNED BY prestaciones.id;


--
-- Name: prestaciones_registro; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE prestaciones_registro (
    id integer NOT NULL,
    id_prestaciones integer NOT NULL,
    montosolicitado real,
    fechasolicitud integer,
    motivosolicitud text,
    fecha_accion integer,
    status text,
    propietario text
);


ALTER TABLE public.prestaciones_registro OWNER TO vbravo;

--
-- Name: prestaciones_registro_id_prestaciones_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE prestaciones_registro_id_prestaciones_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.prestaciones_registro_id_prestaciones_seq OWNER TO vbravo;

--
-- Name: prestaciones_registro_id_prestaciones_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE prestaciones_registro_id_prestaciones_seq OWNED BY prestaciones_registro.id_prestaciones;


--
-- Name: prestaciones_registro_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE prestaciones_registro_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.prestaciones_registro_id_seq OWNER TO vbravo;

--
-- Name: prestaciones_registro_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE prestaciones_registro_id_seq OWNED BY prestaciones_registro.id;


--
-- Name: producto_de_actividad; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE producto_de_actividad (
    id integer NOT NULL,
    nombre text,
    descripcion text,
    referencia text,
    tipo text,
    id_actividad bigint
);


ALTER TABLE public.producto_de_actividad OWNER TO vbravo;

--
-- Name: producto_de_actividad_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE producto_de_actividad_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.producto_de_actividad_id_seq OWNER TO vbravo;

--
-- Name: producto_de_actividad_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE producto_de_actividad_id_seq OWNED BY producto_de_actividad.id;


--
-- Name: proyecto_extra_poa; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE proyecto_extra_poa (
    id integer NOT NULL,
    nombre text,
    descripcion text
);


ALTER TABLE public.proyecto_extra_poa OWNER TO vbravo;

--
-- Name: proyecto_extra_poa_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE proyecto_extra_poa_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.proyecto_extra_poa_id_seq OWNER TO vbravo;

--
-- Name: proyecto_extra_poa_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE proyecto_extra_poa_id_seq OWNED BY proyecto_extra_poa.id;


--
-- Name: proyecto_poa; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE proyecto_poa (
    id integer NOT NULL,
    nombre text,
    descripcion text,
    objetivo_general text,
    objetivo_especifico text,
    problema_a_enfrentar text,
    codigo_proyecto text
);


ALTER TABLE public.proyecto_poa OWNER TO vbravo;

--
-- Name: proyecto_poa_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE proyecto_poa_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.proyecto_poa_id_seq OWNER TO vbravo;

--
-- Name: proyecto_poa_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE proyecto_poa_id_seq OWNED BY proyecto_poa.id;


--
-- Name: proyectos; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE proyectos (
    id integer NOT NULL,
    nombre character(120),
    descripcion text
);


ALTER TABLE public.proyectos OWNER TO vbravo;

--
-- Name: recursos; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE recursos (
    id integer NOT NULL,
    nombre text,
    web text,
    descripcion text,
    inventario integer
);


ALTER TABLE public.recursos OWNER TO vbravo;

--
-- Name: recursos_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE recursos_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.recursos_id_seq OWNER TO vbravo;

--
-- Name: recursos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE recursos_id_seq OWNED BY recursos.id;


--
-- Name: report; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE report (
    id integer NOT NULL,
    author text,
    title text,
    query text,
    description text
);


ALTER TABLE public.report OWNER TO vbravo;

--
-- Name: report_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE report_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.report_id_seq OWNER TO vbravo;

--
-- Name: report_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE report_id_seq OWNED BY report.id;


--
-- Name: repository; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE repository (
    id integer NOT NULL,
    name text NOT NULL,
    value text
);


ALTER TABLE public.repository OWNER TO vbravo;

--
-- Name: reuniones; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE reuniones (
    id integer NOT NULL,
    descripcion text,
    fecha_convocatoria integer,
    status text,
    tipo text,
    fecha_reunion integer,
    archivo_convocatoria text,
    archivo_agenda text,
    archivo_acta text,
    nombre text,
    rolfirma1 text,
    timestampfirma1 integer,
    rolfirma2 text,
    timestampfirma2 integer,
    codigo text,
    asistentes integer DEFAULT 0,
    actual_personal integer
);


ALTER TABLE public.reuniones OWNER TO vbravo;

--
-- Name: reuniones_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE reuniones_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.reuniones_id_seq OWNER TO vbravo;

--
-- Name: reuniones_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE reuniones_id_seq OWNED BY reuniones.id;


--
-- Name: reuniones_registro; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE reuniones_registro (
    id integer NOT NULL,
    descripcion text,
    fecha_convocatoria integer,
    id_reuniones integer NOT NULL,
    status text,
    tipo text,
    fecha_accion integer,
    propietario text
);


ALTER TABLE public.reuniones_registro OWNER TO vbravo;

--
-- Name: reuniones_registro_id_reuniones_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE reuniones_registro_id_reuniones_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.reuniones_registro_id_reuniones_seq OWNER TO vbravo;

--
-- Name: reuniones_registro_id_reuniones_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE reuniones_registro_id_reuniones_seq OWNED BY reuniones_registro.id_reuniones;


--
-- Name: reuniones_registro_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE reuniones_registro_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.reuniones_registro_id_seq OWNER TO vbravo;

--
-- Name: reuniones_registro_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE reuniones_registro_id_seq OWNED BY reuniones_registro.id;


--
-- Name: revision; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE revision (
    repos integer NOT NULL,
    rev text NOT NULL,
    "time" bigint,
    author text,
    message text
);


ALTER TABLE public.revision OWNER TO vbravo;

--
-- Name: session; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE session (
    sid text NOT NULL,
    authenticated integer NOT NULL,
    last_visit integer
);


ALTER TABLE public.session OWNER TO vbravo;

--
-- Name: session_attribute; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE session_attribute (
    sid text NOT NULL,
    authenticated integer NOT NULL,
    name text NOT NULL,
    value text
);


ALTER TABLE public.session_attribute OWNER TO vbravo;

--
-- Name: solicitud_redes; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE solicitud_redes (
    id integer NOT NULL,
    fecha_solicitud integer,
    tipo text,
    cedula_solicitante character(12),
    propietario character(12),
    fecha_resolucion integer,
    fecha_atencion integer,
    observacion text,
    recurso1 integer,
    recurso2 integer,
    recurso3 integer,
    fecha_propuesta integer,
    institucion_vinculada1 integer,
    institucion_vinculada2 integer,
    proyecto integer,
    status character(25),
    tipo_solicitud text
);


ALTER TABLE public.solicitud_redes OWNER TO vbravo;

--
-- Name: solicitud_blog; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE solicitud_blog (
    nombre_blog character(100),
    nombre_web character(160),
    fechallenada integer,
    fechafactible integer,
    fechasolicitadofirmado integer,
    fechaconfigurado integer,
    fechaverificado integer,
    fechaentregado integer,
    fechafinalizado integer,
    rolfactible character(12),
    rolconfigurado character(12),
    rolverificado character(12),
    rolentregado character(12),
    rolfinalizado character(12),
    fechanofactible integer,
    rolnofactible character(12)
)
INHERITS (solicitud_redes);


ALTER TABLE public.solicitud_blog OWNER TO vbravo;

--
-- Name: solicitud_cuentas; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE solicitud_cuentas (
    incluir_correo_electronico boolean,
    incluir_intranet boolean,
    nombres_solicitado text,
    cedula_solicitado character(12)
)
INHERITS (solicitud_redes);


ALTER TABLE public.solicitud_cuentas OWNER TO vbravo;

--
-- Name: solicitud_maquina_virtual; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE solicitud_maquina_virtual (
    memoria_ram_propuesto integer,
    memoria_dd_propuesta integer,
    url_propuesta character(255),
    lista_usuarios text,
    administrador character(12)
)
INHERITS (solicitud_redes);


ALTER TABLE public.solicitud_maquina_virtual OWNER TO vbravo;

--
-- Name: solicitud_redes_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE solicitud_redes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.solicitud_redes_id_seq OWNER TO vbravo;

--
-- Name: solicitud_redes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE solicitud_redes_id_seq OWNED BY solicitud_redes.id;


--
-- Name: solicitud_retiro; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE solicitud_retiro (
    razon_del_retiro character(40),
    fecha_retiro integer,
    incluir_retiro_correo_electronico boolean,
    incluir_retiro_cuenta_intranet boolean
)
INHERITS (solicitud_redes);


ALTER TABLE public.solicitud_retiro OWNER TO vbravo;

--
-- Name: solicitud_trac; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE solicitud_trac (
    nombre_trac text,
    incluir_plugins boolean,
    lista_plugins text,
    administrador character(12)
)
INHERITS (solicitud_redes);


ALTER TABLE public.solicitud_trac OWNER TO vbravo;

--
-- Name: solicitud_wiki; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE solicitud_wiki (
    nombre_wiki text,
    lista_usuarios_internos text,
    administrador character(12),
    titulo_wiki text,
    tipo_vista character(15),
    tipo_edicion character(15),
    lista_usuarios_externos text,
    incluir_usuarios_externos boolean
)
INHERITS (solicitud_redes);


ALTER TABLE public.solicitud_wiki OWNER TO vbravo;

--
-- Name: status_proyecto; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE status_proyecto (
    id integer NOT NULL,
    status text,
    tipo text
);


ALTER TABLE public.status_proyecto OWNER TO vbravo;

--
-- Name: status_proyecto_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE status_proyecto_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.status_proyecto_id_seq OWNER TO vbravo;

--
-- Name: status_proyecto_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE status_proyecto_id_seq OWNED BY status_proyecto.id;


--
-- Name: system; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE system (
    name text NOT NULL,
    value text
);


ALTER TABLE public.system OWNER TO vbravo;

--
-- Name: test; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE test (
    id integer NOT NULL,
    escenario text,
    numero_caso_prueba bigint,
    objetivo text,
    datos_entrada text,
    salida_esperada text,
    observaciones text,
    errores_corregidos text,
    usuario text,
    salida_obtenida text
);


ALTER TABLE public.test OWNER TO vbravo;

--
-- Name: test_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE test_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.test_id_seq OWNER TO vbravo;

--
-- Name: test_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE test_id_seq OWNED BY test.id;


--
-- Name: ticket_change; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE ticket_change (
    ticket integer NOT NULL,
    "time" bigint NOT NULL,
    author text,
    field text NOT NULL,
    oldvalue text,
    newvalue text
);


ALTER TABLE public.ticket_change OWNER TO vbravo;

--
-- Name: ticket_custom; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE ticket_custom (
    ticket integer NOT NULL,
    name text NOT NULL,
    value text
);


ALTER TABLE public.ticket_custom OWNER TO vbravo;

--
-- Name: ticket_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE ticket_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ticket_id_seq OWNER TO vbravo;

--
-- Name: ticket_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE ticket_id_seq OWNED BY ticket.id;


--
-- Name: topic; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE topic (
    id integer NOT NULL,
    forum integer,
    "time" integer,
    author text,
    subscribers text,
    subject text,
    body text
);


ALTER TABLE public.topic OWNER TO vbravo;

--
-- Name: topic_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE topic_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.topic_id_seq OWNER TO vbravo;

--
-- Name: topic_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE topic_id_seq OWNED BY topic.id;


--
-- Name: vacaciones; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE vacaciones (
    id integer NOT NULL,
    id_cedula character(30),
    diasadisfrutar integer,
    diasdisfrutados integer,
    diaspordisfrutar integer,
    fechainicioperiodo integer,
    fechafinperiodo integer,
    fechainicio integer,
    fechafin integer,
    diashabiles integer,
    diasinhabiles integer,
    bonoacancelar real,
    bonoporcancelar real,
    sueldodelmes real,
    sueldoanticipado real,
    status text,
    suplenteinterno_1 text,
    suplenteinterno_2 text,
    observaciones_talento_humano text,
    fechaincorporacion integer,
    fechasolicitud integer,
    totalapagar real,
    informacion_usuario text,
    nombre integer,
    fecha_ingreso integer,
    usuario text,
    observaciones_direccion_ejecutiva text,
    observaciones_presidencia text,
    diasadicionales integer,
    diassolicitados integer,
    cedula_suplente_1 text,
    cedula_suplente_2 text,
    acepta_suplente1 boolean DEFAULT false,
    acepta_suplente2 boolean DEFAULT false
);


ALTER TABLE public.vacaciones OWNER TO vbravo;

--
-- Name: vacaciones_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE vacaciones_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.vacaciones_id_seq OWNER TO vbravo;

--
-- Name: vacaciones_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE vacaciones_id_seq OWNED BY vacaciones.id;


--
-- Name: vacaciones_registro; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE vacaciones_registro (
    id integer NOT NULL,
    id_vacaciones integer NOT NULL,
    propietario text,
    informacion_usuario text,
    nombre_periodo integer,
    fechainicio integer,
    fechafin integer,
    fecha_accion integer,
    status text
);


ALTER TABLE public.vacaciones_registro OWNER TO vbravo;

--
-- Name: vacaciones_registro_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE vacaciones_registro_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.vacaciones_registro_id_seq OWNER TO vbravo;

--
-- Name: vacaciones_registro_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE vacaciones_registro_id_seq OWNED BY vacaciones_registro.id;


--
-- Name: vacaciones_registro_id_vacaciones_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE vacaciones_registro_id_vacaciones_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.vacaciones_registro_id_vacaciones_seq OWNER TO vbravo;

--
-- Name: vacaciones_registro_id_vacaciones_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE vacaciones_registro_id_vacaciones_seq OWNED BY vacaciones_registro.id_vacaciones;


--
-- Name: version; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE version (
    name text NOT NULL,
    "time" bigint,
    description text
);


ALTER TABLE public.version OWNER TO vbravo;

--
-- Name: viatico_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE viatico_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.viatico_id_seq OWNER TO vbravo;

--
-- Name: viaticos; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE viaticos (
    horasalida integer,
    horallegada integer,
    proyecto character(50),
    ciudad character(30),
    pais character(50) DEFAULT 'Venezuela'::bpchar,
    id integer NOT NULL,
    motivo text,
    status character(15),
    cedulaviajero character(10) NOT NULL,
    fechasolicitud integer,
    fechadirector integer,
    fechapresupuesto integer,
    fechapresidente integer,
    cuentapresupuesto text,
    cuentadirector text
);


ALTER TABLE public.viaticos OWNER TO vbravo;

--
-- Name: viaticos_id_seq; Type: SEQUENCE; Schema: public; Owner: vbravo
--

CREATE SEQUENCE viaticos_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.viaticos_id_seq OWNER TO vbravo;

--
-- Name: viaticos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vbravo
--

ALTER SEQUENCE viaticos_id_seq OWNED BY viaticos.id;


--
-- Name: vista_actividad_por_accion; Type: VIEW; Schema: public; Owner: vbravo
--

CREATE VIEW vista_actividad_por_accion AS
    SELECT actividad_por_accion.id, actividad_por_accion.id_codigo_accion AS codigo_accion, actividad_por_accion.nombre, actividad_por_accion.id_accion_especifica, actividad_por_accion.id_equipo_responsable, actividad_por_accion.producto, actividad_por_accion.fecha_entrega, actividad_por_accion.status, actividad_por_accion.resolucion, actividad_por_accion.tipo, actividad_por_accion.fechaplaniteracion, actividad_por_accion.porcentaje, actividad_por_accion.enlace, (SELECT (((personal.apellidos)::text || ', '::text) || (personal.nombres)::text) FROM personal WHERE (personal.id = actividad_por_accion.id_persona_responsable)) AS responsable, (SELECT (((personal.apellidos)::text || ', '::text) || (personal.nombres)::text) FROM personal WHERE (personal.id = actividad_por_accion.id_persona_presidencia)) AS presidencia, actividad_por_accion.tipo_producto, actividad_por_accion.trimestre_entrega, actividad_por_accion.cuantos_productos, (SELECT sum(actividad_registro.porcentaje) AS sum FROM actividad_registro WHERE (((actividad_registro.id_actividad = actividad_por_accion.id) AND (actividad_registro.fechaaccion >= 1357014600)) AND (actividad_registro.fechaaccion <= 1359692940))) AS porcenero, (SELECT sum(actividad_registro.porcentaje) AS sum FROM actividad_registro WHERE (((actividad_registro.id_actividad = actividad_por_accion.id) AND (actividad_registro.fechaaccion > 1359693000)) AND (actividad_registro.fechaaccion <= 1362112140))) AS porcfebrero, (SELECT sum(actividad_registro.porcentaje) AS sum FROM actividad_registro WHERE (((actividad_registro.id_actividad = actividad_por_accion.id) AND (actividad_registro.fechaaccion > 1362112200)) AND (actividad_registro.fechaaccion <= 1364790540))) AS porcmarzo, (SELECT sum(actividad_registro.porcentaje) AS sum FROM actividad_registro WHERE (((actividad_registro.id_actividad = actividad_por_accion.id) AND (actividad_registro.fechaaccion > 1364790600)) AND (actividad_registro.fechaaccion <= 1367382540))) AS porcabril, (SELECT sum(actividad_registro.porcentaje) AS sum FROM actividad_registro WHERE (((actividad_registro.id_actividad = actividad_por_accion.id) AND (actividad_registro.fechaaccion > 1367382600)) AND (actividad_registro.fechaaccion <= 1370060940))) AS porcmayo, (SELECT sum(actividad_registro.porcentaje) AS sum FROM actividad_registro WHERE (((actividad_registro.id_actividad = actividad_por_accion.id) AND (actividad_registro.fechaaccion > 1370061000)) AND (actividad_registro.fechaaccion <= 1372652940))) AS porcjunio, (SELECT sum(actividad_registro.porcentaje) AS sum FROM actividad_registro WHERE (((actividad_registro.id_actividad = actividad_por_accion.id) AND (actividad_registro.fechaaccion > 1372653000)) AND (actividad_registro.fechaaccion <= 1375331340))) AS porcjulio, (SELECT sum(actividad_registro.porcentaje) AS sum FROM actividad_registro WHERE (((actividad_registro.id_actividad = actividad_por_accion.id) AND (actividad_registro.fechaaccion > 1375331400)) AND (actividad_registro.fechaaccion <= 1378009740))) AS porcagosto, (SELECT sum(actividad_registro.porcentaje) AS sum FROM actividad_registro WHERE (((actividad_registro.id_actividad = actividad_por_accion.id) AND (actividad_registro.fechaaccion > 1378009800)) AND (actividad_registro.fechaaccion <= 1380601740))) AS porcseptiembre, (SELECT sum(actividad_registro.porcentaje) AS sum FROM actividad_registro WHERE (((actividad_registro.id_actividad = actividad_por_accion.id) AND (actividad_registro.fechaaccion > 1380601800)) AND (actividad_registro.fechaaccion <= 1383280140))) AS porcoctubre, (SELECT sum(actividad_registro.porcentaje) AS sum FROM actividad_registro WHERE (((actividad_registro.id_actividad = actividad_por_accion.id) AND (actividad_registro.fechaaccion > 1383280200)) AND (actividad_registro.fechaaccion <= 1385872140))) AS porcnoviembre, (SELECT sum(actividad_registro.porcentaje) AS sum FROM actividad_registro WHERE (((actividad_registro.id_actividad = actividad_por_accion.id) AND (actividad_registro.fechaaccion > 1385872200)) AND (actividad_registro.fechaaccion <= 1388550540))) AS porcdiciembre FROM actividad_por_accion;


ALTER TABLE public.vista_actividad_por_accion OWNER TO vbravo;

--
-- Name: vista_actividad_por_accion_consolidado; Type: VIEW; Schema: public; Owner: vbravo
--

CREATE VIEW vista_actividad_por_accion_consolidado AS
    SELECT actividad_por_accion.id, actividad_por_accion.id_codigo_accion AS codigo_accion, actividad_por_accion.nombre, actividad_por_accion.id_accion_especifica, actividad_por_accion.id_equipo_responsable, actividad_por_accion.producto, actividad_por_accion.fecha_entrega, actividad_por_accion.status, actividad_por_accion.resolucion, actividad_por_accion.tipo, actividad_por_accion.fechaplaniteracion, actividad_por_accion.porcentaje, actividad_por_accion.enlace, (SELECT (((personal.apellidos)::text || ', '::text) || (personal.nombres)::text) FROM personal WHERE (personal.id = actividad_por_accion.id_persona_responsable)) AS responsable, (SELECT (((personal.apellidos)::text || ', '::text) || (personal.nombres)::text) FROM personal WHERE (personal.id = actividad_por_accion.id_persona_presidencia)) AS presidencia, actividad_por_accion.tipo_producto, actividad_por_accion.trimestre_entrega, actividad_por_accion.cuantos_productos, (SELECT sum(actividad_registro.porcentaje) AS sum FROM actividad_registro WHERE (((actividad_registro.id_actividad = actividad_por_accion.id) AND (actividad_registro.fechaaccion >= 1357014600)) AND (actividad_registro.fechaaccion <= 1359692940))) AS porcenero, (SELECT sum(actividad_registro.porcentaje) AS sum FROM actividad_registro WHERE (((actividad_registro.id_actividad = actividad_por_accion.id) AND (actividad_registro.fechaaccion > 1359693000)) AND (actividad_registro.fechaaccion <= 1362112140))) AS porcfebrero, (SELECT sum(actividad_registro.porcentaje) AS sum FROM actividad_registro WHERE (((actividad_registro.id_actividad = actividad_por_accion.id) AND (actividad_registro.fechaaccion > 1362112200)) AND (actividad_registro.fechaaccion <= 1364790540))) AS porcmarzo, (SELECT sum(actividad_registro.porcentaje) AS sum FROM actividad_registro WHERE (((actividad_registro.id_actividad = actividad_por_accion.id) AND (actividad_registro.fechaaccion > 1364790600)) AND (actividad_registro.fechaaccion <= 1367382540))) AS porcabril, (SELECT sum(actividad_registro.porcentaje) AS sum FROM actividad_registro WHERE (((actividad_registro.id_actividad = actividad_por_accion.id) AND (actividad_registro.fechaaccion > 1367382600)) AND (actividad_registro.fechaaccion <= 1370060940))) AS porcmayo, (SELECT sum(actividad_registro.porcentaje) AS sum FROM actividad_registro WHERE (((actividad_registro.id_actividad = actividad_por_accion.id) AND (actividad_registro.fechaaccion > 1370061000)) AND (actividad_registro.fechaaccion <= 1372652940))) AS porcjunio, (SELECT sum(actividad_registro.porcentaje) AS sum FROM actividad_registro WHERE (((actividad_registro.id_actividad = actividad_por_accion.id) AND (actividad_registro.fechaaccion > 1372653000)) AND (actividad_registro.fechaaccion <= 1375331340))) AS porcjulio, (SELECT sum(actividad_registro.porcentaje) AS sum FROM actividad_registro WHERE (((actividad_registro.id_actividad = actividad_por_accion.id) AND (actividad_registro.fechaaccion > 1375331400)) AND (actividad_registro.fechaaccion <= 1378009740))) AS porcagosto, (SELECT sum(actividad_registro.porcentaje) AS sum FROM actividad_registro WHERE (((actividad_registro.id_actividad = actividad_por_accion.id) AND (actividad_registro.fechaaccion > 1378009800)) AND (actividad_registro.fechaaccion <= 1380601740))) AS porcseptiembre, (SELECT sum(actividad_registro.porcentaje) AS sum FROM actividad_registro WHERE (((actividad_registro.id_actividad = actividad_por_accion.id) AND (actividad_registro.fechaaccion > 1380601800)) AND (actividad_registro.fechaaccion <= 1383280140))) AS porcoctubre, (SELECT sum(actividad_registro.porcentaje) AS sum FROM actividad_registro WHERE (((actividad_registro.id_actividad = actividad_por_accion.id) AND (actividad_registro.fechaaccion > 1383280200)) AND (actividad_registro.fechaaccion <= 1385872140))) AS porcnoviembre, (SELECT sum(actividad_registro.porcentaje) AS sum FROM actividad_registro WHERE (((actividad_registro.id_actividad = actividad_por_accion.id) AND (actividad_registro.fechaaccion > 1385872200)) AND (actividad_registro.fechaaccion <= 1388550540))) AS porcdiciembre FROM actividad_por_accion;


ALTER TABLE public.vista_actividad_por_accion_consolidado OWNER TO vbravo;

--
-- Name: vista_vacaciones; Type: VIEW; Schema: public; Owner: vbravo
--

CREATE VIEW vista_vacaciones AS
    SELECT vacaciones.id, vacaciones.id_cedula, vacaciones.diasadisfrutar, (((personal.nombres)::text || ', '::text) || (personal.apellidos)::text) AS nombreapellido, personal.cargo, personal.departamento, (SELECT personal.cargo FROM personal WHERE ((personal.cedula)::text = vacaciones.cedula_suplente_1)) AS cargo_1, (SELECT personal.cargo FROM personal WHERE ((personal.cedula)::text = vacaciones.cedula_suplente_2)) AS cargo_2, vacaciones.diasdisfrutados, vacaciones.diaspordisfrutar, vacaciones.fechainicioperiodo, vacaciones.fechafinperiodo, vacaciones.fechainicio, vacaciones.fechafin, vacaciones.diashabiles, vacaciones.diasinhabiles, vacaciones.bonoacancelar, vacaciones.bonoporcancelar, vacaciones.sueldodelmes, vacaciones.sueldoanticipado, vacaciones.status, vacaciones.suplenteinterno_1, vacaciones.suplenteinterno_2, vacaciones.observaciones_talento_humano, vacaciones.fechaincorporacion, vacaciones.fechasolicitud, vacaciones.totalapagar, vacaciones.informacion_usuario, vacaciones.nombre, personal.fecha_ingreso, personal.usuario, vacaciones.observaciones_direccion_ejecutiva, vacaciones.observaciones_presidencia, vacaciones.diasadicionales, vacaciones.diassolicitados, vacaciones.cedula_suplente_1, vacaciones.cedula_suplente_2, vacaciones.acepta_suplente1, vacaciones.acepta_suplente2 FROM (vacaciones JOIN personal ON ((vacaciones.id_cedula = personal.cedula)));


ALTER TABLE public.vista_vacaciones OWNER TO vbravo;

--
-- Name: wiki; Type: TABLE; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE TABLE wiki (
    name text NOT NULL,
    version integer NOT NULL,
    "time" bigint,
    author text,
    ipnr text,
    text text,
    comment text,
    readonly integer
);


ALTER TABLE public.wiki OWNER TO vbravo;

--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY accion_especifica ALTER COLUMN id SET DEFAULT nextval('accion_especifica_id_seq'::regclass);


--
-- Name: id_proyecto_poa; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY accion_especifica ALTER COLUMN id_proyecto_poa SET DEFAULT nextval('accion_especifica_id_proyecto_poa_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY actividad_por_accion ALTER COLUMN id SET DEFAULT nextval('actividad_por_accion_id_seq'::regclass);


--
-- Name: id_accion_especifica; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY actividad_por_accion ALTER COLUMN id_accion_especifica SET DEFAULT nextval('actividad_por_accion_id_accion_especifica_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY actividad_registro ALTER COLUMN id SET DEFAULT nextval('actividad_registro_id_seq'::regclass);


--
-- Name: id_actividad; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY actividad_registro ALTER COLUMN id_actividad SET DEFAULT nextval('actividad_registro_id_actividad_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY adjuntos ALTER COLUMN id SET DEFAULT nextval('adjuntos_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY architecture ALTER COLUMN id SET DEFAULT nextval('architecture_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY confirmado_reunion ALTER COLUMN id SET DEFAULT nextval('confirmado_reunion_id_seq'::regclass);


--
-- Name: id_reunion; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY confirmado_reunion ALTER COLUMN id_reunion SET DEFAULT nextval('confirmado_reunion_id_reunion_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY consejero_reunion ALTER COLUMN id SET DEFAULT nextval('consejero_reunion_id_seq'::regclass);


--
-- Name: id_reunion; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY consejero_reunion ALTER COLUMN id_reunion SET DEFAULT nextval('consejero_reunion_id_reunion_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY correspondencia ALTER COLUMN id SET DEFAULT nextval('correspondencia_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY correspondencia_registro ALTER COLUMN id SET DEFAULT nextval('correspondencia_registro_id_seq'::regclass);


--
-- Name: id_correspondencia; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY correspondencia_registro ALTER COLUMN id_correspondencia SET DEFAULT nextval('correspondencia_registro_id_correspondencia_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY download ALTER COLUMN id SET DEFAULT nextval('download_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY download_type ALTER COLUMN id SET DEFAULT nextval('download_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY equipo_personal ALTER COLUMN id SET DEFAULT nextval('equipo_personal_id_seq'::regclass);


--
-- Name: id_equipo; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY equipo_personal ALTER COLUMN id_equipo SET DEFAULT nextval('equipo_personal_id_equipo_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY equipo_responsable ALTER COLUMN id SET DEFAULT nextval('equipo_responsable_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY estado_de_actividad ALTER COLUMN id SET DEFAULT nextval('estado_de_actividad_id_seq'::regclass);


--
-- Name: id_actividad; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY estado_de_actividad ALTER COLUMN id_actividad SET DEFAULT nextval('estado_de_actividad_id_actividad_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY forum ALTER COLUMN id SET DEFAULT nextval('forum_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY forum_group ALTER COLUMN id SET DEFAULT nextval('forum_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY message ALTER COLUMN id SET DEFAULT nextval('message_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY personal ALTER COLUMN id SET DEFAULT nextval('personal_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY platform ALTER COLUMN id SET DEFAULT nextval('platform_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY porcentaje_producto ALTER COLUMN id SET DEFAULT nextval('porcentaje_producto_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY prestaciones ALTER COLUMN id SET DEFAULT nextval('prestaciones_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY prestaciones_registro ALTER COLUMN id SET DEFAULT nextval('prestaciones_registro_id_seq'::regclass);


--
-- Name: id_prestaciones; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY prestaciones_registro ALTER COLUMN id_prestaciones SET DEFAULT nextval('prestaciones_registro_id_prestaciones_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY producto_de_actividad ALTER COLUMN id SET DEFAULT nextval('producto_de_actividad_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY proyecto_extra_poa ALTER COLUMN id SET DEFAULT nextval('proyecto_extra_poa_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY proyecto_poa ALTER COLUMN id SET DEFAULT nextval('proyecto_poa_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY recursos ALTER COLUMN id SET DEFAULT nextval('recursos_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY report ALTER COLUMN id SET DEFAULT nextval('report_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY reuniones ALTER COLUMN id SET DEFAULT nextval('reuniones_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY reuniones_registro ALTER COLUMN id SET DEFAULT nextval('reuniones_registro_id_seq'::regclass);


--
-- Name: id_reuniones; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY reuniones_registro ALTER COLUMN id_reuniones SET DEFAULT nextval('reuniones_registro_id_reuniones_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY solicitud_blog ALTER COLUMN id SET DEFAULT nextval('solicitud_redes_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY solicitud_cuentas ALTER COLUMN id SET DEFAULT nextval('solicitud_redes_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY solicitud_maquina_virtual ALTER COLUMN id SET DEFAULT nextval('solicitud_redes_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY solicitud_redes ALTER COLUMN id SET DEFAULT nextval('solicitud_redes_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY solicitud_retiro ALTER COLUMN id SET DEFAULT nextval('solicitud_redes_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY solicitud_trac ALTER COLUMN id SET DEFAULT nextval('solicitud_redes_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY solicitud_wiki ALTER COLUMN id SET DEFAULT nextval('solicitud_redes_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY status_proyecto ALTER COLUMN id SET DEFAULT nextval('status_proyecto_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY test ALTER COLUMN id SET DEFAULT nextval('test_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY ticket ALTER COLUMN id SET DEFAULT nextval('ticket_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY topic ALTER COLUMN id SET DEFAULT nextval('topic_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY vacaciones ALTER COLUMN id SET DEFAULT nextval('vacaciones_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY vacaciones_registro ALTER COLUMN id SET DEFAULT nextval('vacaciones_registro_id_seq'::regclass);


--
-- Name: id_vacaciones; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY vacaciones_registro ALTER COLUMN id_vacaciones SET DEFAULT nextval('vacaciones_registro_id_vacaciones_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY viaticos ALTER COLUMN id SET DEFAULT nextval('viaticos_id_seq'::regclass);


--
-- Name: accion_especifica_pk; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY accion_especifica
    ADD CONSTRAINT accion_especifica_pk PRIMARY KEY (id);


--
-- Name: actividad_por_accion_pk; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY actividad_por_accion
    ADD CONSTRAINT actividad_por_accion_pk PRIMARY KEY (id);


--
-- Name: adjuntos_pkey; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY adjuntos
    ADD CONSTRAINT adjuntos_pkey PRIMARY KEY (id);


--
-- Name: architecture_pkey; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY architecture
    ADD CONSTRAINT architecture_pkey PRIMARY KEY (id);


--
-- Name: assessments_pkey; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY assessments
    ADD CONSTRAINT assessments_pkey PRIMARY KEY (username, id_ticket);


--
-- Name: attachment_pk; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY attachment
    ADD CONSTRAINT attachment_pk PRIMARY KEY (type, id, filename);


--
-- Name: auth_cookie_pk; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY auth_cookie
    ADD CONSTRAINT auth_cookie_pk PRIMARY KEY (cookie, ipnr, name);


--
-- Name: cache_pkey; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY cache
    ADD CONSTRAINT cache_pkey PRIMARY KEY (id);


--
-- Name: calendario_pkey; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY calendario
    ADD CONSTRAINT calendario_pkey PRIMARY KEY (id);


--
-- Name: component_pkey; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY component
    ADD CONSTRAINT component_pkey PRIMARY KEY (name);


--
-- Name: confirmado; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY confirmado_reunion
    ADD CONSTRAINT confirmado PRIMARY KEY (id);


--
-- Name: confirmado_id_reunion; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY confirmado_reunion
    ADD CONSTRAINT confirmado_id_reunion UNIQUE (id_reunion, id_personal);


--
-- Name: download_pkey; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY download
    ADD CONSTRAINT download_pkey PRIMARY KEY (id);


--
-- Name: download_type_pkey; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY download_type
    ADD CONSTRAINT download_type_pkey PRIMARY KEY (id);


--
-- Name: enum_pk; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY enum
    ADD CONSTRAINT enum_pk PRIMARY KEY (type, name);


--
-- Name: equipo_personal_id_equipo_key; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY equipo_personal
    ADD CONSTRAINT equipo_personal_id_equipo_key UNIQUE (id_equipo, id_personal);


--
-- Name: equipo_personal_pk; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY equipo_personal
    ADD CONSTRAINT equipo_personal_pk PRIMARY KEY (id);


--
-- Name: equipo_responsable_pk; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY equipo_responsable
    ADD CONSTRAINT equipo_responsable_pk PRIMARY KEY (id);


--
-- Name: estado_de_actividad_pkey; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY estado_de_actividad
    ADD CONSTRAINT estado_de_actividad_pkey PRIMARY KEY (id);


--
-- Name: forum_group_pkey; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY forum_group
    ADD CONSTRAINT forum_group_pkey PRIMARY KEY (id);


--
-- Name: forum_pkey; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY forum
    ADD CONSTRAINT forum_pkey PRIMARY KEY (id);


--
-- Name: id; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY porcentaje_producto
    ADD CONSTRAINT id PRIMARY KEY (id);


--
-- Name: id_correspondencia; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY correspondencia
    ADD CONSTRAINT id_correspondencia PRIMARY KEY (id);


--
-- Name: id_correspondencia_registro; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY correspondencia_registro
    ADD CONSTRAINT id_correspondencia_registro PRIMARY KEY (id);


--
-- Name: id_periodo; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY vacaciones
    ADD CONSTRAINT id_periodo PRIMARY KEY (id);


--
-- Name: id_prestaciones; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY prestaciones
    ADD CONSTRAINT id_prestaciones PRIMARY KEY (id);


--
-- Name: id_solicitud_prestaciones; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY prestaciones_registro
    ADD CONSTRAINT id_solicitud_prestaciones PRIMARY KEY (id);


--
-- Name: id_status; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY status_proyecto
    ADD CONSTRAINT id_status PRIMARY KEY (id);


--
-- Name: id_vacaciones_registro; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY vacaciones_registro
    ADD CONSTRAINT id_vacaciones_registro PRIMARY KEY (id);


--
-- Name: message_pkey; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY message
    ADD CONSTRAINT message_pkey PRIMARY KEY (id);


--
-- Name: milestone_pkey; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY milestone
    ADD CONSTRAINT milestone_pkey PRIMARY KEY (name);


--
-- Name: node_change_pk; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY node_change
    ADD CONSTRAINT node_change_pk PRIMARY KEY (repos, rev, path, change_type);


--
-- Name: permission_pk; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY permission
    ADD CONSTRAINT permission_pk PRIMARY KEY (username, action);


--
-- Name: pk_actividad_registro_id; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY actividad_registro
    ADD CONSTRAINT pk_actividad_registro_id PRIMARY KEY (id);


--
-- Name: pk_cedula; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY personal
    ADD CONSTRAINT pk_cedula PRIMARY KEY (cedula);


--
-- Name: pk_id; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY viaticos
    ADD CONSTRAINT pk_id PRIMARY KEY (id);


--
-- Name: pk_institucion_id; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY institucion
    ADD CONSTRAINT pk_institucion_id PRIMARY KEY (id);


--
-- Name: pk_proyectos_id; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY proyectos
    ADD CONSTRAINT pk_proyectos_id PRIMARY KEY (id);


--
-- Name: pk_recurso_id; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY recursos
    ADD CONSTRAINT pk_recurso_id PRIMARY KEY (id);


--
-- Name: pk_solicitud_blog_id; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY solicitud_blog
    ADD CONSTRAINT pk_solicitud_blog_id PRIMARY KEY (id);


--
-- Name: pk_solicitud_cuentas; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY solicitud_cuentas
    ADD CONSTRAINT pk_solicitud_cuentas PRIMARY KEY (id);


--
-- Name: pk_solicitud_maquina_virtual_id; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY solicitud_maquina_virtual
    ADD CONSTRAINT pk_solicitud_maquina_virtual_id PRIMARY KEY (id);


--
-- Name: pk_solicitud_redes_id; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY solicitud_redes
    ADD CONSTRAINT pk_solicitud_redes_id PRIMARY KEY (id);


--
-- Name: pk_solicitud_retiro; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY solicitud_retiro
    ADD CONSTRAINT pk_solicitud_retiro PRIMARY KEY (id);


--
-- Name: pk_solicitud_trac_id; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY solicitud_trac
    ADD CONSTRAINT pk_solicitud_trac_id PRIMARY KEY (id);


--
-- Name: pk_solicitud_wiki; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY solicitud_wiki
    ADD CONSTRAINT pk_solicitud_wiki PRIMARY KEY (id);


--
-- Name: platform_pkey; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY platform
    ADD CONSTRAINT platform_pkey PRIMARY KEY (id);


--
-- Name: producto_de_actividad_pk; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY producto_de_actividad
    ADD CONSTRAINT producto_de_actividad_pk PRIMARY KEY (id);


--
-- Name: proyecto_poa_pk; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY proyecto_poa
    ADD CONSTRAINT proyecto_poa_pk PRIMARY KEY (id);


--
-- Name: report_pkey; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY report
    ADD CONSTRAINT report_pkey PRIMARY KEY (id);


--
-- Name: repository_pk; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY repository
    ADD CONSTRAINT repository_pk PRIMARY KEY (id, name);


--
-- Name: reunion_consejero; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY consejero_reunion
    ADD CONSTRAINT reunion_consejero PRIMARY KEY (id);


--
-- Name: reunion_consejero_id_reunion; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY consejero_reunion
    ADD CONSTRAINT reunion_consejero_id_reunion UNIQUE (id_reunion, id_personal);


--
-- Name: reuniones_codigo_key; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY reuniones
    ADD CONSTRAINT reuniones_codigo_key UNIQUE (codigo);


--
-- Name: reuniones_codigo_unico; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY reuniones
    ADD CONSTRAINT reuniones_codigo_unico UNIQUE (codigo);


--
-- Name: reuniones_pk; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY reuniones
    ADD CONSTRAINT reuniones_pk PRIMARY KEY (id);


--
-- Name: reuniones_registro_pk; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY reuniones_registro
    ADD CONSTRAINT reuniones_registro_pk PRIMARY KEY (id);


--
-- Name: revision_pk; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY revision
    ADD CONSTRAINT revision_pk PRIMARY KEY (repos, rev);


--
-- Name: session_attribute_pk; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY session_attribute
    ADD CONSTRAINT session_attribute_pk PRIMARY KEY (sid, authenticated, name);


--
-- Name: session_pk; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY session
    ADD CONSTRAINT session_pk PRIMARY KEY (sid, authenticated);


--
-- Name: system_pkey; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY system
    ADD CONSTRAINT system_pkey PRIMARY KEY (name);


--
-- Name: test_pkey; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY test
    ADD CONSTRAINT test_pkey PRIMARY KEY (id);


--
-- Name: ticket_change_pk; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY ticket_change
    ADD CONSTRAINT ticket_change_pk PRIMARY KEY (ticket, "time", field);


--
-- Name: ticket_custom_pk; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY ticket_custom
    ADD CONSTRAINT ticket_custom_pk PRIMARY KEY (ticket, name);


--
-- Name: ticket_pkey; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY ticket
    ADD CONSTRAINT ticket_pkey PRIMARY KEY (id);


--
-- Name: topic_pkey; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY topic
    ADD CONSTRAINT topic_pkey PRIMARY KEY (id);


--
-- Name: version_pkey; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY version
    ADD CONSTRAINT version_pkey PRIMARY KEY (name);


--
-- Name: wiki_pk; Type: CONSTRAINT; Schema: public; Owner: vbravo; Tablespace: 
--

ALTER TABLE ONLY wiki
    ADD CONSTRAINT wiki_pk PRIMARY KEY (name, version);


--
-- Name: indexestado; Type: INDEX; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE INDEX indexestado ON actividad_registro USING btree (estado);


--
-- Name: indexforid; Type: INDEX; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE INDEX indexforid ON actividad_por_accion USING btree (id NULLS FIRST);


--
-- Name: indexforidandstatus; Type: INDEX; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE INDEX indexforidandstatus ON actividad_por_accion USING btree (id, status);


--
-- Name: indexforidtipostatus; Type: INDEX; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE INDEX indexforidtipostatus ON actividad_por_accion USING btree (id NULLS FIRST, tipo, status);


--
-- Name: indexforregistroid; Type: INDEX; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE INDEX indexforregistroid ON actividad_registro USING btree (id);


--
-- Name: indexforstatus; Type: INDEX; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE INDEX indexforstatus ON actividad_por_accion USING btree (status);


--
-- Name: indexfortipo; Type: INDEX; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE INDEX indexfortipo ON actividad_por_accion USING btree (tipo NULLS FIRST);


--
-- Name: indexid_actividad; Type: INDEX; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE INDEX indexid_actividad ON actividad_registro USING btree (id_actividad);


--
-- Name: node_change_repos_rev_idx; Type: INDEX; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE INDEX node_change_repos_rev_idx ON node_change USING btree (repos, rev);


--
-- Name: revision_repos_time_idx; Type: INDEX; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE INDEX revision_repos_time_idx ON revision USING btree (repos, "time");


--
-- Name: session_authenticated_idx; Type: INDEX; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE INDEX session_authenticated_idx ON session USING btree (authenticated);


--
-- Name: session_last_visit_idx; Type: INDEX; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE INDEX session_last_visit_idx ON session USING btree (last_visit);


--
-- Name: ticket_change_ticket_idx; Type: INDEX; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE INDEX ticket_change_ticket_idx ON ticket_change USING btree (ticket);


--
-- Name: ticket_change_time_idx; Type: INDEX; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE INDEX ticket_change_time_idx ON ticket_change USING btree ("time");


--
-- Name: ticket_status_idx; Type: INDEX; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE INDEX ticket_status_idx ON ticket USING btree (status);


--
-- Name: ticket_time_idx; Type: INDEX; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE INDEX ticket_time_idx ON ticket USING btree ("time");


--
-- Name: wiki_time_idx; Type: INDEX; Schema: public; Owner: vbravo; Tablespace: 
--

CREATE INDEX wiki_time_idx ON wiki USING btree ("time");


--
-- Name: accion_especifica_fkey1; Type: FK CONSTRAINT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY accion_especifica
    ADD CONSTRAINT accion_especifica_fkey1 FOREIGN KEY (id_proyecto_poa) REFERENCES proyecto_poa(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: actividad_por_accion_fkey2; Type: FK CONSTRAINT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY actividad_por_accion
    ADD CONSTRAINT actividad_por_accion_fkey2 FOREIGN KEY (id_accion_especifica) REFERENCES accion_especifica(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: id_producto_de_actividad; Type: FK CONSTRAINT; Schema: public; Owner: vbravo
--

ALTER TABLE ONLY porcentaje_producto
    ADD CONSTRAINT id_producto_de_actividad FOREIGN KEY (id_producto_de_actividad) REFERENCES producto_de_actividad(id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

