from Szek import Szek
import szekProgramMetodusok


szekekLista = szekProgramMetodusok.peldanyokLista()
szekProgramMetodusok.peldanyok_kiirasa(szekekLista)
szekProgramMetodusok.labak_szama(szekekLista)
print(szekProgramMetodusok.maxLabSzin(szekekLista))
print(f"{szekProgramMetodusok.labakszama(szekekLista)}db")
print(f"{szekProgramMetodusok.vanpiros4labu_2(szekekLista)}")
