import os
import erniebot

# Set authentication
erniebot.api_type = "aistudio"
erniebot.access_token = "8e9e050008f1e71129231efbf6b7e35303da9b07"

def generate_webpage_from_markdown(markdown_file):
    """
    Use ERNIE to convert markdown to beautiful HTML webpage
    """
    print("🤖 Step 2: Generating webpage with ERNIE...")
    
    # Read the markdown content
    if not os.path.exists(markdown_file):
        print(f"❌ Error: {markdown_file} not found!")
        print("   Please run step1_extract_pdf_v2.py first")
        return None
    
    with open(markdown_file, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    
    print(f"   → Read {len(markdown_content)} characters from markdown")
    
    # Truncate if too long (ERNIE has token limits)
    max_chars = 8000
    if len(markdown_content) > max_chars:
        print(f"   ⚠️ Content too long, using first {max_chars} characters")
        markdown_content = markdown_content[:max_chars] + "\n\n[...content truncated for web generation...]"
    
    # Create prompt for ERNIE
    prompt = f"""You are a professional web developer. Convert this technical documentation into a beautiful, modern HTML webpage.

Requirements:
1. Create a complete HTML5 document with <!DOCTYPE html>
2. Include modern CSS styling inside <style> tag:
   - Clean, professional design with dark blue header
   - Responsive layout (works on mobile)
   - Nice color scheme (use IBM blue #0f62fe, white, grays)
   - Good typography (use system fonts like Arial, Helvetica)
   - Proper spacing and margins
   - Code blocks with monospace font and light gray background
3. Add a navigation menu/table of contents if there are sections
4. Add smooth transitions and hover effects
5. Make headings stand out with proper hierarchy (h1, h2, h3)
6. Style any code examples or technical content appropriately

Content to convert:
{markdown_content}

Generate ONLY the complete HTML code. Start with <!DOCTYPE html> and end with </html>.
Do not include markdown code blocks or explanations - just pure HTML code.
"""
    
    print("   → Calling ERNIE API to generate HTML...")
    print("   ⏳ This may take 30-60 seconds...")
    
    try:
        response = erniebot.ChatCompletion.create(
            model="ernie-4.0",
            messages=[{
                "role": "user",
                "content": prompt
            }],
            temperature=0.7,
        )
        
        html_content = response.get_result()
        
        # Clean up markdown code blocks if present
        html_content = html_content.replace('``````', '')
        html_content = html_content.strip()
        
        # Ensure it starts with DOCTYPE
        if not html_content.startswith("<!DOCTYPE") and not html_content.startswith("<!doctype"):
            print("   ⚠️ Adding DOCTYPE declaration...")
            html_content = "<!DOCTYPE html>\n" + html_content
        
        # Save to index.html
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print("   ✅ Webpage generated successfully!")
        print("   → HTML saved to: index.html")
        print(f"   → File size: {len(html_content)} characters")
        
        return html_content
        
    except Exception as e:
        print(f"   ❌ Error generating webpage: {e}")
        print("\n   💡 Tip: Check your AI Studio token quota at:")
        print("      https://aistudio.baidu.com/usercenter/token")
        return None

if __name__ == "__main__":
    html = generate_webpage_from_markdown('extracted_content.md')
    
    if html:
        print("\n🎉 Step 2 Complete!")
        print("\n📋 Next steps:")
        print("   1. Open index.html in your browser to preview")
        print("      Run: explorer.exe index.html")
        print("   2. If it looks good, we'll push to GitHub")
        print("   3. Then enable GitHub Pages")
