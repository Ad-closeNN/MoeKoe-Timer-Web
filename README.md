# MoeKoe Timer Web
一个将 [MoeKoe Timer](https://gist.github.com/Ad-closeNN/c83822b3bd7b65d5be003397c6829af6) 中记录的时间上传到服务器供查看的后端(Python Flask)项目。
### ???这是什么东西？

三者关系如下：
> [MoeKoe Music](https://github.com/iAJue/MoeKoeMusic)：音乐软件。\
> [MoeKoe Timer](https://gist.github.com/Ad-closeNN/c83822b3bd7b65d5be003397c6829af6)：记录 MoeKoe Music 播放音乐的时长的软件。\
> [MoeKoe Timer Web](https://github.com/Ad-closeNN/MoeKoe-Timer-Web)：将 MoeKoe Timer 记录的时间以网页的形式展现出来。

## 部署

推荐使用 [Vercel](https://vercel.com) 部署。点击下方按钮即可开始部署。这真的是一个按钮！
> [!IMPORTANT]
> **需要**输入变量 `password` 的内容！这个内容**是为 MoeKoe Timer 准备的。请务必记住这个密码，且请勿分享给他人！！！**

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/import?s=https://github.com/Ad-closeNN/MoeKoe-Timer-Web&env=password)

## 使用
### Vercel
因国内原因，你需要绑一个域名来获得API。

比如`https://123456789.vercel.app`，这类域名通常情况下无法在中国大陆直连，所以需要CNAME一个域名。

---

假设你可以查看网站的链接为 https://123.com 。访问 `https://123.com/set` ，查看是否是 `403 Forbidden`。如果是，那么将这段链接复制下来（ https://123.com/set ） 。如果不是，那就是你搞错了。

### MoeKoe Timer
1. 打开 `.timer/config.ini`
2. 把 `web_Enabled` 后的 `False` 改为 `True`
3. 将 `web_API` 等号后写入 `[你部署好后的API]`也就是上面假设的 https://123.com/set 。这里需要你自己真实的域名。别用这个123.com，除非你真的有这个域名。
4. 将 `web_Password` 等号后写入 `[你在部署的时候写的Password后的密码]`。假设是 `114514`。
5. 重新打开 MoeKoe Timer。如果你开有。
