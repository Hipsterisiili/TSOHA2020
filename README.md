# TSOHA2020
Musiikkitietokantasovellus, josta käyttäjä voi tarkastella musiikkitietokannasta löytyviä tietoja sekä luoda ohjelman avustamana soittolistoja tietokannasta löytyvistä kappaleista.

Sovellus tulee sisältämään kaksi käyttäjäroolia: "admin" ja "user". User voi tarkastella tietokantaa ja tehdä sieltä hakuja kun taas admin voi sen lisäksi tehdä muutoksia tietokantaan.

Käyttäjä voi hakea tietokannasta musiikkia hakien esimerkiksi kappeleiden esittäjien, albumien, julkaisuvuosien ja genrejen avulla. Lisäksi käyttäjä voi pyytää sovellusta palauttamaan soittolistan kappaleista, jotka sopivat käyttäjän nimeämiin hakuehtoihin. Sovellus sekoittaa soittolistan jollakin yksinkertaisella "sattumanvaraisella" menetelmällä.

Tietokannan tulee sisältää ainakin seuraavat tietokantataulut:

ARTISTI
(id INTEGER PRIMARY KEY, nimi TEXT, ensisijainenGenre INTEGER (references GENRE)

ALBUMI  
(id INTEGER PRIMARY KEY, nimi TEXT, artistiId INTEGER (references ARTISTI), julkaisuVuosi INTEGER)

KAPPALE 
(id INTEGER PRIMARY KEY, nimi TEXT, albumiId INTEGER (references ALBUMI), kesto INTEGER)

GENRE   
(id INTEGER PRIMARY KEY, nimi TEXT)

KAPPALEGENRE 
(id INTEGER PRIMAR KEY, kappaleId INTEGER (references KAPPALE), genreId INTEGER (references GENRE))


Esimerkkejä user storysta:

Käyttäjä tahtoo löytää lapsuusajan rock-hittejä ja valitsee hakuunsa siis attribuuteiksi genren "rock" ja julkaisuvuodet 1995-2005. 

--> Ohjelma palauttaa listan kaikista kappaleista, jotka sopivat haluttuun hakuun

Käyttäjä tahtoo tehdä puolen tunnin mittaiden samasta musiikista, jota haettiin edellisessä esimerkissä.

--> Ohjelma palauttaa sekoitetun listan halutun kaltaisista kappaleista siten että kaikkien kappaleiden kuuntelemiseen menee puoli tuntia. HUOM. Viimeinen kappale todennäköisesti ylittää aikarajan.

Järjestelmänvalvoja tahtoo lisätä uuden kappaleen tietokantaan, joten hän kirjautuu sisään etuoikeutettuun tilaan ja lisää kappaleen mainiten samalla kappaleeseen liittyvät olennaiset tiedot: kappaleen nimen, keston, albumin, artistin, genren ja julkaisuvuoden. 

--> Mikäli tällaista genreä, albumia ja/tai artistia ei ole vielä tietokannassa, ohjelma huomauttaa tästä järjestelmänvalvojalle, joka voi vielä harkita lisätäänkö uusia albumeita/artisteja/genrejä tietokantaan yksinkertaisessa "kyllä/ei"-valintaruudussa.

--> Halutut tiedot lisätään tietokantaan.
