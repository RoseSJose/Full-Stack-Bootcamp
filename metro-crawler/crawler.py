import requests
import bs4

def get_all_song_links(url):
    ret = []
    resp = requests.get(url)
    soup = bs4.BeautifulSoup(resp.content, features="html.parser")
    links = soup.find_all("a", attrs={"class":"title hasvidtable"})
    for i in links:
        ret.append(i['href'])
    return ret
        
def get_file_name(url):
    fname = url.split("/")[-1].replace(".html",".txt")
    return fname
    
    
def get_song_lyrics(url):
    lyrics = []
    resp = requests.get(url)
    soup = bs4.BeautifulSoup(resp.content, features="html.parser")
    verse = soup.find_all("p", attrs={"class":"verse"})
    for i in verse:
        lyrics.append(i.get_text())
    return "\n".join(lyrics)
            
def main():
    links = get_all_song_links("https://www.metrolyrics.com/alan-walker-lyrics.html")
    for i in links:
        fname = get_file_name(i)
        f = open(fname, 'w')
        lyrics = get_song_lyrics(i)
        f.write(lyrics)
        print(i)
        #print(get_song_lyrics(i))
        break
    
    
if __name__ == "__main__":
    main()
