--
-- PostgreSQL database dump
--

\restrict EuhmdmchXbBBcDlAaPlznTdp48KLPAbgCfK4z0I6q8eic7yi9Y3xxT1Axcy5KVm

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatia_mea_categorie; Type: TABLE DATA; Schema: django; Owner: maria
--

INSERT INTO django.aplicatia_mea_categorie (nume_categorie, descriere, id, iconita) VALUES ('Apa de parfum', 'Concentratie ridicata de uleiuri esentiale.', 1, 'fa-magic');
INSERT INTO django.aplicatia_mea_categorie (nume_categorie, descriere, id, iconita) VALUES ('Apa de toaleta', 'Ideala pentru utilizarea zilnica.', 2, 'fa-wind');
INSERT INTO django.aplicatia_mea_categorie (nume_categorie, descriere, id, iconita) VALUES ('Ulei parfumat', 'Persistenta maxima pe piele.', 3, 'fa-droplet');


--
-- Name: aplicatia_mea_categorie_id_seq; Type: SEQUENCE SET; Schema: django; Owner: maria
--

SELECT pg_catalog.setval('django.aplicatia_mea_categorie_id_seq', 3, true);


--
-- PostgreSQL database dump complete
--

\unrestrict EuhmdmchXbBBcDlAaPlznTdp48KLPAbgCfK4z0I6q8eic7yi9Y3xxT1Axcy5KVm

--
-- PostgreSQL database dump
--

\restrict mZncU35KKk2BW3fvUNWXl8RSuXC7fTOzwciUWPvtD8LF7bYoS8mwItOMqkzZ6MG

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatia_mea_furnizor; Type: TABLE DATA; Schema: django; Owner: maria
--

INSERT INTO django.aplicatia_mea_furnizor (id_brand, nume_brand, tara, telefon, este_premium) VALUES (1, 'Chanel', 'Franta', '0722111222', true);
INSERT INTO django.aplicatia_mea_furnizor (id_brand, nume_brand, tara, telefon, este_premium) VALUES (2, 'Dior', 'Franta', '0722333444', true);
INSERT INTO django.aplicatia_mea_furnizor (id_brand, nume_brand, tara, telefon, este_premium) VALUES (3, 'Tom Ford', 'USA', '0744555666', true);
INSERT INTO django.aplicatia_mea_furnizor (id_brand, nume_brand, tara, telefon, este_premium) VALUES (4, 'Versace', 'Italia', '0755777888', false);
INSERT INTO django.aplicatia_mea_furnizor (id_brand, nume_brand, tara, telefon, este_premium) VALUES (5, 'Armani', 'Italia', '0766999000', true);
INSERT INTO django.aplicatia_mea_furnizor (id_brand, nume_brand, tara, telefon, este_premium) VALUES (6, 'Calvin Klein', 'SUA', NULL, false);
INSERT INTO django.aplicatia_mea_furnizor (id_brand, nume_brand, tara, telefon, este_premium) VALUES (7, 'Sol de Janeiro', 'Brazilia', NULL, false);
INSERT INTO django.aplicatia_mea_furnizor (id_brand, nume_brand, tara, telefon, este_premium) VALUES (8, 'Jean Paul Gaultier', 'Franta', NULL, true);
INSERT INTO django.aplicatia_mea_furnizor (id_brand, nume_brand, tara, telefon, este_premium) VALUES (9, 'Lattafa', 'Emiratele Arabe Unite', NULL, false);


--
-- Name: aplicatia_mea_furnizor_id_brand_seq; Type: SEQUENCE SET; Schema: django; Owner: maria
--

SELECT pg_catalog.setval('django.aplicatia_mea_furnizor_id_brand_seq', 9, true);


--
-- PostgreSQL database dump complete
--

\unrestrict mZncU35KKk2BW3fvUNWXl8RSuXC7fTOzwciUWPvtD8LF7bYoS8mwItOMqkzZ6MG

--
-- PostgreSQL database dump
--

\restrict cdKGwvF2MZA4rKvkjVoaq6GjXqEbO7gXdAsKE0HRZlkAjJkh1haDxYrkqEzGqb3

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatia_mea_parfum; Type: TABLE DATA; Schema: django; Owner: maria
--

INSERT INTO django.aplicatia_mea_parfum (id_parfum, descriere, pret, gen_parfum, volum, imagine, nume_parfum, nume_categorie_id) VALUES (1, 'O aroma clasica, simbolul elegantei feminine.', 550.00, 'Dame', 50, 'parfumuri/chanel5.jpg', 'Chanel No 5', 1);
INSERT INTO django.aplicatia_mea_parfum (id_parfum, descriere, pret, gen_parfum, volum, imagine, nume_parfum, nume_categorie_id) VALUES (2, 'Esență masculină cu note puternice de cedru.', 420.00, 'Barbatesc', 100, 'parfumuri/sauvage.jpg', 'Dior Sauvage', 1);
INSERT INTO django.aplicatia_mea_parfum (id_parfum, descriere, pret, gen_parfum, volum, imagine, nume_parfum, nume_categorie_id) VALUES (3, 'Parfum de nisa cu note de tabac si vanilie.', 890.00, 'Unisex', 50, 'parfumuri/tobacco_vanille.png', 'Tobacco Vanille', 1);
INSERT INTO django.aplicatia_mea_parfum (id_parfum, descriere, pret, gen_parfum, volum, imagine, nume_parfum, nume_categorie_id) VALUES (4, 'Un amestec proaspat de flori de portocal si iasomie.', 350.00, 'Dame', 30, 'parfumuri/miss_dior.webp', 'Miss Dior', 1);
INSERT INTO django.aplicatia_mea_parfum (id_parfum, descriere, pret, gen_parfum, volum, imagine, nume_parfum, nume_categorie_id) VALUES (5, 'Eleganta italiana intr-o sticluta cu note marine.', 480.00, 'Barbatesc', 75, 'parfumuri/aqua_di_gio.jpg', 'Aqua di Gio', 1);
INSERT INTO django.aplicatia_mea_parfum (id_parfum, descriere, pret, gen_parfum, volum, imagine, nume_parfum, nume_categorie_id) VALUES (7, 'Un buchet in care toate florile se imbina armonios, oferind senzatia unei flori ideale purtata de note care trec de la senzual la catifelat, proaspat sau fructat.', 900.00, 'Dame', 100, 'parfumuri/jadore_iNF9BMn.jpg', 'Dior J''adore', 1);
INSERT INTO django.aplicatia_mea_parfum (id_parfum, descriere, pret, gen_parfum, volum, imagine, nume_parfum, nume_categorie_id) VALUES (8, 'Apa de toaleta unisex Calvin Klein CK One Gold se distinge printr-o aroma tinereasca si lemnoasa, care combina forta ambelor sexe.', 160.00, 'Unisex', 200, 'parfumuri/ck_one_gold_m8697il.webp', 'CK One Gold', 2);
INSERT INTO django.aplicatia_mea_parfum (id_parfum, descriere, pret, gen_parfum, volum, imagine, nume_parfum, nume_categorie_id) VALUES (9, 'O distractie fara sfarsit si o energie molipsitoare – toate acestea le veti regasi in senzualul parfum pentru corp, inspirat de insorita Brazilie.', 200.00, 'Dame', 240, 'parfumuri/sol_de_janeiro62_LAHDNgC.webp', 'Sol de Janeiro ''62', 2);
INSERT INTO django.aplicatia_mea_parfum (id_parfum, descriere, pret, gen_parfum, volum, imagine, nume_parfum, nume_categorie_id) VALUES (10, 'Un must-have pentru femei.', 840.00, 'Dame', 80, 'parfumuri/scandal_ppUAVYV.jpg', 'Scandal le Parfum', 1);
INSERT INTO django.aplicatia_mea_parfum (id_parfum, descriere, pret, gen_parfum, volum, imagine, nume_parfum, nume_categorie_id) VALUES (11, 'Dezvaluie forta seducatoare a aromelor Orientului.', 100.00, 'Dame', 20, 'parfumuri/yara_candy_rcehufB.webp', 'Yara Candy', 3);
INSERT INTO django.aplicatia_mea_parfum (id_parfum, descriere, pret, gen_parfum, volum, imagine, nume_parfum, nume_categorie_id) VALUES (12, 'Lattafa Yara este o compozitie orientala cu vanilie.', 100.00, 'Dame', 20, 'parfumuri/yara_GySMrNX.webp', 'Yara', 3);


--
-- Name: aplicatia_mea_parfum_id_parfum_seq; Type: SEQUENCE SET; Schema: django; Owner: maria
--

SELECT pg_catalog.setval('django.aplicatia_mea_parfum_id_parfum_seq', 21, true);


--
-- PostgreSQL database dump complete
--

\unrestrict cdKGwvF2MZA4rKvkjVoaq6GjXqEbO7gXdAsKE0HRZlkAjJkh1haDxYrkqEzGqb3

--
-- PostgreSQL database dump
--

\restrict 5xRPkyXb6Obnn2Out5fDri5l5E6LxOmYt2o6OeLqZsCMsa8l4zdFukXKbYsFnkV

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatia_mea_parfum_furnizori; Type: TABLE DATA; Schema: django; Owner: maria
--

INSERT INTO django.aplicatia_mea_parfum_furnizori (id, parfum_id, furnizor_id) VALUES (1, 1, 1);
INSERT INTO django.aplicatia_mea_parfum_furnizori (id, parfum_id, furnizor_id) VALUES (2, 2, 2);
INSERT INTO django.aplicatia_mea_parfum_furnizori (id, parfum_id, furnizor_id) VALUES (3, 3, 3);
INSERT INTO django.aplicatia_mea_parfum_furnizori (id, parfum_id, furnizor_id) VALUES (4, 4, 2);
INSERT INTO django.aplicatia_mea_parfum_furnizori (id, parfum_id, furnizor_id) VALUES (5, 5, 5);
INSERT INTO django.aplicatia_mea_parfum_furnizori (id, parfum_id, furnizor_id) VALUES (7, 7, 2);
INSERT INTO django.aplicatia_mea_parfum_furnizori (id, parfum_id, furnizor_id) VALUES (8, 8, 6);
INSERT INTO django.aplicatia_mea_parfum_furnizori (id, parfum_id, furnizor_id) VALUES (9, 9, 7);
INSERT INTO django.aplicatia_mea_parfum_furnizori (id, parfum_id, furnizor_id) VALUES (10, 10, 8);
INSERT INTO django.aplicatia_mea_parfum_furnizori (id, parfum_id, furnizor_id) VALUES (11, 11, 9);
INSERT INTO django.aplicatia_mea_parfum_furnizori (id, parfum_id, furnizor_id) VALUES (12, 12, 9);


--
-- Name: aplicatia_mea_parfum_furnizori_id_seq; Type: SEQUENCE SET; Schema: django; Owner: maria
--

SELECT pg_catalog.setval('django.aplicatia_mea_parfum_furnizori_id_seq', 15, true);


--
-- PostgreSQL database dump complete
--

\unrestrict 5xRPkyXb6Obnn2Out5fDri5l5E6LxOmYt2o6OeLqZsCMsa8l4zdFukXKbYsFnkV

--
-- PostgreSQL database dump
--

\restrict vTWf2Qyn4lwm16DLZRBrziDRJeOI9LDXHyUgir2jM222fwrEYK4sSkdJKSguUhT

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatia_mea_compozitiaparfumului; Type: TABLE DATA; Schema: django; Owner: maria
--



--
-- PostgreSQL database dump complete
--

\unrestrict vTWf2Qyn4lwm16DLZRBrziDRJeOI9LDXHyUgir2jM222fwrEYK4sSkdJKSguUhT

--
-- PostgreSQL database dump
--

\restrict nmfrBOpWZurIsijSPNgrfmDfhAsbbk1YDeOFOO23l4fpyHzXiAUQE1lchXnMXZo

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatia_mea_stoc; Type: TABLE DATA; Schema: django; Owner: maria
--

INSERT INTO django.aplicatia_mea_stoc (id_stoc, cantitate, actualizat, parfum_id) VALUES (1, 25, '2026-02-12 20:01:19.865516+02', 1);
INSERT INTO django.aplicatia_mea_stoc (id_stoc, cantitate, actualizat, parfum_id) VALUES (2, 40, '2026-02-12 20:01:19.865516+02', 2);
INSERT INTO django.aplicatia_mea_stoc (id_stoc, cantitate, actualizat, parfum_id) VALUES (3, 10, '2026-02-12 20:01:19.865516+02', 3);
INSERT INTO django.aplicatia_mea_stoc (id_stoc, cantitate, actualizat, parfum_id) VALUES (4, 15, '2026-02-12 20:01:19.865516+02', 4);
INSERT INTO django.aplicatia_mea_stoc (id_stoc, cantitate, actualizat, parfum_id) VALUES (5, 30, '2026-02-12 20:01:19.865516+02', 5);


--
-- Name: aplicatia_mea_stoc_id_stoc_seq; Type: SEQUENCE SET; Schema: django; Owner: maria
--

SELECT pg_catalog.setval('django.aplicatia_mea_stoc_id_stoc_seq', 5, true);


--
-- PostgreSQL database dump complete
--

\unrestrict nmfrBOpWZurIsijSPNgrfmDfhAsbbk1YDeOFOO23l4fpyHzXiAUQE1lchXnMXZo

--
-- PostgreSQL database dump
--

\restrict rS1GqvC5lit3CRjKRaB2xeBbI17zhnVyVT7qcLi7eDOHodkFtqaK0bvPNc1ExqJ

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatia_mea_vanzarizilnice; Type: TABLE DATA; Schema: django; Owner: maria
--

INSERT INTO django.aplicatia_mea_vanzarizilnice (id_vanzare, data, cantitate, venit_total, parfum_id) VALUES (1, '2026-02-10', 2, 1100.00, 1);
INSERT INTO django.aplicatia_mea_vanzarizilnice (id_vanzare, data, cantitate, venit_total, parfum_id) VALUES (2, '2026-02-10', 1, 420.00, 2);
INSERT INTO django.aplicatia_mea_vanzarizilnice (id_vanzare, data, cantitate, venit_total, parfum_id) VALUES (3, '2026-02-11', 1, 890.00, 3);
INSERT INTO django.aplicatia_mea_vanzarizilnice (id_vanzare, data, cantitate, venit_total, parfum_id) VALUES (4, '2026-02-11', 3, 1650.00, 1);
INSERT INTO django.aplicatia_mea_vanzarizilnice (id_vanzare, data, cantitate, venit_total, parfum_id) VALUES (5, '2026-02-11', 2, 960.00, 5);


--
-- Name: aplicatia_mea_vanzarizilnice_id_vanzare_seq; Type: SEQUENCE SET; Schema: django; Owner: maria
--

SELECT pg_catalog.setval('django.aplicatia_mea_vanzarizilnice_id_vanzare_seq', 5, true);


--
-- PostgreSQL database dump complete
--

\unrestrict rS1GqvC5lit3CRjKRaB2xeBbI17zhnVyVT7qcLi7eDOHodkFtqaK0bvPNc1ExqJ

