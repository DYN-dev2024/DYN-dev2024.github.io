import os
import re

directory = './content'

# 这个正则专门抓取您 2026041502.md 里面的那种“没有 padding、顺序错乱”的旧 span 标签
pattern_old_span = re.compile(r'<span style="color:red; font-weight:bold; background-color:yellow;">(.*?)</span>')

# 替换为我们最完美的标准格式（加入 padding:0 4px 让左右有舒适的留白）
replacement_span = r'<span style="color:red; background-color:yellow; font-weight:bold; padding:0 4px;">\1</span>'

modified_count = 0

print("正在全局扫描并优化标签间距...\n")

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.md'):
            filepath = os.path.join(root, file)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            original_content = content
            
            # 执行替换
            content = pattern_old_span.sub(replacement_span, content)

            if content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ 已成功注入 Padding 优化间距: {filepath}")
                modified_count += 1

print(f"\n🎉 处理完成！共为您优化了 {modified_count} 个文件。")
input("请按回车键 (Enter) 退出程序...")