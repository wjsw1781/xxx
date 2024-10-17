import os
from DrissionPage import ChromiumPage, ChromiumOptions
import DrissionPage
from loguru import logger
import time
import DrissionPage._base
import DrissionPage._base.base 
user_path_work=os.path.abspath('./001')
url='https://creator.douyin.com/creator-micro/content/manage'
os.makedirs(user_path_work, exist_ok=True)
co = ChromiumOptions()
co.set_local_port(9222)
co.set_browser_path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
co.set_user_data_path(user_path_work)
page = ChromiumPage(addr_or_opts=co)
# page.screencast.set_save_path('video')  # 设置视频存放路径
# page.screencast.set_mode.video_mode()  # 设置录制
# page.screencast.start()  # 开始录制

page.get(url)
page.wait(15)

page.scroll.to_see(up_ele)


delete_span=up_ele.ele('xpath://span[contains(text(), "删除作品")]')
import execjs
print(execjs.eval("'red yellow blue'.split(' ')"))
ctx = execjs.compile("""
    function add(x, y) {
        return x + y;
    }
""")
print(ctx.call("add", 1, 2))

npm config set registry https://registry.npmmirror.com	
npm cache clean --force

#文本中包含
delete_span=up_ele.ele('xpath://span[contains(text(), "删除作品")]')

#属性中包含
player_span=up_ele.ele('xpath://span[contains(@class, "info-figure-text")]')
