const CryptoJS = require('crypto-JS')
function main(timesamp,page){
    var b = 'bVHm4pJn6kT8kqsJ'
    var y = '$d6eb7ff91ee257475%'
    var d = '游戏 孩子'
    var h = 10
    var text = [timesamp, b, y, d, h, page].sort().join("")
    var hashInBase64 = CryptoJS.SHA256(text).toString()
    console.log(hashInBase64)
    return hashInBase64
}
// signature
