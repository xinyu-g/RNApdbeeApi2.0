# API dla narzędzia RNApdbee

Celem projektu jest implementacja API umożliwiającego korzystanie z narzędzia RNApdbee
(http://rnapdbee.cs.put.poznan.pl/) z poziomu pythona. Ponieważ autorzy narzędzia nie udostępniają
odpowiednich metod, implementację należy zrealizować metodą web-scraping.
Zaimplementowane funkcje powinny pokrywać pełną funkcjonalność narzędzia, tj generację
struktury drugorzędowej zarówno na podstawie struktury podanej w formacie PDB (w postaci
lokalnego pliku lub identyfikatora PBD), jak i na podstawie listy par (z lokalnego pliku w formacie
BPSEQ lub CT) z uwzględnieniem wszystkich dostępnych w RNApdbee opcji.