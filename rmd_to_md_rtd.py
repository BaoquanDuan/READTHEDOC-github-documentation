import subprocess
from pathlib import Path
import re
import sys

rmd_file = Path("docs/source/CHESS.Rmd")
output_md = Path("docs/source/CHESS.md")
tmp_md = Path("docs/source/CHESS_tmp.md")

try:
    # 调用 Rscript 渲染 Rmd -> Markdown
    subprocess.run([
        "Rscript", "-e",
        f'rmarkdown::render("{rmd_file}", output_format="md_document", output_file="{tmp_md}")'
    ], check=True)
except subprocess.CalledProcessError as e:
    print(f"❌ ERROR: Failed to render {rmd_file}")
    print(e)
    sys.exit(1)  # 立即停止构建

# 读取 Markdown
try:
    with tmp_md.open("r", encoding="utf-8") as f:
        md_lines = f.readlines()
except Exception as e:
    print(f"❌ ERROR: Cannot read temporary Markdown {tmp_md}")
    print(e)
    sys.exit(1)

# 删除 YAML 头
yaml_start, yaml_end = None, None
for i, line in enumerate(md_lines):
    if line.strip() == "---":
        if yaml_start is None:
            yaml_start = i
        elif yaml_end is None:
            yaml_end = i
            break
if yaml_start is not None and yaml_end is not None:
    md_lines = md_lines[:yaml_start] + md_lines[yaml_end+1:]

# 替换 `{r ...}` 代码块为标准 ```r
md_lines = [re.sub(r'^```(\{r.*\})', "```r", line) for line in md_lines]

# 写入最终 Markdown
try:
    with output_md.open("w", encoding="utf-8") as f:
        f.writelines(md_lines)
except Exception as e:
    print(f"❌ ERROR: Cannot write output Markdown {output_md}")
    print(e)
    sys.exit(1)

# 删除临时文件
try:
    tmp_md.unlink()
except Exception:
    pass

print(f"✅ CHESS.Rmd 已转换为 ReadTheDocs Markdown: {output_md}")
