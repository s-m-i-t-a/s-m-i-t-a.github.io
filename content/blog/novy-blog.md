title: Blog za pomoci Pelicanu
tags: blog, python, pelican
date: 2012-09-26


Dlouho zela moje doména prázdnotou a já psal poznámky různě po papírech, což stačilo do doby, než jsem zapomněl, kde vlastně ty potřebné papíry mám. Proto padlo rozhodnutí, vytvářet poznámky na počítači.

Rozhodnutí v čem a jak psát bylo těžké, ať už řešení, která dnešní web nabízí nebo vlastní výroba blogu, ale spíše to bylo nalézání slepých uliček.

Tyto uličky mě dovedly k tomu, co pro tvorbu poznámek požaduji:

* musí běžet na [Google App Engine,](https://developers.google.com/appengine/)
* musí být nejlépe napsané v [Pythonu](http://www.python.org) s podporou pluginů,
* psát na svém notebooku,
* psát ve [Vimu,](http://www.vim.org/)
* psát [Markdown,](http://daringfireball.net/projects/markdown/)
* mít blog verzovaný [Gitem.](http://git-scm.com/)

Po chvilce hledání na netu jsem narazil na generátor [Pelican](http://docs.getpelican.com "Pelican is a static site generator, written in Python."), který splnil mé požadavky.

Uvádím zde jen nastavení pro Google App Engine, [instalaci Pelicanu](http://docs.getpelican.com/en/3.0/getting_started.html#installing-pelican) najdete v jeho dokumentaci.

### Pelican a Google App Engine

*Pelican* mám nastavený tak, aby výstup uložil do adresáře `output` v kořenu repozitáře. GAE potřebuje vědět, kde má vzít patřičné stránky, proto přidáme pár řádek do `app.yaml` do sekce `handlers.`

    :::yaml

    application: test
    version: 1
    runtime: python27
    api_version: 1
    threadsafe: true


    handlers:

    # Toto mapuje ikonku /favicon.ico do adresare s tematem, kde ji mam umistenou.
    - url: /favicon\.ico
      static_files: output/theme/images/favicon.ico
      upload: output/theme/images/favicon\.ico

    # Toto je namapování kořene na index.html
    - url: /
      static_files: output/index.html
      upload: output/index.html

    # Toto mapuje url do adresare output.
    # Pr. URL http://www.smita.info/bagr.html namapuje na output/bagr.html
    - url: /
      static_dir: output

Parametr `upload` říká, že se při nasazení na servery Googlu má tento soubor též přenést.
