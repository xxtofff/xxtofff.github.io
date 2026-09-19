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
.site-nav {
  width: 100%;
  height: 64px;
  background: #242424;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 9999;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
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
  font-size: 24px;
  font-weight: 500;
  text-decoration: none !important;
  white-space: nowrap;
}

.nav-name:hover {
  color: #ffffff !important;
  font-weight: 500;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 42px;
}

.nav-links a {
  color: #d0d0d0 !important;
  font-size: 18px;
  font-weight: 400;
  text-decoration: none !important;
  white-space: nowrap;
}

.nav-links a:hover {
  color: #ffffff !important;
  font-weight: 600;
}

body.jp-Notebook {
  padding-top: 64px !important;
  overflow-x: hidden !important;
}

body.jp-Notebook > main {
  width: 1250px !important;
  max-width: calc(100% - 80px) !important;
  margin: 0 auto !important;
  padding-top: 35px !important;
  padding-bottom: 60px !important;
}

.jp-Notebook {
  background: var(--jp-layout-color0);
}

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

@media screen and (max-width: 960px) {
  .nav-inner {
    max-width: calc(100% - 40px);
  }

  .nav-name {
    font-size: 22px;
  }

  .nav-links {
    gap: 28px;
  }

  .nav-links a {
    font-size: 17px;
  }

  body.jp-Notebook > main {
    width: 100% !important;
    max-width: none !important;
    padding: 30px 25px 50px 25px !important;
  }
}

@media screen and (max-width: 600px) {
  .site-nav {
    height: 110px;
  }

  .nav-inner {
    max-width: none;
    padding: 15px 20px;
    flex-direction: column;
    justify-content: center;
    gap: 12px;
  }

  .nav-name {
    font-size: 21px;
  }

  .nav-links {
    gap: 24px;
  }

  .nav-links a {
    font-size: 16px;
  }

  body.jp-Notebook {
    padding-top: 110px !important;
  }

  body.jp-Notebook > main {
    padding: 25px 20px 45px 20px !important;
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

theme_script = """
<script>
const savedTheme = localStorage.getItem("theme");
const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
if (savedTheme === "dark" || (!savedTheme && prefersDark)) document.body.classList.add("dark-mode");
</script>
"""

html = html.replace("</head>", header_css + "</head>", 1)
html = html.replace('<body class="jp-Notebook" data-jp-theme-light="true" data-jp-theme-name="JupyterLab Light">', '<body class="jp-Notebook" data-jp-theme-light="true" data-jp-theme-name="JupyterLab Light">' + header_html, 1)
html = html.replace("</body>", theme_script + "</body>", 1)

html_file.write_text(html, encoding="utf-8")
generated_file.unlink()