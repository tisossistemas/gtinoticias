import requests, re, bs4, urllib, doctest
def pesquisaGoogleNews():
    sopa = bs4.BeautifulSoup(requests.get('https://news.google.com.br/', headers=headersRequests()).text, 'html.parser')
    for x in sopa.find_all('td', class_="esc-layout-article-cell" ):
        linkCurto = encurtaURL(x.h2.a.get('href'))
        texto = '' + x.a.text + ' '
        fonte = 'Fonte: ' + x.find('tr').span.text + ' - ' + x.find('tr').find('span', class_='al-attribution-timestamp').text + ' :'
        imprimir = fonte +'\n' + texto + '\n' + linkCurto + '\n' + '*' * 20
        print(imprimir)
def pesquisaTwiter():
    sopa = bs4.BeautifulSoup(requests.get('https://twitter.com/i/streams/category/687094900836274199?lang=pt-br',headers=headersRequests()).text, 'html.parser')
    for x in sopa.find_all('div', class_='TweetWithPivotModule'):
        texto = 'Twitter: '+x.p.text+'\n'+'*'*20
        print(texto)
def pesquisaG1():
    sopa = bs4.BeautifulSoup(requests.get('http://g1.globo.com/',headers=headersRequests()).text, 'html.parser')
    def cabeca():
        for x in sopa.find_all('div', class_='feed-post type-basico'):
            textoLink = x.p.text
            linkCurto = encurtaURL(x.a.get('href'))
            fonte = 'Fonte: G1'+x.find('span', class_='feed-post-time-label').text
            imprimir = fonte+' '+'\n'+textoLink+'\n'+linkCurto+'\n'+'*'*20
            print(imprimir )
    def destaqueLateral():
        for y in sopa.find_all('div', class_='content nano-content'):
            textoLink = y.a.text.strip()+' '
            linkCurto = encurtaURL(y.a.get('href'))
            fonte = 'Fonte: G1 Destaque barra lateral'
            imprimir = fonte+' \n'+textoLink+'\n'+linkCurto+'\n'+'*'*20
            print(imprimir)
    def planetaBizarro():
        sopa = bs4.BeautifulSoup(requests.get('http://g1.globo.com/planeta-bizarro/').text, 'html.parser')
        for x in sopa.find_all('div', class_='feed-text-wrapper'):
            fonte = 'Fonte: ' + x.span.text + ' - ' + x.find('span', class_='feed-post-time-label').text + ' :\n'
            texto = x.p.text + ' \n'
            linkCurto = encurtaURL(x.a.get('href'))
            imprimir = fonte + texto + linkCurto+'\n'+'*'*20
            print(imprimir)
    cabeca()
    planetaBizarro()
    destaqueLateral()
def pesquisaIg():
    sopa = bs4.BeautifulSoup(requests.get('https://www.ig.com.br',headers=headersRequests()).text, 'html.parser')
    for x in sopa.find_all('li', class_='item'):
        fonte = 'Fonte: IG \n'
        texto = x.find('span').text+'\n'
        texto1 = x.h3.text+' \n'
        linkCurto = encurtaURL(x.find('a').get('href'))
        imprimir = fonte+texto+texto1.strip()+'\n'+linkCurto
        print(imprimir         ,'\n','*'*8)
    for y in sopa.find_all('a', class_='titulo'):
        texto = y.get('title')+'\n'
        linkCurto = encurtaURL(y.get('href'))
        fonte = 'Fonte: IG \n'
        imprimiry = fonte+texto+linkCurto
        print(imprimiry,'\n','*'*8)
def pesquisaUol():
    sopa = bs4.BeautifulSoup(requests.get('https://www.uol.com.br/',headers=headersRequests()).text, 'html.parser')
    for x in sopa.find_all('a', class_='opacity-group'):
        fonte = 'Fonte: UOL Origem Interna ->'+x.get('data-metrics').split(';')[1] + '\n'
        texto = x.text.strip()
        linkCurto = encurtaURL(x.get('href'))
        print(fonte + texto+'\n' + linkCurto+'\n','*'*8)
def principalNoticiaBizarras():
    sopa = bs4.BeautifulSoup(requests.request('get', 'https://www.noticiasbizarras.com.br',headers=headersRequests()).text, 'html.parser')
    for x in sopa.find_all('h2'):
        titulo = x.a.get('title')
        link = x.a.get('href')
        print('Titulo: ', titulo, '\nLink: ', link, '\n', '*' * 8)
def lateralNoticiasBizarras():
    sopa = bs4.BeautifulSoup(requests.request('get', 'https://www.noticiasbizarras.com.br',headers=headersRequests()).text, 'html.parser')
    for x in sopa.find_all('div', class_="sidebar1"):
        for y in x.ul:
            titulo = y.a.get('title')
            link = y.a.get('href')
            print('Titulo: '+titulo + '\nLink: ' + link, '\n', '*' * 8)
def ultimasMeioNorte():
    sopa = bs4.BeautifulSoup(requests.request('get', 'http://www.meionorte.com/ultimas-noticias',headers=headersRequests()).text, 'html.parser')
    for x in sopa.find_all('h4'):
        titulo = x.a.get('title')
        link = 'http://www.meionorte.com' + x.a.get('href')
        print('Titulo: ', titulo, '\nLink: ', link, '\n', '*' * 8)
def JogoSerioDestaque():
    sopa = bs4.BeautifulSoup(requests.request('get', 'https://www.jornaljogoserio.com.br/', headers=headersRequests()).text, 'html.parser')
    try:
        for x in sopa.find_all('div', class_='box-destaques'):
            for y in x.find_all('li'):
                titulo = y.span.text
                texto = y.p.text
                Fonte = 'http://www.jornaljogoserio.com.br/'
                link = encurtaURL(Fonte + y.a.get('href'))
                print('Titulo: ', titulo,'Fonte: ',Fonte ,'\nTexto: ', texto, '\nLink: ', link, '\n', '*' * 8)
    except:
        print('Falha no site'+Fonte)
def JogoSerioAgronegocio():
    sopa = bs4.BeautifulSoup(requests.request('get', 'https://www.jornaljogoserio.com.br/', headers=headersRequests()).text, 'html.parser')
    try:
        for x in sopa.find_all('div', class_='coluna-noticia verde'):
            for y in x.find_all('li'):
                titulo = y.span.text
                texto = y.p.text
                Fonte = 'http://www.jornaljogoserio.com.br/'
                link = encurtaURL(Fonte + y.a.get('href'))
                print('Titulo: ', titulo, 'Fonte: ', Fonte, '\nTexto: ', texto, '\nLink: ', link, '\n', '*' * 8)
    except:
        print('Falha no site ' + Fonte)
def JogoSerioAlgazarra():
    sopa = bs4.BeautifulSoup(requests.request('get', 'https://www.jornaljogoserio.com.br/', headers=headersRequests()).text, 'html.parser')
    try:
        for x in sopa.find_all('div', class_='coluna-noticia laranja'):
            for y in x.find_all('li'):
                titulo = y.span.text
                texto = y.p.text
                Fonte = 'http://www.jornaljogoserio.com.br/'
                link = encurtaURL(Fonte + y.a.get('href'))
                print('Titulo: ', titulo, 'Fonte: ', Fonte, '\nTexto: ', texto, '\nLink: ', link, '\n', '*' * 8)
    except:
        print('Falha no site ' + Fonte)


def testandoHeaders():
    re = requests.get('http://www.andradas.mg.gov.br/', headers=headersRequests())
    #sopa = bs4.BeautifulSoup(re.headers, 'html.parser')
    print(re.headers)

#================Usando termo de pesquisa=========================
def pesquisaGoogleNewsP(pesquisar):
    sopa = bs4.BeautifulSoup(requests.get('https://www.google.com.br/search?num=200&source=lnms&tbm=nws&sa=X&ved=0ahUKEwiGnoXC9sPRAhWDHZAKHX01A_wQ_AUICSgC&biw=832&bih=638&q='+urllib.parse.quote(pesquisar, safe='')).text, 'html.parser')
    for x in sopa.find_all('div', class_='g'):
        linkCurto = encurtaURL(''+x.td.a.get('href').split('&')[0].split('=')[1]+'')
        descricao = ''+x.find('div', class_='st').text+' '
        texto = ''+x.td.a.text+' '
        fonteTempo = 'Fonte: '+x.td.span.text+': '
        imprimir = fonteTempo+'\n'+texto+'\n'+descricao+'\n'+linkCurto+'\n'+'*'*20
        print(imprimir)
def pesquisaG1P(pesquisar):
    sopa = bs4.BeautifulSoup(requests.get('http://g1.globo.com/busca/?q='+urllib.parse.quote(pesquisar, safe='')).text, 'html.parser')
    for x in sopa.find_all('div', class_='busca-materia-padrao'):
        texto = x.a.text+'\n'
        fonte = 'Fonte: '+x.find('span', class_='busca-portal').text+' - '
        data =  x.find('span', class_='busca-tempo-decorrido').text.strip()+' \n'
        link = 'http:'+x.a.get('href')
        linkCurto = encurtaURL(link)
        imprimir = fonte+data+texto+linkCurto
        print(imprimir      , '\n','*'*8)
def headersRequests():
    headers = {"Accept-Language": "en-US", "Accept-Encoding": "gzip, defate, sdch",
               "Referrer": "https://www.google.com.br",
               "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
    return headers


    return headers
#=================================================================

def encurtaURL(url):
    linkCurto = requests.get('http://migre.me/api.txt?url=' + url)
    if 'API' in linkCurto.text:
        retorno = 'Link: ' + url
        return retorno
    else:
        retorno = 'Link: ' + linkCurto.text
        return retorno
def pesquisaTudo(pesquisa=''):
    if pesquisa == '':
        pesquisaTwiter()
        pesquisaGoogleNews()
        pesquisaG1()
        pesquisaIg()
        pesquisaUol()
    else:
        pesquisaGoogleNewsP(pesquisa)
        pesquisaG1P(pesquisa)
#pesquisaGoogleNews()
#pesquisaG1()
#pesquisaIg()
#pesquisaTwiter()
#pesquisaUol()
#principalNoticiaBizarras()
#lateralNoticiasBizarras()
#ultimasMeioNorte()
#JogoSerioAgronegocio()
#JogoSerioDestaque()
#JogoSerioAlgazarra()
#JogoSerioPolicial()
#testandoHeaders()
pesquisaTudo()

