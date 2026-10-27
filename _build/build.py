"""「飯塚山笠を調べよう」の index.html と gemini.html を content.py から作る。
python3 _build/build.py
"""
import html
from pathlib import Path
import content as C

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://a-tozak.github.io/yamakasa-shiraberu/"
DESC = "4年社会「地域で受けつがれてきたもの」で、飯塚山笠を子どもが自分で調べる単元の進め方。5つの段階、調べるときのくり返し、Gemini Notebookの作り方、計画シートやインタビューの紙をまとめました。"

CSS = """
:root{--ink:#15181c;--black:#0e0f11;--paper:#ffffff;--wash:#f5f5f2;--line:#e2e2de;--sub:#5f646b;--accent:#2b5fd9;--acc-wash:#eef3fd;--red:#d12a1e;--red-wash:#fff4f3;
 --font:"BIZ UDPGothic","Hiragino Sans","Hiragino Kaku Gothic ProN","Noto Sans JP",sans-serif}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--font);line-height:1.75;font-size:17px}
img{max-width:100%;display:block}
a{color:var(--accent);overflow-wrap:anywhere}
h1,h2,h3{word-break:auto-phrase;color:var(--black);line-height:1.4}
ruby rt{font-size:.5em}
.hero h1 ruby rt{font-size:.3em;letter-spacing:.1em}
.hero h1{padding-top:.25em}
.top{position:sticky;top:0;z-index:5;background:var(--black);color:#fff}
.top .in{max-width:1080px;margin:0 auto;padding:10px 16px;display:flex;gap:16px;align-items:center;flex-wrap:wrap}
.top b{font-size:15px;letter-spacing:.04em}
.top nav{display:flex;gap:14px;flex-wrap:wrap;font-size:14px}
.top nav a{color:#d9dbe0;text-decoration:none}
.top nav a:hover{color:#fff}
.wrap{max-width:1080px;margin:0 auto;padding:0 16px}
.hero{padding:36px 0 18px}
.hero .unit{color:var(--sub);font-size:15px;margin:0}
.hero h1{font-size:clamp(30px,5vw,46px);margin:.1em 0 .3em;letter-spacing:.04em}
.mondai{border:2.5px solid var(--red);border-radius:10px;padding:14px 18px;background:var(--red-wash)}
.mondai span{display:inline-block;background:var(--red);color:#fff;font-weight:700;font-size:14px;padding:1px 10px;border-radius:4px}
.mondai p{margin:.4em 0 0;font-size:clamp(19px,2.6vw,24px);font-weight:700;word-break:auto-phrase}
section{padding:34px 0 8px}
.sh{display:flex;align-items:baseline;gap:12px;border-bottom:2px solid var(--black);padding-bottom:6px;margin-bottom:18px}
.sh h2{margin:0;font-size:clamp(22px,3vw,28px)}
.sh p{margin:0;color:var(--sub);font-size:15px}
/* 段階の流れ（上の一覧） */
.flow{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin-bottom:26px}
.flow a{display:block;text-decoration:none;color:inherit;background:var(--wash);border-radius:10px;padding:10px 10px 12px;position:relative;text-align:center}
.flow a:not(:last-child)::after{content:"";position:absolute;right:-9px;top:50%;width:0;height:0;border-left:8px solid #b9bcc2;border-top:8px solid transparent;border-bottom:8px solid transparent;transform:translateY(-50%)}
.flow .n{display:inline-flex;width:30px;height:30px;border-radius:50%;background:var(--black);color:#fff;align-items:center;justify-content:center;font-weight:700}
.flow a:last-child .n{background:var(--red)}
.flow b{display:block;font-size:17px;margin-top:4px}
.flow small{display:block;color:var(--sub);font-size:13px;line-height:1.5;word-break:auto-phrase}
/* 段階の中身 */
.stage{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.15fr);gap:24px;align-items:center;padding:22px 0;border-bottom:1px solid var(--line)}
.stage:nth-of-type(even) .pics{order:2}
.stage .pics{display:grid;gap:8px}
.stage .pics.two{grid-template-columns:1fr 1fr}
.stage .pics img{border-radius:10px;background:#fff;border:1px solid var(--line)}
.stage .lab{display:inline-flex;gap:8px;align-items:center;font-weight:700;color:var(--sub);font-size:15px}
.stage .lab i{font-style:normal;display:inline-flex;width:28px;height:28px;border-radius:50%;background:var(--black);color:#fff;align-items:center;justify-content:center}
.stage.last .lab i{background:var(--red)}
.stage h3{font-size:clamp(21px,2.8vw,26px);margin:.2em 0 .5em}
.stage ul{margin:0;padding-left:1.2em}
.stage li{margin-bottom:.35em}
.use{margin-top:10px;display:flex;flex-wrap:wrap;gap:6px}
.use span{font-size:13px;border:1px solid var(--accent);color:var(--accent);border-radius:20px;padding:1px 10px;background:var(--acc-wash)}
/* くり返しの図 */
.cycle{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:24px;align-items:center}
.cycle svg{width:100%;height:auto}
.cycle .note{background:var(--wash);border-radius:10px;padding:14px 18px}
.yakusoku{border:2px solid var(--red);border-radius:10px;padding:12px 18px;margin-top:16px}
.yakusoku b{color:var(--red)}
.yakusoku ul{margin:.3em 0 0;padding-left:1.2em}
/* リンク・ファイル */
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px}
.card{border:1px solid var(--line);border-radius:10px;padding:12px 16px;background:#fff}
.card b{display:block;font-size:16px}
.card small{display:block;color:var(--sub);font-size:14px;line-height:1.6;margin-top:2px}
.card a{font-size:14px;word-break:break-all}
.btn{display:inline-block;background:var(--accent);color:#fff;text-decoration:none;font-weight:700;border-radius:8px;padding:8px 16px;margin-top:6px}
.gem{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:20px;align-items:center;background:var(--acc-wash);border-radius:12px;padding:18px 20px}
.gem h3{margin:0 0 .3em}
.gem p{margin:0}
.teacher{color:var(--sub);font-size:15px}
pre{white-space:pre-wrap;font-family:inherit;font-size:15px;background:var(--wash);border-radius:8px;padding:12px 14px;margin:8px 0 0}
.copyrow{display:flex;justify-content:space-between;align-items:center;gap:10px}
.copyrow b{font-size:17px}
button.cp{font:inherit;font-size:14px;font-weight:700;border:1.5px solid var(--accent);color:var(--accent);background:#fff;border-radius:6px;padding:4px 12px;cursor:pointer;white-space:nowrap}
ol.steps{padding-left:1.4em}
ol.steps li{margin-bottom:.6em}
footer{margin-top:40px;background:var(--wash);padding:22px 0;font-size:14px;color:var(--sub)}
footer .wrap{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap}
@media (max-width:820px){
 .flow{grid-template-columns:1fr 1fr}
 .flow a:not(:last-child)::after{display:none}
 .stage,.cycle,.gem{grid-template-columns:1fr}
 .stage:nth-of-type(even) .pics{order:0}
}
@media print{.top{position:static}}
"""

COPY_JS = """<script>
function cp(b){const t=b.closest('.copy').querySelector('pre').innerText;
 const done=()=>{const o=b.textContent;b.textContent='コピーしました';setTimeout(()=>b.textContent=o,1500)};
 if(navigator.clipboard){navigator.clipboard.writeText(t).then(done).catch(()=>fb(t,done))}else fb(t,done)}
function fb(t,done){const a=document.createElement('textarea');a.value=t;document.body.appendChild(a);a.select();
 try{document.execCommand('copy');done()}catch(e){}a.remove()}
</script>"""


def head(title, path, desc):
    url = BASE + path
    return f"""<!doctype html>
<html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:title" content="{title}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{BASE}og.png"><meta property="og:locale" content="ja_JP">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0e0f11">
<link rel="icon" href="https://a-tozak.github.io/School_Stock/favicon.ico">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"LearningResource","name":"{title}","description":"{desc}","inLanguage":"ja","educationalLevel":"小学校4年","learningResourceType":"単元の進め方","publisher":{{"@type":"Organization","name":"School Stock","url":"https://a-tozak.github.io/School_Stock/"}},"url":"{url}"}}</script>
<style>{CSS}</style></head><body>
<header class="top"><div class="in"><b>飯塚山笠を調べよう</b><nav><a href="./#zentai">全体</a><a href="./#kurikaeshi">調べ方</a><a href="gemini.html">Gemini Notebook</a><a href="./#kami">使う紙</a></nav></div></header>
"""


FOOT = """<footer><div class="wrap"><span>4年社会「地域で受けつがれてきたもの」の実践（2026年10月〜11月）。子どもの名前と学校の中のことは入れていません。</span>
<span><a href="https://a-tozak.github.io/School_Stock/">School Stock</a>　© School Stock</span></div></footer>"""


def cycle_svg():
    import math
    W, H, cx, cy, r = 560, 520, 280, 262, 190
    n = len(C.CYCLE)
    parts = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="調べるときのくり返し">',
             '<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#8a8f96"/></marker></defs>',
             f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#e2e2de" stroke-width="18"/>']
    pts = []
    for i in range(n):
        a = -math.pi / 2 + 2 * math.pi * i / n
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    for i in range(n):
        a1 = -math.pi / 2 + 2 * math.pi * (i + .22) / n
        a2 = -math.pi / 2 + 2 * math.pi * (i + .78) / n
        x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
        x2, y2 = cx + r * math.cos(a2), cy + r * math.sin(a2)
        parts.append(f'<path d="M{x1:.1f},{y1:.1f} A{r},{r} 0 0 1 {x2:.1f},{y2:.1f}" fill="none" stroke="#8a8f96" stroke-width="2.5" marker-end="url(#ah)"/>')
    for i, ((t, s), (x, y)) in enumerate(zip(C.CYCLE, pts)):
        fill = "#2b5fd9" if i == 2 else "#0e0f11"
        parts.append(f'<g><rect x="{x-92:.1f}" y="{y-30:.1f}" width="184" height="60" rx="12" fill="#fff" stroke="{fill}" stroke-width="2.5"/>'
                     f'<text x="{x:.1f}" y="{y-5:.1f}" text-anchor="middle" font-size="18" font-weight="700" fill="{fill}">{t}</text>'
                     f'<text x="{x:.1f}" y="{y+17:.1f}" text-anchor="middle" font-size="13" fill="#5f646b">{s}</text></g>')
    parts.append(f'<text x="{cx}" y="{cy-6}" text-anchor="middle" font-size="20" font-weight="700" fill="#0e0f11">調べるときの</text>'
                 f'<text x="{cx}" y="{cy+22}" text-anchor="middle" font-size="20" font-weight="700" fill="#0e0f11">くり返し</text></svg>')
    return "".join(parts)


def index():
    flow = "".join(f'<a href="#{s["key"]}"><span class="n">{i}</span><b>{s["name"]}</b><small>{s["head"].replace("　", "")}</small></a>'
                   for i, s in enumerate(C.STAGES, 1))
    stages = []
    for i, s in enumerate(C.STAGES, 1):
        pics = "".join(f'<img src="img/{f}" alt="" loading="lazy">' for f in s["img"])
        last = " last" if i == len(C.STAGES) else ""
        stages.append(f'''<div class="stage{last}" id="{s["key"]}"><div class="pics{" two" if len(s["img"]) > 1 else ""}">{pics}</div>
<div><span class="lab"><i>{i}</i>{s["name"]}</span><h3>{s["head"]}</h3><ul>{"".join(f"<li>{d}</li>" for d in s["do"])}</ul>
<div class="use">{"".join(f"<span>{u}</span>" for u in s["use"])}</div></div></div>''')
    yak = "".join(f"<li>{y}</li>" for y in C.YAKUSOKU)
    links = "".join(f'<div class="card"><b>{html.escape(t)}</b><small>{html.escape(n)}</small><a href="{u}" target="_blank" rel="noopener">{u}</a></div>' for t, u, n in C.LINKS)
    files = "".join(f'<div class="card"><b>{html.escape(t)}</b><small>{html.escape(n)}</small><a class="btn" href="files/{f}" download>ダウンロード</a></div>' for t, f, n in C.FILES)
    return head(C.TITLE + "｜4年社会 単元の進め方", "", DESC) + f'''<main class="wrap">
<div class="hero"><p class="unit">{C.UNIT}</p><h1>{C.TITLE_R}</h1>
<div class="mondai"><span>学習問題</span><p>{C.MONDAI}</p></div></div>

<section id="zentai"><div class="sh"><h2>学習の進め方</h2><p>5つの順番で進めます</p></div>
<div class="flow">{flow}</div>
{"".join(stages)}
</section>

<section id="kurikaeshi"><div class="sh"><h2>調べるときのくり返し</h2><p>調べるたびに、この順でたしかめます</p></div>
<div class="cycle">{cycle_svg()}<div><div class="note">{C.CYCLE_NOTE}</div>
<div class="yakusoku"><b>やくそく</b><ul>{yak}</ul></div></div></div>
</section>

<section id="gemini"><div class="gem"><div><h3>調べるときは、Gemini Notebookに相談できます</h3>
<p>{C.R("検索", "けんさく")}のことばや、どの{C.SHIRYO}を見ればよいか、何が分かれば予想が合っていると言えるかを、いっしょに考えてくれます。答えは、どの{C.SHIRYO}に書いてあるかといっしょに返ってきます。</p></div>
<a class="btn" href="gemini.html">使い方を見る</a></div></section>

<section id="shirabesaki"><div class="sh"><h2>調べる先</h2><p>まず、ここから読みます</p></div>
<div class="cards">{links}</div>
<p class="teacher">2026年10月20日に、開けることを確かめました。写真は公式のページで見ます。</p></section>

<section id="kami"><div class="sh"><h2>使う紙</h2><p>先生向け</p></div>
<p class="teacher">この単元で使った紙です。印刷して使えます。例の中の学校名と人の名前は「〇〇」にしてあります。</p>
<div class="cards">{files}</div></section>
</main>{FOOT}</body></html>'''


def gemini():
    qs = "".join(f'<div class="card copy"><div class="copyrow"><b>{html.escape(t)}</b><button class="cp" onclick="cp(this)">コピーする</button></div><pre>{html.escape(q)}</pre></div>' for t, q in C.NB_QUESTIONS)
    src = "".join(f"<li>{html.escape(t)}<br><small><a href=\"{u}\" target=\"_blank\" rel=\"noopener\">{u}</a></small></li>" for t, u, n in C.LINKS)
    d = "飯塚山笠を調べる4年生のために、Gemini Notebookを相談相手にする作り方。入れる資料、会話の設定に貼る文、子どもの聞き方の例。"
    return head("Gemini Notebookで調べる｜飯塚山笠を調べよう", "gemini.html", d) + f'''<main class="wrap">
<div class="hero"><p class="unit">{C.UNIT}</p><h1>Gemini Notebookで調べる</h1>
<p>Gemini Notebookは、入れた{C.SHIRYO}の中から答えて、どこに書いてあるかを教えてくれます。答えを聞くためではなく、調べ方を相談するために使います。</p></div>

<section><div class="sh"><h2>子どもの聞き方</h2><p>［　］の中を自分の言葉に書きかえて聞きます</p></div>
<div class="cards">{qs}</div>
<div class="yakusoku"><b>やくそく</b><ul>
<li>名前、住所、学校名は書かない。</li>
<li>答えをそのまま写さない。教えてもらった{C.SHIRYO}を開いて、自分で読む。</li>
<li>Googleで{C.R("検索", "けんさく")}するときも、出てきた答えだけで決めずに、リンク先のページを開いて、どこに書いてあるかをたしかめる。</li>
</ul></div></section>

<section><div class="sh"><h2>先生の準備</h2><p>15分ほどでできます</p></div>
<ol class="steps">
<li>学校のGoogleアカウントで <a href="https://notebooklm.google.com/" target="_blank" rel="noopener">Gemini Notebook</a> を開き、新しいノートブックを作ります。名前は「{C.NB_NAME}」にします。</li>
<li>ソースに、下の「調べる先」のウェブサイトを1つずつ追加します。あわせて、「単元の手引き」のテキストを追加します。</li>
<li>チャットの設定（会話のスタイルを決める画面）で、自分で指示を書く欄を選び、下の「会話の設定に貼る文」を貼ります。</li>
<li>先に先生が、下の「子どもの聞き方」で試します。答えにどの{C.SHIRYO}が示されるかを確かめます。</li>
<li>子どもに共有します。子どもがGemini Notebookを使えるかは、学校や市の決まりで確かめてください。</li>
</ol>
<p class="teacher">画面の名前は、Googleの更新で変わることがあります。</p>
<div class="card copy"><div class="copyrow"><b>会話の設定に貼る文</b><button class="cp" onclick="cp(this)">コピーする</button></div><pre>{html.escape(C.NB_INSTRUCTION)}</pre></div>
<p><a class="btn" href="files/tebiki.txt" download>単元の手引き（テキスト）をダウンロード</a></p>
<h3>調べる先（ソースに入れるウェブサイト）</h3><ul>{src}</ul>
</section>
</main>{FOOT}{COPY_JS}</body></html>'''


def tebiki():
    out = ["飯塚山笠を調べるための手引き（4年社会「地域で受けつがれてきたもの」）", "",
           "学習問題", "飯塚山笠や博多祇園山笠など、祭りや行事は何のためにつくって、なぜみんな参加するのだろう。", "",
           "10月27日に学級で出た予想", "何のためにつくられたか：昔あった出来事をお祝いするため／神社やお寺に関係がある／病気が起きないように",
           "参加する理由：人との関係をつなぐため／受けついでほしい／町をもり上げるため／家が近い人に協力", "",
           "調べるときのくり返し"]
    out += [f"・{t}：{s}" for t, s in C.CYCLE]
    out += ["", "分かったことの種類",
            "・事実：本当にあったこと（年、できごと、決まり）",
            "・言い伝え：「〜といわれる」と書いてあること",
            "・人の思い：「〜したい」「〜と思う」と話していること",
            "・分からなかった：資料にのっていないこと", "",
            "予想のたしかめ方の例",
            "予想「100年くらい前に始まった」→ 始まった年が分かれば、たしかめられる。80年前から120年前までなら合っている。", "",
            "調べる先"]
    out += [f"・{t}　{u}　{n}" for t, u, n in C.LINKS]
    out += ["", "やくそく", "・話を聞いた人の名前は書かない。", "・家の人が山笠に出ているかどうかは書かない。", "・資料に書いていないことは「分からなかった」と書く。"]
    return "\n".join(out)


if __name__ == "__main__":
    (ROOT / "index.html").write_text(index(), encoding="utf-8")
    (ROOT / "gemini.html").write_text(gemini(), encoding="utf-8")
    (ROOT / "files").mkdir(exist_ok=True)
    (ROOT / "files" / "tebiki.txt").write_text(tebiki(), encoding="utf-8")
    (ROOT / "sitemap.xml").write_text(f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{BASE}</loc></url><url><loc>{BASE}gemini.html</loc></url></urlset>
''', encoding="utf-8")
    print("built")
