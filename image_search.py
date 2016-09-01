from googleapiclient.discovery import build
from urllib.request import urlretrieve

def cats_image_search(breed_name, file_name):
    service = build("customsearch",  "v1",
                     developerKey="AIzaSyDu96t81G86A7hW36-2I-1BnYgDPp0J8Ek")

    results = service.cse().list(
        q=breed_name,
        cx='017847062227810365920:whopzxvqb6i',
        searchType='image',
        num=1,
        imgType='clipart',
        fileType='png',
        safe='off'
    ).execute()
    if not 'items' in results:
        print
        'No result !!\nres is: {}'.format(results)
    else:
        for item in results['items']:
            urlretrieve(item['link'], file_name)

def main():
    cats_image_search('british blue cat', 'images/british_blue_cat.png')

if __name__ == '__main__':
    main()