from pathlib import Path
import subprocess
import sys

notebook = Path("linear_regression_from_scratch.ipynb")
html_file = Path("index.html")

subprocess.run([sys.executable, "-m", "nbconvert", "--to", "html", "--template", "lab", str(notebook)], check=True)

generated_file = notebook.with_suffix(".html")
html = generated_file.read_text(encoding="utf-8")

html = html.replace("<title>linear_regression_from_scratch</title>", "<title>Linear Regression from Scratch</title>", 1)

html = html.replace("""MathJax.Hub.Config({
                TeX: {
                    equationNumbers: {""", """MathJax.Hub.Config({
                TeX: {
                    Macros: {
                        bm: ["{\\\\boldsymbol{#1}}", 1]
                    },
                    equationNumbers: {""", 1)

header_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;500;700&display=swap');

html {
  box-sizing: border-box;
}

*, *:before, *:after {
  box-sizing: inherit;
}

html {
  scroll-behavior: smooth;
}

body.jp-Notebook {
  padding-top: 64px !important;
  overflow-x: hidden !important;
}

.site-nav {
  width: 100%;
  height: 64px;
  background: #242424;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 1000;
  font-family: "Noto Sans", "Helvetica Neue", Helvetica, Arial, sans-serif !important;
}

.nav-inner {
  width: 1100px;
  max-width: calc(100% - 80px);
  height: 100%;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-family: "Noto Sans", "Helvetica Neue", Helvetica, Arial, sans-serif !important;
}

.nav-name {
  color: #ffffff !important;
  font-family: "Noto Sans", "Helvetica Neue", Helvetica, Arial, sans-serif !important;
  font-size: 24px !important;
  font-weight: 500 !important;
  line-height: 1.5 !important;
  text-decoration: none !important;
  white-space: nowrap;
}

.nav-name:hover {
  color: #ffffff !important;
  font-weight: 700 !important;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 42px;
  font-family: "Noto Sans", "Helvetica Neue", Helvetica, Arial, sans-serif !important;
}

.nav-links a {
  color: #d0d0d0 !important;
  font-family: "Noto Sans", "Helvetica Neue", Helvetica, Arial, sans-serif !important;
  font-size: 18px !important;
  font-weight: 400 !important;
  line-height: 1.5 !important;
  text-decoration: none !important;
  white-space: nowrap;
}

.nav-links a:hover {
  color: #ffffff !important;
  font-weight: 700 !important;
}

/* =========================
   Notebook layout
   ========================= */

.note-layout {
  width: 1510px;
  max-width: calc(100% - 40px);
  margin: 0 auto;
  padding-top: 35px;
  padding-bottom: 60px;
  display: grid;
  grid-template-columns: 230px minmax(0, 1250px);
  column-gap: 30px;
  align-items: start;
}

body.jp-Notebook > .note-layout > main {
  width: 100% !important;
  min-width: 0 !important;
  margin: 0 !important;
  padding: 0 !important;
}

.jp-Notebook {
  background: var(--jp-layout-color0);
}

/* =========================
   Notebook typography
   ========================= */

.jp-RenderedHTMLCommon {
  font-size: 18px !important;
  line-height: 1.6 !important;
}

.jp-RenderedHTMLCommon p {
  line-height: 1.6 !important;
  margin-top: 0.9em !important;
  margin-bottom: 1.15em !important;
}

.jp-RenderedHTMLCommon h1,
.jp-RenderedHTMLCommon h2,
.jp-RenderedHTMLCommon h3,
.jp-RenderedHTMLCommon h4 {
  line-height: 1.25 !important;
  scroll-margin-top: 90px !important;
}

.jp-RenderedHTMLCommon h1 {
  margin-top: 0 !important;
  margin-bottom: 0.8em !important;
}

.jp-RenderedHTMLCommon h2 {
  margin-top: 1.8em !important;
}

.jp-RenderedHTMLCommon h3 {
  margin-top: 1.5em !important;
}

.jp-RenderedHTMLCommon img {
  max-width: 100%;
  height: auto;
}

.jp-RenderedHTMLCommon table {
  max-width: 100%;
  overflow-x: auto;
}

.jp-RenderedHTMLCommon pre {
  overflow-x: auto;
}

/* =========================
   Table of contents
   ========================= */

.note-toc {
  position: sticky;
  top: 90px;
  width: 230px;
  max-height: calc(100vh - 115px);
  overflow-y: auto;
  align-self: start;
  font-family: "Noto Sans", "Helvetica Neue", Helvetica, Arial, sans-serif !important;
  transition: opacity 0.2s ease, transform 0.2s ease;
}

.note-toc-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 12px;
}

.note-toc-title {
  margin: 0;
  color: #242424;
  font-size: 17px !important;
  font-weight: 700 !important;
  line-height: 1.4;
}

.note-toc-hide {
  border: none;
  padding: 0;
  background: transparent;
  color: #777777;
  font-family: "Noto Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 13px;
  font-weight: 400;
  cursor: pointer;
}

.note-toc-hide:hover {
  color: #242424;
  font-weight: 700;
}

.note-toc ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

.note-toc li {
  margin: 0;
  padding: 0;
}

.note-toc li.toc-h3 {
  padding-left: 14px;
}

.note-toc a {
  display: block;
  padding: 4px 0;
  color: #777777 !important;
  font-family: "Noto Sans", "Helvetica Neue", Helvetica, Arial, sans-serif !important;
  font-size: 14px !important;
  font-weight: 400 !important;
  line-height: 1.45;
  text-decoration: none !important;
}

.note-toc a:hover {
  color: #242424 !important;
  font-weight: 700 !important;
}

.note-toc a.active {
  color: #242424 !important;
  font-weight: 700 !important;
}

.toc-reopen {
  display: none;
  position: fixed;
  top: 82px;
  left: 20px;
  z-index: 950;
  border: none;
  padding: 8px 12px;
  background: #242424;
  color: #ffffff;
  font-family: "Noto Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 14px;
  font-weight: 500;
  border-radius: 3px;
  cursor: pointer;
}

.toc-reopen:hover {
  font-weight: 700;
}

/* =========================
   Collapsed TOC
   ========================= */

body.toc-hidden .note-layout {
  width: 1250px;
  max-width: calc(100% - 40px);
  grid-template-columns: 0 minmax(0, 1250px);
  column-gap: 0;
}

body.toc-hidden .note-toc {
  width: 0;
  opacity: 0;
  overflow: hidden;
  pointer-events: none;
  transform: translateX(-20px);
}

body.toc-hidden .toc-reopen {
  display: block;
}

/* =========================
   Responsive
   ========================= */

@media screen and (max-width: 1500px) {
  .note-layout {
    width: calc(100% - 40px);
    grid-template-columns: 210px minmax(0, 1fr);
    column-gap: 25px;
  }

  .note-toc {
    width: 210px;
  }

  body.toc-hidden .note-layout {
    width: calc(100% - 40px);
    grid-template-columns: 0 minmax(0, 1fr);
  }
}

@media screen and (max-width: 960px) {
  .nav-inner {
    width: 100%;
    max-width: none;
    margin: 0;
    padding: 18px 20px;
    flex-direction: column;
    justify-content: center;
    gap: 14px;
  }

  .nav-name {
    font-size: 22px !important;
  }

  .nav-links {
    gap: 28px;
  }

  .nav-links a {
    font-size: 17px !important;
  }

  .note-layout {
    width: 100%;
    max-width: none;
    grid-template-columns: 210px minmax(0, 1fr);
    column-gap: 25px;
    padding: 30px 25px 50px 25px;
  }

  .note-toc {
    width: 210px;
  }
}

@media screen and (max-width: 760px) {
  .note-layout {
    display: block;
    padding: 25px 20px 45px 20px;
  }

  .note-toc {
    position: fixed;
    top: 140px;
    left: 20px;
    width: 260px;
    max-width: calc(100vw - 40px);
    max-height: calc(100vh - 160px);
    padding: 16px;
    background: var(--jp-layout-color0);
    border: 1px solid var(--jp-border-color2);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
    z-index: 900;
  }

  .toc-reopen {
    display: block;
    top: 130px;
  }

  body.toc-hidden .note-layout {
    width: 100%;
    max-width: none;
    display: block;
  }

  body.toc-hidden .note-toc {
    width: 0;
    padding: 0;
    border: none;
    box-shadow: none;
  }

  .jp-RenderedHTMLCommon {
    font-size: 17px !important;
  }
}
</style>
"""

header_html = """
<nav class="site-nav">
  <div class="nav-inner">
    <a class="nav-name" href="/">Adam Mendoza</a>

    <div class="nav-links">
      <a href="/about/">About</a>
      <a href="/notes/">Notes</a>
    </div>
  </div>
</nav>
"""

toc_html = """
<aside class="note-toc" id="note-toc">
  <div class="note-toc-header">
    <div class="note-toc-title">Contents</div>
    <button class="note-toc-hide" id="toc-hide" type="button">Hide</button>
  </div>
  <ul id="toc-list"></ul>
</aside>
"""

toc_reopen_html = """
<button class="toc-reopen" id="toc-reopen" type="button">Contents</button>
"""

toc_script = """<script>document.addEventListener("DOMContentLoaded",()=>{const tocList=document.getElementById("toc-list"),hideButton=document.getElementById("toc-hide"),reopenButton=document.getElementById("toc-reopen"),headings=document.querySelectorAll("main h2, main h3");headings.forEach((heading,index)=>{if(!heading.id)heading.id="section-"+index;const li=document.createElement("li");li.className=heading.tagName.toLowerCase()==="h3"?"toc-h3":"toc-h2";const link=document.createElement("a");link.href="#"+heading.id;link.textContent=heading.textContent.replace("¶","").trim();link.addEventListener("click",()=>{heading.scrollIntoView({behavior:"smooth",block:"start"});});li.appendChild(link);tocList.appendChild(li);});hideButton.addEventListener("click",()=>{document.body.classList.add("toc-hidden");});reopenButton.addEventListener("click",()=>{document.body.classList.remove("toc-hidden");});const links=Array.from(tocList.querySelectorAll("a"));const observer=new IntersectionObserver(entries=>{entries.forEach(entry=>{if(entry.isIntersecting){links.forEach(link=>link.classList.remove("active"));const activeLink=tocList.querySelector('a[href="#'+entry.target.id+'"]');if(activeLink)activeLink.classList.add("active");}});},{rootMargin:"-90px 0px -70% 0px",threshold:0});headings.forEach(heading=>observer.observe(heading));});</script>"""

html = html.replace("</head>", header_css + "</head>", 1)

html = html.replace(
    "<main>",
    '<div class="note-layout">' + toc_html + "<main>",
    1
)

html = html.replace("</main>", "</main></div>", 1)

html = html.replace(
    '<body class="jp-Notebook" data-jp-theme-light="true" data-jp-theme-name="JupyterLab Light">',
    '<body class="jp-Notebook" data-jp-theme-light="true" data-jp-theme-name="JupyterLab Light">' + header_html + toc_reopen_html,
    1
)

html = html.replace("</body>", toc_script + "</body>", 1)

html_file.write_text(html, encoding="utf-8")
generated_file.unlink()