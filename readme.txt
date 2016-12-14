
#執行方式
#建立資料檔欄位名稱,寫入Data.csv檔(以;分隔)
$ python3 ./crawl_title.py

#抓取資料,給予參數(使用者性別F/M)
$ python3 ./crawl.py F


######執行檔########
#crawl_title.py 為抓取資料欄位

#crawl_user.py 為抓取會員個人資料與照片(圖片檔名為使用者編號,存與photo資料夾下)

#crawl.py 為抓取目前線上會員資料(預設為前10頁)
#crawl.py 會呼叫crawl_user.py 並給參數url(會員個人資料網址)

