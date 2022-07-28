
        function DateStr(){
    "11-15 10:03:16"
    var date = new Date()
    var month = date.getMonth()
    var day = date.getDate()+1
    var hours = date.getHours()
    var minutes = date.getMinutes()
    var second = date.getSeconds()
    var re_str = month.toString() + '-' + day.toString()+' '+hours.toString()+':'+minutes.toString()+':'+second.toString()
    var all_str = "2021-11-12 17:41 assemble 11-14 09:59:46 " + re_str
    return  all_str

}
        function E() {
            return String(parseInt((new Date).getTime()) + 268)
        }
        function B() {
            var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : {}
              , t = "e"
              , n = "x"
              , a = "1"
              , o = E();
            return e[t + n + a] = function(e) {
                for (var t = "9527".split("").map(function(e) {
                    return Number(e)
                }), n = e.split("").map(function(e) {
                    return Number(e)
                }), a = 7 * n.reduce(function(e, t) {
                    return e + t
                }, 0) % 10, o = [], r = 0, i = 0; i < n.length; i++)
                    o[i] = (n[i] + t[r]) % 10,
                    r = (r + 1) % t.length;
                for (var c = t.length % n.length, s = Array.apply(null, {
                    length: 10
                }), l = 0; l < c; l++)
                    s[l] = o[o.length - l - 1];
                s[c] = a;
                for (var u = c + 1; u < o.length + 1; u++)
                    s[u] = o[o.length - u];
                return T(s.join(""))
            }(o),
            t = null,
            n = null,
            a = null,
            e
        }
function T(e) {
            for (var t = [], n = function() {
                for (var e = [], t = 0; t < 36; t++)
                    t >= 0 && t <= 9 ? e.push(t) : e.push(String.fromCharCode(t + 87));
                return e
            }(); e; ) {
                var a = e % 36;
                t.unshift(n[a]),
                e = parseInt(e / 36)
            }
            return t.join("")
        }

function main(){
    var n = B(n = {
        platform: "pc",
        version: "5.8.5",
        ua: "Chrome 95",
        ex: DateStr()
        })
    console.log(n)
    return n
}


