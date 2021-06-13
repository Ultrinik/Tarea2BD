PGDMP     
                    y            Tarea1    13.1    13.1     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16666    Tarea1    DATABASE     d   CREATE DATABASE "Tarea1" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Spanish_Chile.1252';
    DROP DATABASE "Tarea1";
                postgres    false            �            1259    16700    cuenta_bancaria    TABLE     �   CREATE TABLE public.cuenta_bancaria (
    numero_cuenta integer NOT NULL,
    id_usuario integer NOT NULL,
    balance numeric NOT NULL
);
 #   DROP TABLE public.cuenta_bancaria;
       public         heap    postgres    false            �            1259    16672    moneda    TABLE     �   CREATE TABLE public.moneda (
    id integer NOT NULL,
    sigla character varying(10) NOT NULL,
    nombre character varying(80) NOT NULL
);
    DROP TABLE public.moneda;
       public         heap    postgres    false            �            1259    16667    pais    TABLE     g   CREATE TABLE public.pais (
    cod_pais integer NOT NULL,
    nombre character varying(45) NOT NULL
);
    DROP TABLE public.pais;
       public         heap    postgres    false            �            1259    16677    precio_moneda    TABLE     �   CREATE TABLE public.precio_moneda (
    id_moneda integer NOT NULL,
    fecha timestamp without time zone NOT NULL,
    valor numeric NOT NULL
);
 !   DROP TABLE public.precio_moneda;
       public         heap    postgres    false            �            1259    16690    usuario    TABLE     9  CREATE TABLE public.usuario (
    id integer NOT NULL,
    nombre character varying(50) NOT NULL,
    apellido character varying(50),
    correo character varying(50) NOT NULL,
    "contraseña" character varying(50) NOT NULL,
    pais integer NOT NULL,
    fecha_registro timestamp without time zone NOT NULL
);
    DROP TABLE public.usuario;
       public         heap    postgres    false            �            1259    16713    usuario_tiene_moneda    TABLE     �   CREATE TABLE public.usuario_tiene_moneda (
    id_usuario integer NOT NULL,
    id_moneda integer NOT NULL,
    balance numeric NOT NULL
);
 (   DROP TABLE public.usuario_tiene_moneda;
       public         heap    postgres    false            �          0    16700    cuenta_bancaria 
   TABLE DATA           M   COPY public.cuenta_bancaria (numero_cuenta, id_usuario, balance) FROM stdin;
    public          postgres    false    204            �          0    16672    moneda 
   TABLE DATA           3   COPY public.moneda (id, sigla, nombre) FROM stdin;
    public          postgres    false    201   =        �          0    16667    pais 
   TABLE DATA           0   COPY public.pais (cod_pais, nombre) FROM stdin;
    public          postgres    false    200   Z        �          0    16677    precio_moneda 
   TABLE DATA           @   COPY public.precio_moneda (id_moneda, fecha, valor) FROM stdin;
    public          postgres    false    202   w        �          0    16690    usuario 
   TABLE DATA           d   COPY public.usuario (id, nombre, apellido, correo, "contraseña", pais, fecha_registro) FROM stdin;
    public          postgres    false    203   �        �          0    16713    usuario_tiene_moneda 
   TABLE DATA           N   COPY public.usuario_tiene_moneda (id_usuario, id_moneda, balance) FROM stdin;
    public          postgres    false    205   �        @           2606    16707 $   cuenta_bancaria cuenta_bancaria_pkey 
   CONSTRAINT     m   ALTER TABLE ONLY public.cuenta_bancaria
    ADD CONSTRAINT cuenta_bancaria_pkey PRIMARY KEY (numero_cuenta);
 N   ALTER TABLE ONLY public.cuenta_bancaria DROP CONSTRAINT cuenta_bancaria_pkey;
       public            postgres    false    204            :           2606    16676    moneda moneda_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.moneda
    ADD CONSTRAINT moneda_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.moneda DROP CONSTRAINT moneda_pkey;
       public            postgres    false    201            8           2606    16671    pais pais_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.pais
    ADD CONSTRAINT pais_pkey PRIMARY KEY (cod_pais);
 8   ALTER TABLE ONLY public.pais DROP CONSTRAINT pais_pkey;
       public            postgres    false    200            <           2606    16684     precio_moneda precio_moneda_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public.precio_moneda
    ADD CONSTRAINT precio_moneda_pkey PRIMARY KEY (id_moneda, fecha);
 J   ALTER TABLE ONLY public.precio_moneda DROP CONSTRAINT precio_moneda_pkey;
       public            postgres    false    202    202            >           2606    16694    usuario usuario_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.usuario DROP CONSTRAINT usuario_pkey;
       public            postgres    false    203            B           2606    16720 .   usuario_tiene_moneda usuario_tiene_moneda_pkey 
   CONSTRAINT        ALTER TABLE ONLY public.usuario_tiene_moneda
    ADD CONSTRAINT usuario_tiene_moneda_pkey PRIMARY KEY (id_usuario, id_moneda);
 X   ALTER TABLE ONLY public.usuario_tiene_moneda DROP CONSTRAINT usuario_tiene_moneda_pkey;
       public            postgres    false    205    205            E           2606    16708 /   cuenta_bancaria cuenta_bancaria_id_usuario_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.cuenta_bancaria
    ADD CONSTRAINT cuenta_bancaria_id_usuario_fkey FOREIGN KEY (id_usuario) REFERENCES public.usuario(id);
 Y   ALTER TABLE ONLY public.cuenta_bancaria DROP CONSTRAINT cuenta_bancaria_id_usuario_fkey;
       public          postgres    false    2878    203    204            C           2606    16685 *   precio_moneda precio_moneda_id_moneda_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.precio_moneda
    ADD CONSTRAINT precio_moneda_id_moneda_fkey FOREIGN KEY (id_moneda) REFERENCES public.moneda(id);
 T   ALTER TABLE ONLY public.precio_moneda DROP CONSTRAINT precio_moneda_id_moneda_fkey;
       public          postgres    false    2874    202    201            D           2606    16695    usuario usuario_pais_fkey    FK CONSTRAINT     z   ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_pais_fkey FOREIGN KEY (pais) REFERENCES public.pais(cod_pais);
 C   ALTER TABLE ONLY public.usuario DROP CONSTRAINT usuario_pais_fkey;
       public          postgres    false    2872    203    200            G           2606    16726 8   usuario_tiene_moneda usuario_tiene_moneda_id_moneda_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.usuario_tiene_moneda
    ADD CONSTRAINT usuario_tiene_moneda_id_moneda_fkey FOREIGN KEY (id_moneda) REFERENCES public.moneda(id);
 b   ALTER TABLE ONLY public.usuario_tiene_moneda DROP CONSTRAINT usuario_tiene_moneda_id_moneda_fkey;
       public          postgres    false    2874    201    205            F           2606    16721 9   usuario_tiene_moneda usuario_tiene_moneda_id_usuario_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.usuario_tiene_moneda
    ADD CONSTRAINT usuario_tiene_moneda_id_usuario_fkey FOREIGN KEY (id_usuario) REFERENCES public.usuario(id);
 c   ALTER TABLE ONLY public.usuario_tiene_moneda DROP CONSTRAINT usuario_tiene_moneda_id_usuario_fkey;
       public          postgres    false    203    205    2878            �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �     