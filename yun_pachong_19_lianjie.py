#与课程所讲不一致。新浪新闻改版后，新闻不再分页（课程是分页的），而是鼠标翻动后更新的

import requests
import json
res = requests.get("http://cre.mix.sina.com.cn/api/v3/get?callback=jQuery11110020958177349853502_1519289022374&cateid=sina_all&cre=tianyi&mod=pcpager_china&merge=3&statics=1&this_page=1&length=40&up=0&down=0&pageurl=http%3A%2F%2Fnews.sina.com.cn%2Fc%2Fnd%2F2018-01-30%2Fdoc-ifyremfz2269397.shtml&imp_type=2&action=0&fields=media%2Cauthor%2Clabels_show%2Ccommentid%2Ccomment_count%2Ctitle%2Cltitle%2Curl%2Cinfo%2Cthumbs%2Cthumb%2Cctime%2Creason%2Ccategory%2Cvideo_id%2ChotTag%2Cimg_count%2Cgif%2Clive_stime%2Clive_etime%2Cmedia_id%2Csummary%2CorgUrl%2Cshow%2Cintro%2Cdocid%2Cplaytimes%2Cvideo_height%2Cvideo_width%2Ctime_length%2Cuser_icon%2Cuid&tm=1519289025&offset=0&ad=%7B%22rotate_count%22%3A100%2C%22platform%22%3A%22pc%22%2C%22channel%22%3A%22tianyi_pcpager_china%22%2C%22page_url%22%3A%22http%3A%2F%2Fnews.sina.com.cn%2Fc%2Fnd%2F2018-01-30%2Fdoc-ifyremfz2269397.shtml%22%2C%22timestamp%22%3A1519289025303%7D&_=1519289022380")
jd = json.loads(res.text.lstrip('jQuery11110020958177349853502_1519289022374(')).rstrip(');')
jd



import requests
from bs4 import BeautifulSoup

res = requests.get("http://cre.mix.sina.com.cn/api/v3/get?callback=jQuery11110020958177349853502_1519289022374&cateid=sina_all&cre=tianyi&mod=pcpager_china&merge=3&statics=1&this_page=1&length=40&up=0&down=0&pageurl=http%3A%2F%2Fnews.sina.com.cn%2Fc%2Fnd%2F2018-01-30%2Fdoc-ifyremfz2269397.shtml&imp_type=2&action=0&fields=media%2Cauthor%2Clabels_show%2Ccommentid%2Ccomment_count%2Ctitle%2Cltitle%2Curl%2Cinfo%2Cthumbs%2Cthumb%2Cctime%2Creason%2Ccategory%2Cvideo_id%2ChotTag%2Cimg_count%2Cgif%2Clive_stime%2Clive_etime%2Cmedia_id%2Csummary%2CorgUrl%2Cshow%2Cintro%2Cdocid%2Cplaytimes%2Cvideo_height%2Cvideo_width%2Ctime_length%2Cuser_icon%2Cuid&tm=1519289025&offset=0&ad=%7B%22rotate_count%22%3A100%2C%22platform%22%3A%22pc%22%2C%22channel%22%3A%22tianyi_pcpager_china%22%2C%22page_url%22%3A%22http%3A%2F%2Fnews.sina.com.cn%2Fc%2Fnd%2F2018-01-30%2Fdoc-ifyremfz2269397.shtml%22%2C%22timestamp%22%3A1519289025303%7D&_=1519289022380")
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')
soup



