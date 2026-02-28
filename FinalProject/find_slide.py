import re

def fix_slide_numbers():
    with open(r'c:\Users\kim50\OneDrive\Desktop\FinalProject\발표용.HTML', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    slide_count = 0
    changed = False

    for i in range(len(lines)):
        line = lines[i]
        if '<div class="slide-container"' in line or '<div class=\'slide-container\'' in line or '<div class="slide-container ' in line:
            slide_count += 1
            
            # Look backwards to find the comment
            for j in range(i-1, max(-1, i-5), -1):
                if '<!--' in lines[j] and '-->' in lines[j] and ('Slide' in lines[j] or 'slide' in lines[j]):
                    old_comment = lines[j]
                    
                    # Regex replacement: "Slide X:" -> "Slide Y:", "Slide X " -> "Slide Y "
                    new_comment = re.sub(r'(?i)Slide\s+\d+(\.\d+)?(\s*:)', f'Slide {slide_count}\\2', old_comment)
                    if new_comment == old_comment:
                        new_comment = re.sub(r'(?i)Slide\s+\d+(\.\d+)?:?', f'Slide {slide_count}:', old_comment)
                        
                    if old_comment != new_comment:
                        print(f'Replacing line {j+1}: {old_comment.strip()}  ->  {new_comment.strip()}')
                        lines[j] = new_comment
                        changed = True
                    break

    if changed:
        with open(r'c:\Users\kim50\OneDrive\Desktop\FinalProject\발표용.HTML', 'w', encoding='utf-8') as f:
            f.writelines(lines)
        print("File updated successfully.")
    else:
        print("No changes needed.")

if __name__ == "__main__":
    fix_slide_numbers()
