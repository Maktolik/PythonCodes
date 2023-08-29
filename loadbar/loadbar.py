import requests
import tqdm


def download_files(url: str, filename: str):
    with open(filename, 'wb') as f:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            size = int(r.headers.get('content-lenghts', 0))

            tqdm_param = {
                'desc': url,
                'total': size,
                'miniters': 1,
                'unit': 'it',
                'unit_scale': True,
                'unit_divisor': 1024,
            }
            with tqdm.tqdm(**tqdm_param) as pb:
                for chunk in r.iter_content(chunk_size=8192):
                    pb.update(len(chunk))
                    f.write(chunk)


def main():
    download_files('https://drive.usercontent.google.com/download?id=194h3iW8zqKcCK1cW-fyLNaxkXkQp8V7r&export=download&authuser=0&confirm=t&uuid=ecf0aa6e-9d25-4718-b5f9-58859374e666&at=APZUnTUNDQrAzevZqNaWqrZyr9VA:1693101269334','prog.rar')

if __name__ == '__main__':
    main()