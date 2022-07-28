var CryptoJS = require("crypto-js");
var crypto = require('crypto');
var HmacSha1 = require('crypto-js/hmac-sha1');
var Base64 = require('crypto-js/enc-base64');

function main(api) {
	var key = 'D23ABC@#56'
	var Authorization = Base64.stringify((HmacSha1(api, key)))
	var md = crypto.createHash('md5');
	var cryptostr = md.update(Authorization)
		.digest('hex');
	console.log(cryptostr)
	return cryptostr
}


function aes256(text) {
	const crypto = require('crypto');
	const algorithm = 'aes-256-cbc';
	const keyStr = 'D23ABC@#56'
	const ivStr = 'apidata/api/gk/score/special'
	const keyByte = Buffer.from(keyStr)
	const ivByte = Buffer.from(ivStr)
	let encryptedData = text
	let iv = Buffer.from(ivStr, 'hex');
	let encryptedText = Buffer.from(encryptedData, 'hex');
	let decipher = crypto.createDecipheriv(algorithm, Buffer.from(keyStr), iv);
	let decrypted = decipher.update(encryptedText);
	decrypted = Buffer.concat([decrypted, decipher.final()]);
	return decrypted.toString();
}


function aesDecrypt(text) {
	var u = {
		"uri": "apidata/api/gk/score/special"
	}
	var l = {
	"code": "0000",
	"message": "成功",
	"data": {
		"method": "aes-256-cbc",
		"text": text
	},
	"location": "",
	"encrydata": ""
    }
	var e, a, t, b, n;
	return (l.data = (n = (e = {
				iv: u.uri,
				text: l.data.text,
				SIGN: 'D23ABC@#56'
			})
			.iv,
			a = e.text,
			e = e.SIGN,
			e = CryptoJS.PBKDF2(e, "secret", {
				keySize: 8,
				iterations: 1e3,
				hasher: CryptoJS.algo.SHA256
			})
			.toString(),
			n = CryptoJS.PBKDF2(n, "secret", {
				keySize: 4,
				iterations: 1e3,
				hasher: CryptoJS.algo.SHA256
			})
			.toString(),
			a = CryptoJS.lib.CipherParams.create({
				ciphertext: CryptoJS.enc.Hex.parse(a)
			}),
			n = CryptoJS.AES.decrypt(a, CryptoJS.enc.Hex.parse(e), {
				iv: CryptoJS.enc.Hex.parse(n)
			}),
			JSON.parse(n.toString(CryptoJS.enc.Utf8)))),
		l
}

function main_enc(text){

    var result = aesDecrypt(text).data
    return result
}
//var r = main_enc("eab8325abc5a1440b7708431e83f79ace38694dfe7ad23799dc1ea375c38e2c704f762ae0d167b18a944e616d112ea21218fac03a39282b7860eee2e0192732d202eb902af5c7685888d8f68f8cc662deb9f407b9037951dba1673ff2af19c325d8639cd72ab36e347358791104ec8830b29707d607df5601d4952c50c47e25c007b70941823d9b47112844d4eeb0b2ec08887d6810028463f005a04fee97e5cf083a867cf88d5a3da617511ee71a700460a7fb9f89213662c517a35904f03c8bb81c6c4af73c73cb483568219b5a856a7ca111b806fbd90b34881eec6aea68cfcc7da43432d66483df6474078126c7af19a0d9e2795d11223dbd6687a778e16e702e67b20b6e02234443b7ddb11a71bb159ec48c3faa799b40241006aec412a6d0783b266f60bc8ac9fdf05f05e86de8917bc284f307c2f3342472621ec4c4c35f198f5c1079cbc15799fc9b993721867a6f9a0adc5fc73e4cdbdd7224cf0fe786d56c798336063c12f14a9f4ac312a9e8a6c905f15965caf0b1d146318bbecb0818b89af6b03fe71fe529bb0c6dc5317fb32fde9db1cf7ef8d6e717e849f1fdb0c9dda9c7f1c5fdb4cccd95dfe2bf59d0171eca079275e9b632cf7465e58a67ca72404ea445614e21a7de47c2fbcb3b1f17ad25bcc0aab996f6eae255594e079585a9d01b782c93123e367ab7e9ec68e6198ffb9eacb88474d1c55d7a1c1348fd0dfedcad24db770f5a6568c7073aaf87aa9c46a4933b6091e650155b765929b6eddf36cd830526f4c3c37d0470a2326219a54c6012ab58dc0872b642bb7fce479561d7d728b576af390ccc705abfb0470d6e1654035630f41344bf97a2bdf6e009f21c90448fac85f5bc821a11f01c08ba1dc3734fabef9df4a0a2988722059eb28c4e03b727f5b86e248a0655816f6617235b2ac913a95dd57c4319677e34155826d78f50c865ac70153b0c13658cc6f40754c75dd3e5251939654ff73f1131677a35533e8ab7f56ba45bbb9ad72c5dbedf54ffe99a0be21afc500bd887912487703073daf8d2e98435450e2758855ec51a2812e4726f7963511a0d84a4b092c63108bd5c3238144957f44942107280191b4d38e05f6ac145b038e60f0392a6293c458ed47408c6877e476d84be9236f1c7534523c3429cf646a11976624e03a39f6a11ddc18d498bf269dc8ef134a2fa57fe5398cd2d0915a7ce4122fe5f9b77c98a93d5d0574b71ea71f9fb085ce9a1e9cb3900502a06ee93023278ce1f8b5c1515279201859d1f2029a78fdb308ff96769671d96a99b7b60e830e003e50f68493653d79c91350b2f9405c789c8925e67d3a9451a5d7e5ba9ac156db06d855c34b3fbef83c73b42b5a5de71b45e68e7ae715c46a6ac8d662a8d72a590e14b2d9142dbdf72b5ce8cebfe2d47b6cf7e73e7a3d51abc81a2b56b36e55509a8499dc60e7d9d92639ee5133b67297afbc89a09068916c344d413d64bd424cde37664e9cbf4fbe9d4f18d06cb6a838bb13247f1fc6f0b06dcd169a95b3d1989e65fbf52bb1d992de9077d025c736cec39bd572e68b4c8b12cd6ef0c102330261475b930987d638aa08d110f9d3089d1dcf128183d31da115761a1a6dc862abcd121bc37925ea8e3279a05ab493d8bc164111006766a62aca3d795afa53b26c78d790236b8b03d1bf669a7d30b48014bc8d9863f505d16d9f3b1e46adff450fd40256c59c05e160ef9dde1f59f944483cbaa17be19fc3be2aeda341bf90f66accb01fff174a5cf54f8d322419c69a8fb44c8ddc3ddd594a1d981a206fa9dcd0fdaf47bfed106fbe5a5f5516ea5d793fb5c37cd0e774e61a0426f9fbac5633989e63af3023af95c5be098ab34355f70035dd070d95a0797f7b5b3615a5803649c7efd9d34c97ae73499584a4c37f0f55e0a44a21255a1379f7bc5616dfd7cd79e3361ccf4f6a3a7fdd1f56aeb8dd64530b51a641e06700618451171c887b661783c66075d5c74ad377f9efc6a1e47e311eeb6272e5df17cdd4ce859d61ca786bfe7b2c52fd663fa9c398a59f3c11891d40f4f5594a17185fd70ba3a14cf5f20d41e8b95a07ccc1deae15c927d5b15a8029e29de1991840c3068e3c6d7aacf3658eaa1f0d4432e8f3afa065c2a339b7d402fb2053aa66d08bd370b248a6bbc472942aaba09e3d1cd32cb70e7ed02f0c757553965f9f3cabf6f3b01d9f01b7fb1e707ff6b9833b1124e7fb208302f79f7201839ed2f491a78673a048456175720e8f302874a47bbce60c521c6316832dc9aa27b4c85ae3a386af87cbf29b13a0ec1f3ff62cdca00ab9de92a1aab3f3f932cdd5217d101dccb27462836b3d7a25412c05cd00a38be70bc53155049179d107a5e8607d9d741d9664f5883a119250c1baa74f965322429ed04f7d6f5c82bfc84ba3026299fdb7b5101d7b20d2eb9b3f56e893d02c024e4019d53c4b8b28c0067b452c67d55b95fd1194439a78b4fe02c3f9b9c2f7d20626061b4423a7c5be8e96d053116c0c3a0a7fd9d4b268fb18564e59139f93a515a542eb05d216c4c44e60b21dbfbd6020d013fbe242c6a7d9cda0")
//console.log(r)
