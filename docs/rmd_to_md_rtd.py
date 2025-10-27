import subprocess
from pathlib import Path
import re

# -----------------------------
# 配置路径
# -----------------------------
rmd_file = Path("docs/source/CHESS.Rmd")  # 输入 Rmd 文件
output_md = Path("docs/source/CHESS.md")  # 输出 Markdown 文件
tmp_md = Path("docs/source/CHESS_tmp.md") # 临时 Markdown

# -----------------------------
# 1️⃣ 使用 R 渲染 Rmd -> Markdown
# -----------------------------
cmd = [
    "Rscript", "-e",
    f'rmarkdown::render("{rmd_file}", output_format="md_document", output_file="{tmp_md}")'
]

print("🔹 Rendering Rmd to temporary Markdown...")
subprocess.run(cmd, check=True)

# -----------------------------
# 2️⃣ 读取生成的 Markdown
# -----------------------------
with tmp_md.open("r", encoding="utf-8") as f:
    md_lines = f.readlines()

# -----------------------------
# 3️⃣ 删除 YAML 头
# -----------------------------
yaml_start = None
yaml_end = None
for i, line in enumerate(md_lines):
    if line.strip() == "---":
        if yaml_start is None:
            yaml_start = i
        elif yaml_end is None:
            yaml_end = i
            break

if yaml_start is not None and yaml_end is not None:
    md_lines = md_lines[:yaml_start] + md_lines[yaml_end+1:]

# -----------------------------
# 4️⃣ 替换 R 代码块 `{r ...}` -> ```r
# -----------------------------
md_lines = [re.sub(r'^```(\{r.*\})', "```r", line) for line in md_lines]

# -----------------------------
# 5️⃣ 写入最终 Markdown 文件
# -----------------------------
with output_md.open("w", encoding="utf-8") as f:
    f.writelines(md_lines)

print(f"✅ R Markdown has been converted to ReadTheDocs-compatible Markdown: {output_md}")

# -----------------------------
# 可选：删除临时文件
# -----------------------------
tmp_md.unlink()
