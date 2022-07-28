# -*- coding: utf-8 -*-
# @Author  : 夏洛
# @File    : xl.py
# @VX : tl210329
import hashlib

params_api = 'https://www.mafengwo.cn/hotel/ajax.php?'
time_samp = '1646115258591' #str(int(time.time()*1000))
area_code = str(iarea.get("code"))
params = {"_ts":time_samp,"has_booking_rooms":"0","has_faved":"0","iAdultsNum":"2","iAreaId":area_code,"iChildrenNum":"0","iDistance":"10000","iMddId":"10208","iPage":str(page),"iPoiId":"","iPriceMax":"","iPriceMin":"","iRegionId":"-1","nLat":"0","nLng":"0","position_name":"","sAction":"getPoiList5","sCheckIn":"2022-04-09","sCheckOut":"2022-04-10","sChildrenAge":"","sKeyWord":"","sSortFlag":"DESC","sSortType":"comment","sTags":""}
data_params = '{"_ts":"'+time_samp+'","has_booking_rooms":"0","has_faved":"0","iAdultsNum":"2","iAreaId":"'+area_code+'","iChildrenNum":"0","iDistance":"10000","iMddId":"10208","iPage":"'+str(page)+'","iPoiId":"","iPriceMax":"","iPriceMin":"","iRegionId":"-1","nLat":"0","nLng":"0","position_name":"","sAction":"getPoiList5","sCheckIn":"2022-04-09","sCheckOut":"2022-04-10","sChildrenAge":"","sKeyWord":"","sSortFlag":"DESC","sSortType":"comment","sTags":""}c9d6618dbc657b41a66eb0af952906f1'
hashbo = hashlib.md5()
hashbo.update(data_params.encode())
params["_sn"] = hashbo.hexdigest()[2:12]



