# -*- coding: utf-8 -*-
# @Author  : 夏洛
# @File    : xialuo.py
# @VX : tl210329

import pprint
import time
import copyheaders
import execjs
import requests


headers = copyheaders.headers_raw_to_dict(b"""
accept: */*
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
cache-control: no-cache
cookie: __mgjuuid=c010e862-b7a4-4bb1-a0db-2cbf74fbe2aa; _mwp_h5_token=a59a5de69535dc6c6ce9998c1f8d49ea_1643693248578; _mwp_h5_token_enc=ec94b44d21ec4c3519bf2d0c95c294a6
pragma: no-cache
referer: https://pc.mogu.com/content/live-slice/index.html?itemId=1n1syye&actorId=19pb9ua&acm=3.mce.1_4_1n1syye.153585.108975-108368-110740.u7v17sWawEphv.gi_u7v16sWawEqr2p-sv_14gh00dniph4m-pt_153585-src_1-pri_9_19pb9ua-dm1_1000-mid_153585-sd_116_115-xid_2102-t_u7v16sWawEphV-xm_1eloda-lc_201-x_19pb9ua-pit_80-sn_12jxce-pm_355&ptp=31.v5mL0b.0.0.Q0IzCwe1
sec-ch-ua: " Not;A Brand";v="99", "Microsoft Edge";v="97", "Chromium";v="97"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
sec-fetch-dest: script
sec-fetch-mode: no-cors
sec-fetch-site: same-site
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76
""")



def dogetparams(params,_mwp_h5_token,apitype):
    data = params["data"]
    ctx = execjs.compile("""
    function V(t, e) {
        return t(e = {
            exports: {}
        }, e.exports),
        e.exports
    }


    // =========================================================

    var U = V(function(t) {
        var i, n;
        i = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",
        n = {
            rotl: function(t, e) {
                return t << e | t >>> 32 - e
            },
            rotr: function(t, e) {
                return t << 32 - e | t >>> e
            },
            endian: function(t) {
                if (t.constructor == Number)
                    return 16711935 & n.rotl(t, 8) | 4278255360 & n.rotl(t, 24);
                for (var e = 0; e < t.length; e++)
                    t[e] = n.endian(t[e]);
                return t
            },
            randomBytes: function(t) {
                for (var e = []; 0 < t; t--)
                    e.push(Math.floor(256 * Math.random()));
                return e
            },
            bytesToWords: function(t) {
                for (var e = [], n = 0, o = 0; n < t.length; n++,
                o += 8)
                    e[o >>> 5] |= t[n] << 24 - o % 32;
                return e
            },
            wordsToBytes: function(t) {
                for (var e = [], n = 0; n < 32 * t.length; n += 8)
                    e.push(t[n >>> 5] >>> 24 - n % 32 & 255);
                return e
            },
            bytesToHex: function(t) {
                for (var e = [], n = 0; n < t.length; n++)
                    e.push((t[n] >>> 4).toString(16)),
                    e.push((15 & t[n]).toString(16));
                return e.join("")
            },
            hexToBytes: function(t) {
                for (var e = [], n = 0; n < t.length; n += 2)
                    e.push(parseInt(t.substr(n, 2), 16));
                return e
            },
            bytesToBase64: function(t) {
                for (var e = [], n = 0; n < t.length; n += 3)
                    for (var o = t[n] << 16 | t[n + 1] << 8 | t[n + 2], r = 0; r < 4; r++)
                        8 * n + 6 * r <= 8 * t.length ? e.push(i.charAt(o >>> 6 * (3 - r) & 63)) : e.push("=");
                return e.join("")
            },
            base64ToBytes: function(t) {
                t = t.replace(/[^A-Z0-9+\/]/gi, "");
                for (var e = [], n = 0, o = 0; n < t.length; o = ++n % 4)
                    0 != o && e.push((i.indexOf(t.charAt(n - 1)) & Math.pow(2, -2 * o + 8) - 1) << 2 * o | i.indexOf(t.charAt(n)) >>> 6 - 2 * o);
                return e
            }
        },
        t.exports = n
    })
      , q = {
        utf8: {
            stringToBytes: function(t) {
                return q.bin.stringToBytes(unescape(encodeURIComponent(t)))
            },
            bytesToString: function(t) {
                return decodeURIComponent(escape(q.bin.bytesToString(t)))
            }
        },
        bin: {
            stringToBytes: function(t) {
                for (var e = [], n = 0; n < t.length; n++)
                    e.push(255 & t.charCodeAt(n));
                return e
            },
            bytesToString: function(t) {
                for (var e = [], n = 0; n < t.length; n++)
                    e.push(String.fromCharCode(t[n]));
                return e.join("")
            }
        }
    }
      , J = q
      , F = function(t) {
        return null != t && (W(t) || "function" == typeof (e = t).readFloatLE && "function" == typeof e.slice && W(e.slice(0, 0)) || !!t._isBuffer);
        var e
    };


    // ============================================================================

    var z = V(function(t) {
        var v, g, _, w, b;
        v = U,
        g = J.utf8,
        _ = F,
        w = J.bin,
        (b = function(t, e) {
            t.constructor == String ? t = e && "binary" === e.encoding ? w.stringToBytes(t) : g.stringToBytes(t) : _(t) ? t = Array.prototype.slice.call(t, 0) : Array.isArray(t) || (t = t.toString());
            for (var n = v.bytesToWords(t), o = 8 * t.length, r = 1732584193, i = -271733879, s = -1732584194, a = 271733878, u = 0; u < n.length; u++)
                n[u] = 16711935 & (n[u] << 8 | n[u] >>> 24) | 4278255360 & (n[u] << 24 | n[u] >>> 8);
            n[o >>> 5] |= 128 << o % 32,
            n[14 + (o + 64 >>> 9 << 4)] = o;
            var c = b._ff
              , p = b._gg
              , l = b._hh
              , h = b._ii;
            for (u = 0; u < n.length; u += 16) {
                var f = r
                  , d = i
                  , y = s
                  , m = a;
                i = h(i = h(i = h(i = h(i = l(i = l(i = l(i = l(i = p(i = p(i = p(i = p(i = c(i = c(i = c(i = c(i, s = c(s, a = c(a, r = c(r, i, s, a, n[u + 0], 7, -680876936), i, s, n[u + 1], 12, -389564586), r, i, n[u + 2], 17, 606105819), a, r, n[u + 3], 22, -1044525330), s = c(s, a = c(a, r = c(r, i, s, a, n[u + 4], 7, -176418897), i, s, n[u + 5], 12, 1200080426), r, i, n[u + 6], 17, -1473231341), a, r, n[u + 7], 22, -45705983), s = c(s, a = c(a, r = c(r, i, s, a, n[u + 8], 7, 1770035416), i, s, n[u + 9], 12, -1958414417), r, i, n[u + 10], 17, -42063), a, r, n[u + 11], 22, -1990404162), s = c(s, a = c(a, r = c(r, i, s, a, n[u + 12], 7, 1804603682), i, s, n[u + 13], 12, -40341101), r, i, n[u + 14], 17, -1502002290), a, r, n[u + 15], 22, 1236535329), s = p(s, a = p(a, r = p(r, i, s, a, n[u + 1], 5, -165796510), i, s, n[u + 6], 9, -1069501632), r, i, n[u + 11], 14, 643717713), a, r, n[u + 0], 20, -373897302), s = p(s, a = p(a, r = p(r, i, s, a, n[u + 5], 5, -701558691), i, s, n[u + 10], 9, 38016083), r, i, n[u + 15], 14, -660478335), a, r, n[u + 4], 20, -405537848), s = p(s, a = p(a, r = p(r, i, s, a, n[u + 9], 5, 568446438), i, s, n[u + 14], 9, -1019803690), r, i, n[u + 3], 14, -187363961), a, r, n[u + 8], 20, 1163531501), s = p(s, a = p(a, r = p(r, i, s, a, n[u + 13], 5, -1444681467), i, s, n[u + 2], 9, -51403784), r, i, n[u + 7], 14, 1735328473), a, r, n[u + 12], 20, -1926607734), s = l(s, a = l(a, r = l(r, i, s, a, n[u + 5], 4, -378558), i, s, n[u + 8], 11, -2022574463), r, i, n[u + 11], 16, 1839030562), a, r, n[u + 14], 23, -35309556), s = l(s, a = l(a, r = l(r, i, s, a, n[u + 1], 4, -1530992060), i, s, n[u + 4], 11, 1272893353), r, i, n[u + 7], 16, -155497632), a, r, n[u + 10], 23, -1094730640), s = l(s, a = l(a, r = l(r, i, s, a, n[u + 13], 4, 681279174), i, s, n[u + 0], 11, -358537222), r, i, n[u + 3], 16, -722521979), a, r, n[u + 6], 23, 76029189), s = l(s, a = l(a, r = l(r, i, s, a, n[u + 9], 4, -640364487), i, s, n[u + 12], 11, -421815835), r, i, n[u + 15], 16, 530742520), a, r, n[u + 2], 23, -995338651), s = h(s, a = h(a, r = h(r, i, s, a, n[u + 0], 6, -198630844), i, s, n[u + 7], 10, 1126891415), r, i, n[u + 14], 15, -1416354905), a, r, n[u + 5], 21, -57434055), s = h(s, a = h(a, r = h(r, i, s, a, n[u + 12], 6, 1700485571), i, s, n[u + 3], 10, -1894986606), r, i, n[u + 10], 15, -1051523), a, r, n[u + 1], 21, -2054922799), s = h(s, a = h(a, r = h(r, i, s, a, n[u + 8], 6, 1873313359), i, s, n[u + 15], 10, -30611744), r, i, n[u + 6], 15, -1560198380), a, r, n[u + 13], 21, 1309151649), s = h(s, a = h(a, r = h(r, i, s, a, n[u + 4], 6, -145523070), i, s, n[u + 11], 10, -1120210379), r, i, n[u + 2], 15, 718787259), a, r, n[u + 9], 21, -343485551),
                r = r + f >>> 0,
                i = i + d >>> 0,
                s = s + y >>> 0,
                a = a + m >>> 0
            }
            return v.endian([r, i, s, a])
        }
        )._ff = function(t, e, n, o, r, i, s) {
            var a = t + (e & n | ~e & o) + (r >>> 0) + s;
            return (a << i | a >>> 32 - i) + e
        }
        ,
        b._gg = function(t, e, n, o, r, i, s) {
            var a = t + (e & o | n & ~o) + (r >>> 0) + s;
            return (a << i | a >>> 32 - i) + e
        }
        ,
        b._hh = function(t, e, n, o, r, i, s) {
            var a = t + (e ^ n ^ o) + (r >>> 0) + s;
            return (a << i | a >>> 32 - i) + e
        }
        ,
        b._ii = function(t, e, n, o, r, i, s) {
            var a = t + (n ^ (e | ~o)) + (r >>> 0) + s;
            return (a << i | a >>> 32 - i) + e
        }
        ,
        b._blocksize = 16,
        b._digestsize = 16,
        t.exports = function(t, e) {
            if (null == t)
                throw new Error("Illegal argument " + t);
            var n = v.wordsToBytes(b(t, e));
            return e && e.asBytes ? n : e && e.asString ? w.bytesToString(n) : v.bytesToHex(n)
        }
    })

    """)
    x1 = ctx.call("z", data)
    params['mw-t'] = int(time.time() * 1000)
    params['mw-t'] = 1643699128885
    x2 = f"{params['mw-appkey']}&{params['mw-h5-os']}&{params['mw-t']}&{params['mw-ttid']}&{params['mw-uuid']}&{apitype}&v2&{x1}&{_mwp_h5_token}"
    mw_sign = ctx.call("z", x2)
    params["mw-sign"] = mw_sign
    return params


def start(vid):
    config = {"current":0,"tot":99999}
    while config["current"]<config["tot"]:
        time.sleep(1)
        config["current"]+=1
        base_api = 'https://api.mogu.com/h5/mwp.RateWeb.pc.rate.ratelist/v2/'
        params = {
            "mw-appkey": "100028",
            "mw-uuid": "c010e862-b7a4-4bb1-a0db-2cbf74fbe2aa",
            "mw-ttid": "NMMain@mgj_pc_1.0",
            "mw-h5-os": "unknown",
            "data": '{"pageSize":20,"sort":1,"isNewDetail":1,"page":'+str(config["current"])+',"type":1,"marketType":"market_mogujie","itemId":"'+str(vid)+'","clientType":"pc"}'
        }
        _mwp_h5_token = 'a59a5de69535dc6c6ce9998c1f8d49ea_1643693248578'
        apitype = 'mwp.RateWeb.pc.rate.ratelist'
        params_news = dogetparams(params, _mwp_h5_token, apitype)
        pprint.pprint(params_news)
        res = requests.get(base_api, headers=headers, params=params_news).json().get("data")
        for icom in res.get("list"):
            print(icom.get('style'),icom.get('time'),icom.get('content').strip())
        if config["current"] == 1:
            config["tot"] = (res.get("total") //20)+1

if  __name__ == "__main__":

    start('1n0w85s')


