import asyncio
import httpx
import tqdm


async def download_files(url: str, filename: str):
    with open(filename, 'wb') as f:
        async with httpx.AsyncClient() as client:
            async with client.stream('GET', url) as r:
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
                    for chunk in r.aiter_bytes():
                        pb.update(len(chunk))
                        f.write(chunk)


async def main():

    loop = asyncio.get_running_loop()

    urls = [
        # ('https://fs133.tbx.su/files10/1850377_016ac1/com.nianticlabs.pokemongo_0.279.3_2023081400.apk', '50.apk'),
        # ('https://fs126.tbx.su/files10/1851747_55f857/com.miniclip.plagueinc_1.19.13_1527.apk', '100.apk'),
        # ('https://fs109.tbx.su/files10/1853045_d9df8c/com.soulcastry.virtualdroid2_33.5_100335.apk', '200.apk'),
    ]
    tasks = [loop.create_task(download_files(url, filename)) for url, filename in urls]
    await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == '__main__':
    asyncio.run(main())