import pandas as pd
import datetime

termau = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRyXAEy1FiyDdPVe7Q-pAzLHCeeNKWpflstl12091hxlEiACyCCXNqPKoV8B2pV6QzDUTWaOnZAf181/pub?gid=0&single=true&output=csv')

termau['English'] = termau['English'].apply(lambda x: x.lower())
termau['Cymraeg'] = termau['Cymraeg'].apply(lambda x: x.lower())
termau_ec = termau[['English', 'Cymraeg']].sort_values('English')
termau_ce = termau[['Cymraeg', 'English']].sort_values('Cymraeg')


head_old = """\\begin{tabular}{ll}
\\toprule
"""
foot_old = """\\bottomrule
\\end{tabular}
"""

head_new = """\\begin{supertabular}{p{0.22\\textwidth}p{0.22\\textwidth}}
"""

foot_new = """\\end{supertabular}
"""

with open('assets/tex/termau_ec.tex', 'w') as f:
	termau_ec_tex = termau_ec.to_latex(index=False, header=False).replace(head_old, head_new).replace(foot_old, foot_new)
	f.write(termau_ec_tex)

with open('assets/tex/termau_ce.tex', 'w') as f:
	termau_ce_tex = termau_ce.to_latex(index=False, header=False).replace(head_old, head_new).replace(foot_old, foot_new)
	f.write(termau_ce_tex)

misoedd={
    1:'Ionawr',
    2:'Chwefror',
    3:'Mawrth',
    4:'Ebrill',
    5:'Mai',
    6:'Mehefin',
    7:'Gorffenaf',
    8:'Awst',
    9:'Medi',
    10:'Hydref',
    11:'Tachwedd',
    12:'Rhagfyr'
}

with open('assets/head.html', 'r') as f:
    head = f.read()

tabl = ''
for row in termau.iterrows():
    tabl += '<tr>\n  <td>'
    tabl += row[1]['Cymraeg']
    tabl += '</td>\n  <td>'
    tabl += row[1]['English']
    tabl += '</td>\n</tr>\n'

dyddiad = datetime.datetime.now()

foot = f"</table>\n\n<p id='foot'>(<a href='assets/tex/termiadur.pdf'>Lawrlwytho'r pdf</a>) Diweddariad diwethaf ar {dyddiad.day} {misoedd[dyddiad.month]} {dyddiad.year}.</p>\n\n</body>\n</html>"

html = head + tabl + foot

with open('index.html', 'w') as f:
    f.write(html)

