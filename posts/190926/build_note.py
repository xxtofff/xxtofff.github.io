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
html {
  box-sizing: border-box;
}

*, *:before, *:after {
  box-sizing: inherit;
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
}

.nav-name {
  color: #ffffff !important;
  font-size: 24px !important;
  font-weight: 400 !important;
  text-decoration: none !important;
  white-space: nowrap;
  display: inline-flex;
  align-items: center;
  gap: 12px;
}

.nav-name span {
  font-weight: 400 !important;
}

.nav-name:hover {
  color: #ffffff !important;
  font-weight: 700 !important;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 42px;
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
   Hamburger menu
   ========================= */

.toc-toggle {
  position: fixed;
  top: 14px;
  left: 24px;
  width: 36px;
  height: 36px;
  padding: 0;
  border: none;
  background: transparent;
  cursor: pointer;
  z-index: 1100;
}

.toc-toggle span {
  position: absolute;
  left: 5px;
  top: 16px;
  width: 26px;
  height: 3px;
  margin: 0;
  padding: 0;
  background: #d0d0d0;
  border-radius: 2px;
  transform-origin: 13px 1.5px;
  transition: background 0.2s ease, transform 0.25s ease, opacity 0.2s ease;
}

.toc-toggle span:nth-child(1) {
  transform: translateY(-8px);
}

.toc-toggle span:nth-child(2) {
  transform: translateY(0);
}

.toc-toggle span:nth-child(3) {
  transform: translateY(8px);
}

.toc-toggle:hover span {
  background: #ffffff;
}

.toc-toggle.active span:nth-child(1) {
  transform: translateY(0) rotate(45deg);
}

.toc-toggle.active span:nth-child(2) {
  opacity: 0;
  transform: translateY(0) scaleX(0);
}

.toc-toggle.active span:nth-child(3) {
  transform: translateY(0) rotate(-45deg);
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
  grid-template-columns: 230px minmax(0, 1fr);
  column-gap: 30px;
  align-items: start;
  transition: grid-template-columns 0.35s ease, column-gap 0.35s ease;
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
  top: 89px;
  width: 230px;
  max-height: calc(100vh - 115px);
  overflow-y: auto;
  align-self: start;
  font-family: "Noto Sans", "Helvetica Neue", Helvetica, Arial, sans-serif !important;
  transform: translateX(0);
  transition: transform 0.35s ease, opacity 0.25s ease;
  will-change: transform, opacity;
}

.note-toc-title {
  margin: 0 0 14px 0;
  color: #242424;
  font-size: 17px !important;
  font-weight: 700 !important;
  line-height: 1.4;
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

/* =========================
   Hidden TOC
   ========================= */

body.toc-hidden .note-layout {
  grid-template-columns: 0 minmax(0, 1fr);
  column-gap: 0;
}

body.toc-hidden .note-toc {
  transform: translateX(-30px);
  opacity: 0;
  pointer-events: none;
}

/* =========================
   Responsive
   ========================= */

@media screen and (max-width: 1550px) {
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
    column-gap: 0;
  }
}

@media screen and (max-width: 960px) {
  .nav-inner {
    width: 100%;
    max-width: none;
    margin: 0;
    padding: 18px 20px 18px 65px;
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

  body.toc-hidden .note-layout {
    width: 100%;
    max-width: none;
    grid-template-columns: 0 minmax(0, 1fr);
    column-gap: 0;
  }

  .toc-toggle {
    left: 20px;
  }
}

@media screen and (max-width: 760px) {
  .note-layout {
    display: block;
    width: 100%;
    max-width: none;
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
    transform: translateX(0);
  }

  body.toc-hidden .note-toc {
    transform: translateX(calc(-100% - 30px));
    opacity: 1;
    width: 260px;
    max-height: calc(100vh - 160px);
  }

  .jp-RenderedHTMLCommon {
    font-size: 17px !important;
  }
}

@media screen and (max-width: 500px) {
  .site-nav {
    height: 120px;
  }

  .nav-inner {
    padding: 16px 15px 16px 60px;
    gap: 24px;
  }

  .nav-name {
    font-size: 21px !important;
  }

  .nav-links {
    width: 100%;
    justify-content: center;
    gap: 24px;
  }

  .nav-links a {
    font-size: 16px !important;
  }

  body.jp-Notebook {
    padding-top: 120px !important;
  }

  .toc-toggle {
    top: 42px;
    left: 20px;
  }

  .note-toc {
    top: 140px;
  }

  body.jp-Notebook > .note-layout {
    padding-top: 25px;
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

<button class="toc-toggle" id="toc-toggle" type="button" aria-label="Show table of contents" aria-expanded="false">
  <span></span>
  <span></span>
  <span></span>
</button>
"""

toc_html = """
<aside class="note-toc" id="note-toc">
  <div class="note-toc-title">Contents</div>
  <ul id="toc-list"></ul>
</aside>
"""

toc_script = """<script>
document.addEventListener("DOMContentLoaded",()=>{const tocList=document.getElementById("toc-list"),toggle=document.getElementById("toc-toggle"),headings=document.querySelectorAll("main h2, main h3");headings.forEach((heading,index)=>{if(!heading.id)heading.id="section-"+index;const li=document.createElement("li");li.className=heading.tagName.toLowerCase()==="h3"?"toc-h3":"toc-h2";const link=document.createElement("a");link.href="#"+heading.id;link.textContent=heading.textContent.replace("¶","").trim();link.addEventListener("click",()=>{heading.scrollIntoView({behavior:"smooth",block:"start"});});li.appendChild(link);tocList.appendChild(li);});toggle.addEventListener("click",()=>{const hidden=document.body.classList.toggle("toc-hidden");toggle.classList.toggle("active",!hidden);toggle.setAttribute("aria-expanded",String(!hidden));toggle.setAttribute("aria-label",hidden?"Show table of contents":"Hide table of contents");});const links=Array.from(tocList.querySelectorAll("a"));const observer=new IntersectionObserver(entries=>{entries.forEach(entry=>{if(entry.isIntersecting){links.forEach(link=>link.classList.remove("active"));const activeLink=tocList.querySelector('a[href="#'+entry.target.id+'"]');if(activeLink)activeLink.classList.add("active");}});},{rootMargin:"-90px 0px -70% 0px",threshold:0});headings.forEach(heading=>observer.observe(heading));});
</script>"""

html = html.replace("</head>", header_css + "</head>", 1)

html = html.replace("<main>", '<div class="note-layout">' + toc_html + "<main>", 1)

html = html.replace("</main>", "</main></div>", 1)

html = html.replace(
    '<body class="jp-Notebook" data-jp-theme-light="true" data-jp-theme-name="JupyterLab Light">',
    '<body class="jp-Notebook toc-hidden" data-jp-theme-light="true" data-jp-theme-name="JupyterLab Light">' + header_html,
    1
)

html = html.replace("</body>", toc_script + "</body>", 1)

html_file.write_text(html, encoding="utf-8")
generated_file.unlink()