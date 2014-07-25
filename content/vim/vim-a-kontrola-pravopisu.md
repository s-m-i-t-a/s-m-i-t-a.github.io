title: Kontrola pravopisu ve Vimu
tags: vim
status: draft


Když jsem se rozhodl psát na web, tak by to též chtělo něco, co zkontroluje mé chyby, protože jsem člověk, tedy tvor chybující.

!!! Popsat vytvoreni jednoduche fce ve vimu, ktera bude prepinat mezi zapnutou a vypnutou kontrolou pravopisu !!!

    :::vim

    " Vypnuti/zapnuti kontroly pravopisu
    nmap <silent> <leader>s :set spell!<CR>
    set spelllang=cs,en

!!! PŘEPRACOVAT !!!

Z ftp://ftp.vim.org/pub/vim/runtime/spell/ si stáhneme spell soubory, o které máme zájem (cs.iso-8859-2.spl, cs.utf-8.spl, cs.cp1250.spl). A uložíme si je do ~/.vim/spell/ nebo {runtimepath}/spell/. Soubor se hledá dle vzoru {runtimepath}/spell/{spelllang}.{encoding}.spl.
:set spell spelllang=cs -> zapnutí kontroly českého pravopisu
:set nospell -> vypnutí kontroly pravopisu
]s -> následující chyba
[s -> předchozí chyba
zg -> slovo pod kurzorem je správně (ukládá do ~/.vim/spell/{spelllang}.{encoding}.add*)
zG -> jako předchozí, ale po ukončení Vimu je vše zapomenuto (ukládá do /tmp/v*/*)
zw -> slovo pod kurzorem je špatně
zW -> jako předchozí, ale po ukončení Vimu je vše zapomenuto
z= -> vypíše možnosti opravy chybného slova

Zdroj: http://www.abclinuxu.cz/clanky/tipy/vim-7.0#spell


