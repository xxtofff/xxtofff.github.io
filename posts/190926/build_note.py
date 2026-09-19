from pathlib import Path
import subprocess
import sys

notebook = Path("linear_regression_from_scratch.ipynb")
html_file = Path("index.html")

subprocess.run([sys.executable, "-m", "nbconvert", "--to", "html", "--template", "lab", str(notebook)], check=True)

generated_file = notebook.with_suffix(".html")
html = generated_file.read_text(encoding="utf-8")

html = html.replace("<title>linear_regression_from_scratch</title>", "<title>Linear Regression from Scratch</title>", 1)

html = html.replace(
    """MathJax.Hub.Config({
                TeX: {
                    equationNumbers: {""",
    """MathJax.Hub.Config({
                TeX: {
                    Macros: {
                        bm: ["{\\\\boldsymbol{#1}}", 1]
                    },
                    equationNumbers: {""",
    1
)

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
  color: #ffffff;
  font-size: 24px;
  font-weight: 500;
  text-decoration: none;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 42px;
}

.nav-links a {
  color: #d0d0d0;
  font-size: 18px;
  text-decoration: none;
}

.nav-links a:hover {
  color: #ffffff;
}

body.jp-Notebook {
  padding-top: 64px !important;
}

@media screen and (max-width: 960px) {
  .nav-inner {
    max-width: calc(100% - 40px);
  }

  .nav-name {
    font-size: 22px;
  }

  .nav-links a {
    font-size: 17px;
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

html = html.replace("</head>", header_css + "</head>", 1)
html = html.replace('<body class="jp-Notebook" data-jp-theme-light="true" data-jp-theme-name="JupyterLab Light">', '<body class="jp-Notebook" data-jp-theme-light="true" data-jp-theme-name="JupyterLab Light">' + header_html, 1)

html_file.write_text(html, encoding="utf-8")
generated_file.unlink()