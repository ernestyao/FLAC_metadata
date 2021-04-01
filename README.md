# FLAC_metadata

## flac_add_composition.py
Roon处理古典音乐时，会出现一首作品的几个乐章被分拆显示的问题。Roon提供的解决方案是使用`Composition/Work`和`Movement/Part`两个tag。这个python小程序就是为了自动分拆，其作用是，在曲目中找" - "（注意，包含前后空格），以此分割，之前的是作品名（`Composition`），之后的是小曲目或乐章名（`Movement`）。

例如"Brahms：Piano Concerto No.1 in D minor, Op.15 - I. Maestoso-Poco più moderato"，其中"Brahms：Piano Concerto No.1 in D minor, Op.15"就是作品名，写入`Composition`字段，"I. Maestoso-Poco più moderato"写入`Movement`字段。

所以，具体的分隔符可以按个人的习惯设置，这里是我个人喜欢的方式。

与Roon相结合的详细说明，参见我的文章吧。

P.S：`Composition-Movement`和`Work-Part`这两组对Roon来说是等价的，从习惯出发，我选了第一组名称。

使用：

1. 安装[mutagen包](https://mutagen.readthedocs.io)
2. `python3 ./flac_add_composition.py flac文件路径`

基于python 3.9.2开发。