import os
import re

directory = './content'

# 1. 扒掉已经转换好的 HTML 标签外层的“反引号”地雷
pattern_html_ticks = re.compile(r'`(<span style="color:red; background-color:yellow; font-weight:bold; padding:0 4px;">.*?</span>)`')

# 2. 处理带有反引号的星号邀请码： `**S123789**`
pattern_bold_ticks = re.compile(r'`\*\*\s*([a-zA-Z0-9]+)\s*\*\*`')

# 3. 处理普通的星号邀请码： **S123789** (严格限定为4位以上的大写字母和数字，绝不误伤中文)
pattern_bold_normal = re.compile(r'\*\*([A-Z0-9]{4,})\*\*')

replacement_span = r'<span style="color:red; background-color:yellow; font-weight:bold; padding:0 4px;">\1</span>'

modified_count = 0
print("开始深度清理文件中的隐藏符号...\n")

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.md'):
            filepath = os.path.join(root, file)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            original_content = content
            
            # 依次执行三种清理
            content = pattern_html_ticks.sub(r'\1', content)
            content = pattern_bold_ticks.sub(replacement_span, content)
            content = pattern_bold_normal.sub(replacement_span, content)

            if content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ 已完美修复: {filepath}")
                modified_count += 1

print(f"\n🎉 处理完成！共为您清理了 {modified_count} 个文件。")
input("请按回车键 (Enter) 退出程序...")