from pathlib import Path
import subprocess
import sys

notebook = Path("linear_regression_from_scratch.ipynb")
html_file = Path("index.html")

subprocess.run([sys.executable, "-m", "nbconvert", "--to", "html", "--template", "lab", str(notebook)], check=True)

generated_file = notebook.with_suffix(".html")
html = generated_file.read_text(encoding="utf-8")

html = html.replace("<title>linear_regression_from_scratch</title>", "<title>Linear Regression from Scratch</title>", 1)

favicon_html = """
<link rel="icon" type="image/png" href="/assets/images/favicon.png">
"""

header_css = """
<style>
html {
  box-sizing: border-box;
  scroll-behavior: smooth;
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

.nav-name img {
  width: 32px;
  height: 32px;
  object-fit: contain;
  display: block;
  flex-shrink: 0;
  transform: scale(1.35);
}

.nav-name:hover {
  color: #ffffff !important;
  font-weight: 400 !important;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 42px;
}

.nav-links a {
  color: #d0d0d0 !important;
  font-size: 18px !important;
  text-decoration: none !important;
  white-space: nowrap;
}

.nav-links a:hover {
  color: #ffffff !important;
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

</style>
"""

header_html = """
<nav class="site-nav">
  <div class="nav-inner">
    <a class="nav-name" href="/">
      <img src="/assets/images/favicon_inv.png" alt="">
      <span>Adam Mendoza</span>
    </a>

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

html = html.replace("</head>", favicon_html + header_css + "</head>", 1)
html = html.replace("<main>", '<div class="note-layout">' + toc_html + "<main>", 1)
html = html.replace("</main>", "</main></div>", 1)
html = html.replace('<body class="jp-Notebook" data-jp-theme-light="true" data-jp-theme-name="JupyterLab Light">', '<body class="jp-Notebook toc-hidden" data-jp-theme-light="true" data-jp-theme-name="JupyterLab Light">' + header_html, 1)
html = html.replace("</body>", toc_script + "</body>", 1)

html_file.write_text(html, encoding="utf-8")
generated_file.unlink()